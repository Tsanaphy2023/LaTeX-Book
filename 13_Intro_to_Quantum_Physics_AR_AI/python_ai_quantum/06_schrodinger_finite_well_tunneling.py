"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 4: การหาผลเฉลยเชิงตัวเลขของบ่อศักย์จำกัดและการทะลุผ่านกำแพงศักย์ (Quantum Tunneling)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
สมการชเรอดิงเงอร์ 1 มิติ (TISE):
    - (hbar^2 / 2m) d^2 psi / dx^2 + V(x) psi(x) = E psi(x)
ระเบียบวิธีไฟไนต์ดิฟเฟอเรนซ์ (Finite Difference Method):
    d^2 psi / dx^2 ~= (psi_{i+1} - 2*psi_i + psi_{i-1}) / dx^2
แปลงเป็นปัญหาค่าเจาะจงของเมทริกซ์ H * psi = E * psi
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

def solve_finite_potential_well():
    # กำหนดพารามิเตอร์ของระบบ (Atomic Units: hbar = 1, m = 1)
    L = 10.0          # ความกว้างของขอบเขตการคำนวณ (-L/2 ถึง L/2)
    N = 800           # จำนวนกริด
    x = np.linspace(-L/2, L/2, N)
    dx = x[1] - x[0]
    
    # บ่อศักย์ลึกจำกัด (Finite Square Well)
    V0 = 20.0         # ความลึกของบ่อศักย์
    a = 2.0           # ความกว้างครึ่งหนึ่งของบ่อศักย์ (|x| < a)
    V = np.zeros(N)
    V[np.abs(x) >= a] = V0
    
    # สร้างเมทริกซ์แฮมิลโทเนียน H
    # ตัวดำเนินการพลังงานจลน์ T
    diag_T = np.ones(N) * (1.0 / (dx**2))
    off_diag_T = np.ones(N - 1) * (-0.5 / (dx**2))
    
    H = np.diag(diag_T + V) + np.diag(off_diag_T, 1) + np.diag(off_diag_T, -1)
    
    # คำนวณค่าเจาะจงและเวกเตอร์เจาะจง
    eigenvalues, eigenvectors = eigh(H)
    
    # กรองเฉพาะสถานะผูกพัน (Bound States: E < V0)
    bound_mask = eigenvalues < V0
    bound_energies = eigenvalues[bound_mask]
    bound_psi = eigenvectors[:, bound_mask]
    
    print(f"=== พบสถานะผูกพัน (Bound States) ทั้งหมด {len(bound_energies)} ระดับ ===")
    for i, E in enumerate(bound_energies):
        print(f"ระดับพลังงาน n = {i}: E_{i} = {E:7.4f} a.u. (เทียบกับกำแพง V0 = {V0:.1f})")

    plt.figure(figsize=(10, 6))
    plt.plot(x, V, 'k-', lw=2, label='Potential $V(x)$')
    
    scale_factor = 2.5
    for i in range(min(4, len(bound_energies))):
        psi = bound_psi[:, i]
        # นอร์มอลไลซ์
        psi = psi / np.sqrt(np.trapz(psi**2, x))
        E = bound_energies[i]
        plt.axhline(E, color='gray', linestyle='--', alpha=0.7)
        plt.plot(x, E + scale_factor * psi, lw=1.8, label=f'$\\psi_{i}(x)$ (E_{i} = {E:.2f})')

    plt.title("Bound States in a Finite Potential Well (FDM Eigenvalue Solver)", fontsize=13)
    plt.xlabel("Position $x$ (a.u.)", fontsize=11)
    plt.ylabel("Energy / Wavefunction (offset by E)", fontsize=11)
    plt.xlim(-L/2, L/2)
    plt.ylim(-2, V0 + 5)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, loc='upper right')
    plt.tight_layout()
    plt.savefig('finite_well_eigenstates.png', dpi=200)
    print(" บันทึกภาพผลการจำลองที่ 'finite_well_eigenstates.png' สำเร็จ")

if __name__ == '__main__':
    solve_finite_potential_well()
