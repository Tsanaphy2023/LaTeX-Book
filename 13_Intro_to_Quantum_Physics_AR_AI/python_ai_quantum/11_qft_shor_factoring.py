"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 10: การแปลงฟูเรียร์ควอนตัม (QFT) และขั้นตอนวิธีของชอร์ (Shor's Algorithm)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
1. การแปลงฟูเรียร์ควอนตัม (Quantum Fourier Transform: QFT):
   QFT |j> = (1 / sqrt(N)) sum_{k=0}^{N-1} e^{2 pi i j k / N} |k>
2. อัลกอริทึมของชอร์ (Shor's Algorithm) สำหรับการแยกตัวประกอบ N = p * q:
   - แปลงปัญหาไปสู่การหาคาบ r ของฟังก์ชัน f(x) = a^x mod N
   - เมื่อได้คาบ r เป็นเลขคู่ และ a^{r/2} != -1 mod N
   - คำนวณ gcd(a^{r/2} - 1, N) และ gcd(a^{r/2} + 1, N) เพื่อหาตัวประกอบเฉพาะ
=============================================================================
"""

import numpy as np
import math

def qft_matrix(n_qubits):
    """สร้างเมทริกซ์การแปลงฟูเรียร์ควอนตัมขนาด 2^n x 2^n"""
    N = 2**n_qubits
    omega = np.exp(2j * np.pi / N)
    matrix = np.zeros((N, N), dtype=complex)
    for j in range(N):
        for k in range(N):
            matrix[j, k] = omega**(j * k)
    return matrix / np.sqrt(N)

def find_period_classical(a, N):
    """หาคาบ r ของ f(x) = a^x mod N (จำลองสิ่งที่ QFT/QPE สกัดได้ในคอมพิวเตอร์ควอนตัม)"""
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None

def shor_factorization(N):
    print(f"\n=== จำลองขั้นตอนวิธีของชอร์สำหรับการแยกตัวประกอบ N = {N} ===")
    
    # ตรวจสอบว่าเป็นเลขคู่หรือไม่
    if N % 2 == 0:
        return 2, N // 2
        
    np.random.seed(42)
    attempts = 0
    while attempts < 20:
        attempts += 1
        # 1. สุ่มจำนวนเต็ม a ในช่วง 2 ถึง N - 1
        a = np.random.randint(2, N)
        gcd_val = math.gcd(a, N)
        if gcd_val > 1:
            print(f"ความบังเอิญ: สุ่ม a = {a} ได้ gcd({a}, {N}) = {gcd_val} ทันที!")
            return gcd_val, N // gcd_val
            
        print(f"รอบที่ {attempts}: สุ่มเลือกฐาน a = {a} (ซึ่ง gcd({a}, {N}) = 1)")
        
        # 2. คอมพิวเตอร์ควอนตัมหาคาบ r ด้วย QPE + QFT
        r = find_period_classical(a, N)
        print(f"   ควอนตัมสกัดคาบ (Period) ได้: r = {r} (เนื่องจาก {a}^{r} mod {N} = {pow(a, r, N)})")
        
        # 3. เงื่อนไขของชอร์: r ต้องเป็นเลขคู่
        if r % 2 != 0:
            print("   คาบ r เป็นเลขคี่ -> สุ่มค่า a ใหม่...")
            continue
            
        # 4. ตรวจสอบว่า a^{r/2} != -1 mod N
        half_power = pow(a, r // 2, N)
        if (half_power + 1) % N == 0:
            print(f"   a^(r/2) = {half_power} = -1 mod {N} (Trivial Factor) -> สุ่มค่า a ใหม่...")
            continue
            
        # 5. คำนวณตัวประกอบเฉพาะ
        factor1 = math.gcd(half_power - 1, N)
        factor2 = math.gcd(half_power + 1, N)
        
        if factor1 > 1 and factor2 > 1 and factor1 * factor2 == N:
            print(f" สำเร็จ! พบตัวประกอบเฉพาะของ N = {N}: {factor1} และ {factor2} (เพราะ {factor1} x {factor2} = {N})")
            return factor1, factor2
            
    return None, None

def demonstrate_qft_properties():
    print("=== ตรวจสอบคุณสมบัติของเมทริกซ์ QFT 3-Qubit (N = 8) ===")
    F = qft_matrix(3)
    # ตรวจสอบความเป็นเมทริกซ์เอกภาพ: F^dagger * F = I
    is_unitary = np.allclose(F.conj().T @ F, np.eye(8))
    print(f"เมทริกซ์ QFT ขนาด 8x8 เป็นเมทริกซ์เอกภาพ (Unitary Matrix): {is_unitary}")

if __name__ == '__main__':
    demonstrate_qft_properties()
    # ทดลองแยกตัวประกอบ N = 15 (3 x 5)
    shor_factorization(15)
    # ทดลองแยกตัวประกอบ N = 21 (3 x 7)
    shor_factorization(21)
