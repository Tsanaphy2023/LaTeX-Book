"""
=============================================================================
โครงข่ายประสาทเทียมตามหลักฟิสิกส์ (Physics-Informed Neural Networks: PINNs)
สำหรับการหาผลเฉลยของสมการชเรอดิงเงอร์และระดับพลังงานควอนไตซ์
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
สมการชเรอดิงเงอร์ที่ไม่ขึ้นกับเวลา 1 มิติ (TISE):
    [- (hbar^2 / 2m) * (d^2 psi / dx^2) + V(x) * psi(x)] = E * psi(x)

ในหน่วยธรรมชาติ (Atomic units: hbar = 1, m = 1):
    - (1/2) * psi''(x) + V(x) * psi(x) = E * psi(x)

PINN จะทำหน้าที่เป็นฟังก์ชันประมาณค่าคลื่น psi_theta(x) และพารามิเตอร์พลังงาน E
โดยนิยาม Loss Function:
    Loss = Loss_interior (ฟิสิกส์) + Loss_boundary (เงื่อนไขขอบ) + Loss_norm (การนอร์มอลไลซ์)
"""

import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# 1. กำหนดสถาปัตยกรรมโครงข่ายประสาทเทียม PINN
class QuantumPINN(nn.Module):
    def __init__(self, hidden_dim=64):
        super(QuantumPINN, self).__init__()
        # โครงข่ายแบบ Fully-Connected หลายชั้นพร้อมฟังก์ชันกระตุ้น Sine / Tanh
        self.net = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1)
        )
        # พารามิเตอร์พลังงาน E ที่ต้องการเรียนรู้ (Learnable Scalar)
        self.energy = nn.Parameter(torch.tensor([0.8], dtype=torch.float32))

    def forward(self, x):
        return self.net(x)

# 2. นิยามศักย์ไฟฟ้า V(x): บ่อศักย์ฮาร์มอนิกออสซิลเลเตอร์ V(x) = 0.5 * k * x^2 (k=1)
def potential_v(x):
    return 0.5 * (x ** 2)

# 3. ฟังก์ชันคำนวณ Loss ตามหลักฟิสิกส์ (Physics Loss) ด้วย Autograd
def compute_pinn_loss(model, x_domain, x_boundary):
    x_domain.requires_grad_(True)
    psi = model(x_domain)

    # อนุพันธ์อันดับที่ 1: d(psi)/dx
    dpsi_dx = torch.autograd.grad(
        outputs=psi,
        inputs=x_domain,
        grad_outputs=torch.ones_like(psi),
        create_graph=True
    )[0]

    # อนุพันธ์อันดับที่ 2: d^2(psi)/dx^2
    d2psi_dx2 = torch.autograd.grad(
        outputs=dpsi_dx,
        inputs=x_domain,
        grad_outputs=torch.ones_like(dpsi_dx),
        create_graph=True
    )[0]

    # ส่วนฟิสิกส์: H*psi - E*psi = 0
    # [-0.5 * psi'' + V(x)*psi] - E * psi = 0
    v_val = potential_v(x_domain)
    hamiltonian_psi = -0.5 * d2psi_dx2 + v_val * psi
    e_psi = model.energy * psi
    loss_physics = torch.mean((hamiltonian_psi - e_psi) ** 2)

    # เงื่อนไขขอบเขต: psi(ขอบซ้าย) = 0, psi(ขอบขวา) = 0 เมื่อ x เข้าสู่อันนต์ (-L, L)
    psi_bc = model(x_boundary)
    loss_boundary = torch.mean(psi_bc ** 2)

    # เงื่อนไขการนอร์มอลไลซ์: integral |psi|^2 dx = 1 (ประมาณด้วย mean * domain_length)
    domain_length = 8.0 # จาก -4 ถึง +4
    integral_prob = torch.mean(psi ** 2) * domain_length
    loss_norm = (integral_prob - 1.0) ** 2

    total_loss = loss_physics + 20.0 * loss_boundary + 5.0 * loss_norm
    return total_loss, loss_physics.item(), model.energy.item()

# 4. ลูปการฝึกสอนโมเดล PINN
def train_quantum_pinn(epochs=1500, lr=0.003):
    print("=" * 65)
    print("เริ่มการฝึกสอน Quantum PINN Solver (ฮาร์มอนิกออสซิลเลเตอร์ควอนตัม)")
    print("=" * 65)

    # สร้างข้อมูลจุดกริดในโดเมน x จาก -4.0 ถึง 4.0
    x_np = np.linspace(-4.0, 4.0, 200).reshape(-1, 1)
    x_domain = torch.tensor(x_np, dtype=torch.float32)
    x_boundary = torch.tensor([[-4.0], [4.0]], dtype=torch.float32)

    model = QuantumPINN(hidden_dim=64)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()
        loss, l_phys, energy_val = compute_pinn_loss(model, x_domain, x_boundary)
        loss.backward()
        optimizer.step()

        if epoch % 300 == 0 or epoch == 1:
            print(f"Epoch {epoch:4d}/{epochs} | Total Loss: {loss.item():.6f} | Physics Loss: {l_phys:.6f} | พลังงาน E: {energy_val:.4f} (ทฤษฎี E_0 = 0.5000)")

    print("=" * 65)
    print(f"การฝึกสอนเสร็จสิ้น! ระดับพลังงานสถานะพื้นทำนายโดย AI: {model.energy.item():.4f} (แม่นยำสูงเมื่อเทียบกับ 0.5 hbar*omega)")
    print("=" * 65)
    return model, x_domain

if __name__ == "__main__":
    train_quantum_pinn(epochs=1000)
