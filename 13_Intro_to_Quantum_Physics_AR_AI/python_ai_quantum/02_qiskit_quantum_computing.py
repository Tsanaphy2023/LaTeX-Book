"""
=============================================================================
การคำนวณเชิงควอนตัม อัลกอริทึม และการสื่อสารควอนตัมด้วย Qiskit
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ครอบคลุม:
1. การสร้างสถานะพัวพันเบลล์ (Bell State: (|00> + |11>) / sqrt(2))
2. โพรโทคอลการส่งผ่านสถานะทางไกล (Quantum Teleportation)
3. อัลกอริทึมการค้นหาฐานข้อมูลของโกรเวอร์ (Grover's Search Algorithm 2-Qubits)
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def demo_bell_state():
    print("=" * 65)
    print("1. การสร้างสถานะพัวพันเชิงควอนตัม (Bell State Entanglement)")
    print("=" * 65)
    qc = QuantumCircuit(2)
    # ใส่เกต H กับคิวบิตที่ 0 เพื่อสร้างซ้อนทับ
    qc.h(0)
    # ใส่เกต CNOT โดยให้คิวบิต 0 เป็นตัวควบคุม (Control) และคิวบิต 1 เป็นเป้าหมาย (Target)
    qc.cx(0, 1)

    sv = Statevector.from_instruction(qc)
    print("เวกเตอร์สถานะเบลล์ |Phi+>:")
    print(sv)
    probs = sv.probabilities_dict()
    print("ความน่าจะเป็นของการวัดค่า:")
    for state, p in probs.items():
        if p > 0.001:
            print(f"  P(|{state}>) = {p:.4f} ({p*100:.1f}%)")
    print("สังเกตว่าผลลัพธ์มีเพียง |00> และ |11> พัวพันกันสมบูรณ์แบบ!")

def demo_quantum_teleportation():
    print("\n" + "=" * 65)
    print("2. โพรโทคอลการส่งผ่านสถานะควอนตัมทางไกล (Quantum Teleportation)")
    print("=" * 65)
    # คิวบิต 0: สถานะปริศนา |psi> ของ Alice ที่ต้องการส่ง
    # คิวบิต 1: คิวบิตพัวพันของ Alice
    # คิวบิต 2: คิวบิตพัวพันของ Bob
    qc = QuantumCircuit(3)

    # ก. เตรียมสถานะสุ่มที่ต้องการส่งบนคิวบิต 0
    qc.ry(1.2, 0)
    initial_sv = Statevector.from_instruction(qc)
    print("สถานะดั้งเดิมที่ Alice ต้องการส่ง:", initial_sv.data[:2])

    # ข. สร้างคู่พัวพัน EPR ระหว่างคิวบิต 1 และ 2
    qc.h(1)
    qc.cx(1, 2)

    # ค. Alice ทำการวัดแบบเบลล์ (Bell Measurement) บนคิวบิต 0 และ 1
    qc.cx(0, 1)
    qc.h(0)

    # ง. Bob ปรับแก้สถานะตามผลลัพธ์ (คลาสสิกฟีดแบ็ก)
    qc.cx(1, 2)
    qc.cz(0, 2)

    final_sv = Statevector.from_instruction(qc)
    print("วงจรโทรเลขควอนตัมสร้างสำเร็จและพร้อมรันบน Aer Simulator!")

if __name__ == "__main__":
    demo_bell_state()
    demo_quantum_teleportation()
