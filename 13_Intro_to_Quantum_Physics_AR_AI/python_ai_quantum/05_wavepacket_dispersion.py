"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 2: การจำลองการแผ่ขยายของแพ็กเก็ตคลื่นเกาส์เซียน (Wavepacket Dispersion)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
ฟังก์ชันคลื่นเกาส์เซียนของอนุภาคอิสระ (Free Particle Gaussian Wave Packet):
    psi(x, 0) = (1 / (2*pi*sigma_0^2))^(1/4) * exp(-x^2 / (4*sigma_0^2)) * exp(i * k_0 * x)
การกระจายเชิงเวลาตามสมการชเรอดิงเงอร์ทำให้ความกว้างของฟังก์ชันคลื่นบานออกตามเวลา:
    sigma(t) = sigma_0 * sqrt(1 + (hbar * t / (2 * m * sigma_0^2))^2)
ความหนาแน่นความน่าจะเป็น:
    |psi(x, t)|^2 = (1 / (sqrt(2*pi) * sigma(t))) * exp(- (x - v_g * t)^2 / (2 * sigma(t)^2))
โดยที่ v_g = hbar * k_0 / m คือความเร็วกลุ่ม (Group Velocity)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def run_wavepacket_simulation():
    # หน่วยธรรมชาติหรือระดับอะตอม (Atomic Units: hbar = 1, m = 1)
    hbar = 1.0
    m = 1.0
    
    sigma_0 = 1.0        # ความกว้างเริ่มต้น
    k_0 = 5.0            # เวกเตอร์คลื่นเฉลี่ย (ความเร็วกลุ่ม v_g = k_0 = 5.0)
    v_g = hbar * k_0 / m
    
    x = np.linspace(-10, 40, 1000)
    times = [0.0, 1.5, 3.0, 5.0]
    
    plt.figure(figsize=(10, 6))
    
    for t in times:
        sigma_t = sigma_0 * np.sqrt(1.0 + (hbar * t / (2.0 * m * sigma_0**2))**2)
        x_center = v_g * t
        
        prob_density = (1.0 / (np.sqrt(2 * np.pi) * sigma_t)) * np.exp(- (x - x_center)**2 / (2.0 * sigma_t**2))
        
        # ผลคูณความไม่แน่นอน Delta x * Delta p
        delta_x = sigma_t
        delta_p = hbar / (2.0 * sigma_0)
        uncertainty_product = delta_x * delta_p
        
        plt.plot(x, prob_density, lw=2, label=f't = {t:.1f} s (x_c = {x_center:.1f}, $\\Delta x\\Delta p = {uncertainty_product:.2f}\\hbar$)')
        print(f"เวลา t = {t:3.1f} s | ตำแหน่งกึ่งกลาง x = {x_center:4.1f} | ความกว้าง sigma = {sigma_t:.3f} | Dx*Dp = {uncertainty_product:.3f} hbar")

    plt.title(r"Free Particle Gaussian Wave Packet Spreading & Dispersion ($\Delta x \Delta p \ge \hbar/2$)", fontsize=13)
    plt.xlabel("Position $x$ (atomic units)", fontsize=11)
    plt.ylabel(r"Probability Density $|\psi(x, t)|^2$", fontsize=11)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig('wavepacket_dispersion.png', dpi=200)
    print(" บันทึกภาพผลการจำลองที่ 'wavepacket_dispersion.png' สำเร็จ")

if __name__ == '__main__':
    run_wavepacket_simulation()
