"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 10: ขั้นตอนวิธีการค้นหาแบบควอนตัมของโกรเวอร์ (Grover's Search Algorithm)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
ค้นหารายการเป้าหมาย |w> ในฐานข้อมูลไม่เรียงลำดับขนาด N = 2^n รายการ
1. เตรียมสถานะซ้อนทับเสมอกัน: |s> = H^{otimes n} |0> = (1/sqrt(N)) sum_{x} |x>
2. รอบทำซ้ำของโกรเวอร์ (Grover Iteration):
   G = - R_s * R_w = (2 |s><s| - I) * (I - 2 |w><w|)
   - Oracle (R_w): พลิกเฟสของสถานะเป้าหมาย |w> -> -|w>
   - Diffuser (2 |s><s| - I): สะท้อนแอมพลิจูดรอบค่าเฉลี่ย (Inversion about the average)
3. จำนวนรอบทำซ้ำที่เหมาะสมที่สุด: k_opt ~= (pi / 4) * sqrt(N)
4. การเร่งความเร็วแบบควอนตัม: O(sqrt(N)) เทียบกับ O(N) บนคอมพิวเตอร์คลาสสิก
=============================================================================
"""

import numpy as np

def run_grover_search(n_qubits=3, target_idx=5):
    N = 2**n_qubits
    k_opt = int(np.round((np.pi / 4.0) * np.sqrt(N)))
    print(f"\n=== จำลองขั้นตอนวิธีของโกรเวอร์ ({n_qubits} คิวบิต, N = {N} รายการ, เป้าหมาย |{target_idx}>) ===")
    print(f"จำนวนรอบทำซ้ำที่เหมาะสมที่สุด: k_opt = {k_opt} รอบ (คอมพิวเตอร์คลาสสิกต้องสุ่มเฉลี่ย {N/2:.1f} ครั้ง)")
    
    # 1. สร้างสถานะเริ่มต้น |s>
    state = np.ones(N) / np.sqrt(N)
    
    # ตัวดำเนินการสะท้อนรอบค่าเฉลี่ย (Diffuser) D = 2|s><s| - I
    s = np.ones(N) / np.sqrt(N)
    diffuser = 2.0 * np.outer(s, s) - np.eye(N)
    
    print(f"รอบเริ่มต้น k = 0: แอมพลิจูดเป้าหมาย = {state[target_idx]:.4f} | ความน่าจะเป็น = {state[target_idx]**2 * 100:.2f}%")
    
    for k in range(1, k_opt + 2):
        # 1. Oracle: พลิกเครื่องหมายของสถานะเป้าหมาย
        state[target_idx] = -state[target_idx]
        
        # 2. Diffuser: ขยายแอมพลิจูดรอบค่าเฉลี่ย
        state = diffuser @ state
        
        prob_target = state[target_idx]**2
        print(f"รอบที่ k = {k}: แอมพลิจูดเป้าหมาย = {state[target_idx]:.4f} | ความน่าจะเป็น = {prob_target * 100:6.2f}%")

    measured_outcome = np.argmax(state**2)
    print(f" ผลลัพธ์การวัดที่มีความน่าจะเป็นสูงสุด: ดัชนี {measured_outcome} (ตรงกับเป้าหมายที่ตั้งไว้: {measured_outcome == target_idx})")

if __name__ == '__main__':
    # ค้นหาเป้าหมาย |5> จาก 8 รายการ (3 คิวบิต)
    run_grover_search(n_qubits=3, target_idx=5)
    # ค้นหาเป้าหมาย |11> จาก 16 รายการ (4 คิวบิต)
    run_grover_search(n_qubits=4, target_idx=11)
