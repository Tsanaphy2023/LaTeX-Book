"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 9: การจำลองโพรโทคอลโทรเลขควอนตัม (Quantum Teleportation)
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
ต้องการส่งผ่านสถานะไม่ทราบค่า |psi> = alpha |0> + beta |1> จาก Alice ไปยัง Bob
โดยใช้ทรัพยากร:
1. คู่พัวพันเบลล์ (EPR Pair): (|00> + |11>) / sqrt(2) ระหว่าง Alice (q1) และ Bob (q2)
2. วงจรของ Alice: CNOT(q0 -> q1) ตามด้วย H(q0)
3. การวัดผลของ Alice บนฐานคำนวณ ได้บิตคลาสสิก (m0, m1)
4. การแก้สถานะของ Bob: ประยุกต์ใช้เกต X^{m1} Z^{m0} บน q2
ผลลัพธ์: q2 ของ Bob จะกลายสภาพเป็นสถานะ |psi> ดั้งเดิมอย่างสมบูรณ์แบบ 100%
=============================================================================
"""

import numpy as np

def simulate_teleportation_math():
    print("=== การคำนวณเชิงเวกเตอร์ของ Quantum Teleportation Protocol ===")
    
    # 1. กำหนดสถานะเป้าหมายที่ต้องการส่งผ่าน (สุ่มหรือกำหนดเอง)
    theta = np.pi / 3.0
    phi = np.pi / 4.0
    alpha = np.cos(theta / 2.0)
    beta = np.sin(theta / 2.0) * np.exp(1j * phi)
    psi_target = np.array([alpha, beta])
    
    print(f"1. สถานะเป้าหมาย |psi> = ({alpha:.4f}) |0> + ({beta:.4f}) |1>")
    print(f"   ความน่าจะเป็น |alpha|^2 = {np.abs(alpha)**2:.4f}, |beta|^2 = {np.abs(beta)**2:.4f}")
    
    # 2. เมทริกซ์เกต
    H = (1.0 / np.sqrt(2.0)) * np.array([[1, 1], [1, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    CNOT = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ], dtype=complex)
    
    # 3. สถานะเริ่มต้น 3 คิวบิต: |psi> (q0) (x) |0> (q1) (x) |0> (q2)
    q0 = psi_target
    q1 = np.array([1, 0], dtype=complex)
    q2 = np.array([1, 0], dtype=complex)
    state = np.kron(q0, np.kron(q1, q2))
    
    # 4. สร้างคู่พัวพันเบลล์ระหว่าง q1 และ q2: (H (x) I) ตามด้วย CNOT_12
    # Gate H บน q1
    H1 = np.kron(I, np.kron(H, I))
    state = H1 @ state
    # Gate CNOT บน q1, q2
    CNOT12 = np.kron(I, CNOT)
    state = CNOT12 @ state
    print("2. สร้างคู่พัวพัน Bell State (|00> + |11>)/sqrt(2) เรียบร้อย")
    
    # 5. การดำเนินการของ Alice: CNOT(q0, q1) ตามด้วย H(q0)
    CNOT01 = np.kron(CNOT, I)
    state = CNOT01 @ state
    H0 = np.kron(H, np.kron(I, I))
    state = H0 @ state
    print("3. Alice ประยุกต์ใช้ CNOT_01 และ H_0 สำเร็จ")
    
    # 6. จำลองการวัดของ Alice บน q0 และ q1 (มี 4 ผลลัพธ์ที่เป็นไปได้ แต่ละแบบน่าจะเป็น 25%)
    print("4. วิเคราะห์การวัดของ Alice และการแก้สถานะของ Bob:")
    outcomes = [
        ((0, 0), "I"),
        ((0, 1), "X"),
        ((1, 0), "Z"),
        ((1, 1), "X Z")
    ]
    
    for (m0, m1), correction in outcomes:
        # โปรเจกชันตัวดำเนินการวัด
        meas_idx = 2 * m0 + m1
        # ดึงเวกเตอร์สถานะของ q2 ที่สอดคล้องกับผลวัด
        # ในระบบ 3 คิวบิต ฐานคือ |m0 m1 q2>
        sub_state = np.array([state[4 * m0 + 2 * m1 + 0], state[4 * m0 + 2 * m1 + 1]])
        norm = np.linalg.norm(sub_state)
        sub_state = sub_state / norm
        
        # Bob ดำเนินการแก้สถานะตามผลวัด
        bob_state = sub_state.copy()
        if m1 == 1:
            bob_state = X @ bob_state
        if m0 == 1:
            bob_state = Z @ bob_state
            
        fidelity = np.abs(np.vdot(psi_target, bob_state))**2
        print(f"   ผลการวัด Alice: ({m0}, {m1}) -> Bob ใช้เกต {correction:4s} -> Fidelity = {fidelity:.6f} (สมบูรณ์ 100%)")

if __name__ == '__main__':
    simulate_teleportation_math()
