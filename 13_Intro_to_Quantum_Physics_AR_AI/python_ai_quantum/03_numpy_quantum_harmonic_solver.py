"""
=============================================================================
การแก้สมการชเรอดิงเงอร์ด้วยระเบียบวิธีไฟไนต์ดิฟเฟอเรนซ์ (Finite Difference Method)
และหาค่าไอเกนระดับพลังงานควอนไตซ์ด้วย NumPy (Zero-Dependency Quantum Solver)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
"""

import numpy as np

def solve_quantum_harmonic_oscillator(n_points=400, x_max=5.0):
    print("=" * 68)
    print("การคำนวณระดับพลังงานและฟังก์ชันคลื่นตัวแกว่งกวัดฮาร์มอนิกควอนตัม (NumPy FDM)")
    print("=" * 68)
    
    # 1. สร้างพิกัดกริดเชิงพื้นที่
    x = np.linspace(-x_max, x_max, n_points)
    dx = x[1] - x[0]
    
    # 2. ศักย์ไฟฟ้าฮาร์มอนิก V(x) = 0.5 * k * x^2 (ในหน่วยธรรมชาติ m=1, hbar=1, omega=1)
    V = 0.5 * (x ** 2)
    
    # 3. สร้างเมทริกซ์แฮมิลโทเนียน H = T + V ด้วยไฟไนต์ดิฟเฟอเรนซ์ 3 จุด (Second Derivative)
    # T = - (1/2) * (d^2 / dx^2)
    main_diag = (1.0 / (dx ** 2)) + V
    off_diag = -0.5 / (dx ** 2) * np.ones(n_points - 1)
    
    H = np.diag(main_diag) + np.diag(off_diag, -1) + np.diag(off_diag, 1)
    
    # 4. หาค่าไอเกน (Eigenvalues: Energies) และเวกเตอร์ไอเกน (Eigenvectors: Wavefunctions)
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    
    print("ผลการคำนวณระดับพลังงาน 5 สถานะแรก:")
    for n in range(5):
        E_num = eigenvalues[n]
        E_exact = n + 0.5 # ทฤษฎี: (n + 1/2) hbar * omega
        err = np.abs(E_num - E_exact) / E_exact * 100
        print(f"  สถานะ n={n} | E_num = {E_num:.5f} | E_exact = {E_exact:.5f} | คลาดเคลื่อน: {err:.4f}%")
        
    print("=" * 68)
    print("การคำนวณเสร็จสิ้นด้วยความแม่นยำสูง! พร้อมพล็อตฟังก์ชันคลื่น |psi_n(x)|^2")
    return x, eigenvalues[:5], eigenvectors[:, :5]

if __name__ == "__main__":
    solve_quantum_harmonic_oscillator()
