"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 1: การจำลองการแผ่รังสีของวัตถุดำและ Curve Fitting
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
1. กฎการแผ่รังสีของพลังค์ (Planck's Radiation Law):
   u(lambda, T) = (8 * pi * h * c / lambda^5) / (exp(h * c / (lambda * k_B * T)) - 1)
2. กฎของเรย์ลี-ยีนส์ (Rayleigh-Jeans Law - Classical Limit):
   u_RJ(lambda, T) = (8 * pi * k_B * T) / lambda^4
3. กฎการกระจัดของวีน (Wien's Displacement Law):
   lambda_max * T = b (โดย b = 2.89777 * 10^-3 m*K)
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ค่าคงที่มูลฐานทางฟิสิกส์ (SI Units)
h = 6.62607015e-34    # ค่าคงที่พลังค์ (J*s)
c = 2.99792458e8      # อัตราเร็วแสงในสุญญากาศ (m/s)
k_B = 1.380649e-23    # ค่าคงที่โบลต์ซมันน์ (J/K)
b_wien = 2.89777e-3   # ค่าคงที่การกระจัดของวีน (m*K)

def planck_spectral_density(wavelength, T):
    """คำนวณความหนาแน่นพลังงานเชิงสเปกตรัมตามทฤษฎีควอนตัมของพลังค์"""
    exponent = (h * c) / (wavelength * k_B * T)
    # ป้องกัน Overflow สำหรับความยาวคลื่นสั้นมากๆ
    exponent = np.clip(exponent, 0, 500)
    numerator = 8 * np.pi * h * c / (wavelength**5)
    denominator = np.expm1(exponent)
    return numerator / denominator

def rayleigh_jeans_spectral_density(wavelength, T):
    """คำนวณความหนาแน่นพลังงานตามทฤษฎีฟิสิกส์คลาสสิกของเรย์ลี-ยีนส์"""
    return (8 * np.pi * k_B * T) / (wavelength**4)

def run_blackbody_simulation():
    print("=== จำลองการแผ่รังสีของวัตถุดำและการเปรียบเทียบฟิสิกส์ยุคเก่า-ใหม่ ===")
    
    # กำหนดช่วงความยาวคลื่น (100 nm ถึง 3000 nm)
    wavelengths = np.linspace(100e-9, 3000e-9, 1000)
    
    # อุณหภูมิต่างๆ ของวัตถุดำ
    temperatures = [4000, 5000, 5800, 7000] # 5800 K คืออุณหภูมิพื้นผิวดวงอาทิตย์
    
    plt.figure(figsize=(10, 6))
    
    for T in temperatures:
        u_planck = planck_spectral_density(wavelengths, T)
        lambda_max = b_wien / T
        print(f"อุณหภูมิ T = {T:4d} K | lambda_max = {lambda_max*1e9:6.1f} nm (วีน)")
        plt.plot(wavelengths * 1e9, u_planck, label=f'Planck: T = {T} K')
        # มาร์กจุดยอดของสเปกตรัม
        u_peak = planck_spectral_density(np.array([lambda_max]), T)[0]
        plt.scatter([lambda_max * 1e9], [u_peak], color='red', s=30, zorder=5)

    # เปรียบเทียบกับเรย์ลี-ยีนส์ที่ T = 5800 K (วิบัติภัยอัลตราไวโอเลต)
    u_rj = rayleigh_jeans_spectral_density(wavelengths, 5800)
    plt.plot(wavelengths * 1e9, u_rj, 'k--', alpha=0.6, label='Rayleigh-Jeans (5800 K - UV Catastrophe)')

    plt.title("Blackbody Radiation Spectrum: Planck vs Classical Rayleigh-Jeans", fontsize=13)
    plt.xlabel(r"Wavelength $\lambda$ (nm)", fontsize=11)
    plt.ylabel(r"Spectral Energy Density $u(\lambda)$ $(\mathrm{J/m^4})$", fontsize=11)
    plt.ylim(0, 3.5e-3)
    plt.xlim(100, 3000)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig('blackbody_spectrum_simulation.png', dpi=200)
    print(" บันทึกภาพผลการจำลองที่ 'blackbody_spectrum_simulation.png' สำเร็จ")

if __name__ == '__main__':
    run_blackbody_simulation()
