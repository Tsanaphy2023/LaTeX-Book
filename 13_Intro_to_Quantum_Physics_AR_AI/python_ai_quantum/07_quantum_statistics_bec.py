"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 7: การเปรียบเทียบสถิติควอนตัม (Fermi-Dirac, Bose-Einstein, Maxwell-Boltzmann)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
1. การแจกแจงแบบแฟร์มี-ดิแรก (Fermi-Dirac - สำหรับเฟอร์มิออน เช่น อิเล็กตรอน สปินกึ่ง):
   f_FD(E) = 1 / (exp((E - mu) / (k_B * T)) + 1)
2. การแจกแจงแบบโบส-ไอน์สไตน์ (Bose-Einstein - สำหรับโบซอน สปินจำนวนเต็ม):
   f_BE(E) = 1 / (exp((E - mu) / (k_B * T)) - 1)  (โดย E > mu)
3. การแจกแจงแบบคลาสสิกแมกซ์เวลล์-โบลต์ซมันน์ (Maxwell-Boltzmann - ลิมิตคลาสสิก):
   f_MB(E) = exp(-(E - mu) / (k_B * T))
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def run_quantum_statistics():
    print("=== การแจกแจงความน่าจะเป็นตามสถิติควอนตัม ===")
    
    # กำหนดให้ระดับพลังงานเคมี mu = 0 eV และ k_B * T = 0.2 eV
    mu = 0.0
    kT = 0.2
    
    # ช่วงพลังงาน E - mu
    delta_E = np.linspace(-1.0, 2.0, 600)
    
    # คำนวณ Fermi-Dirac
    f_fd = 1.0 / (np.exp((delta_E - mu) / kT) + 1.0)
    
    # คำนวณ Maxwell-Boltzmann
    f_mb = np.exp(- (delta_E - mu) / kT)
    
    # คำนวณ Bose-Einstein (เฉพาะเมื่อ E > mu)
    delta_E_be = np.linspace(0.01, 2.0, 500)
    f_be = 1.0 / (np.exp((delta_E_be - mu) / kT) - 1.0)
    
    plt.figure(figsize=(10, 6))
    plt.plot(delta_E, f_fd, 'b-', lw=2.5, label='Fermi-Dirac (Fermions: Pauli Exclusion, max <= 1)')
    plt.plot(delta_E, f_mb, 'k--', lw=2, alpha=0.8, label='Maxwell-Boltzmann (Classical Limit)')
    plt.plot(delta_E_be, f_be, 'r-', lw=2.5, label='Bose-Einstein (Bosons: Condensation as $E \\to \\mu$)')
    
    plt.axvline(0, color='gray', linestyle=':', label=r'Chemical Potential $\mu$')
    plt.axhline(1.0, color='blue', linestyle=':', alpha=0.5)
    
    plt.title("Comparison of Quantum Statistics: FD vs BE vs Classical MB", fontsize=13)
    plt.xlabel(r"Energy difference $(E - \mu)$ [$\mathrm{eV}$]", fontsize=11)
    plt.ylabel(r"Average Occupation Number $\langle n \rangle$", fontsize=11)
    plt.ylim(0, 3.5)
    plt.xlim(-1.0, 2.0)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, fontsize=10)
    plt.tight_layout()
    plt.savefig('quantum_statistics_comparison.png', dpi=200)
    print(" บันทึกภาพผลการจำลองที่ 'quantum_statistics_comparison.png' สำเร็จ")

if __name__ == '__main__':
    run_quantum_statistics()
