"""
=============================================================================
ปฏิบัติการคอมพิวเตอร์บทที่ 9: การจำลองโพรโทคอลแจกจ่ายกุญแจรหัสลับควอนตัม BB84 และการตรวจจับผู้ดักฟัง
ตำรา: ควอนตัมฟิสิกส์เบื้องต้น (Introduction to Quantum Physics)
ผู้พัฒนา: ผศ.ดร.ชีวะ ทัศนา (สาขาวิชาดิจิทัลการเกษตรและสิ่งแวดล้อม มรภ.รำไพพรรณี)
=============================================================================
ทฤษฎี:
1. Alice สุ่มบิต {0, 1} และสุ่มฐานวัด {Rectilinear (+), Diagonal (x)}
2. Bob สุ่มฐานวัด {+, x} ของตนเองอย่างเป็นอิสระ
3. กรณีไม่มีผู้ดักฟัง (No Eavesdropper):
   - เมื่อฐานตรงกัน Bob จะวัดได้บิตตรงกับ Alice 100% (QBER = 0%)
4. กรณีมีผู้ดักฟัง Eve (Intercept-Resend Attack):
   - Eve สุ่มวัดฐานผิด 50% ทำให้ฟังก์ชันคลื่นยุบตัวสู่สถานะใหม่
   - ส่งผลให้เมื่อ Alice และ Bob ฐานตรงกัน Bob มีโอกาสวัดผิด 25% (QBER = 25%)
=============================================================================
"""

import numpy as np

def simulate_bb84(num_photons=1000, eve_present=False):
    print(f"\n=== จำลอง BB84 Protocol ({num_photons} โฟตอน, ผู้ดักฟัง Eve = {eve_present}) ===")
    
    # 0 = Rectilinear (+), 1 = Diagonal (x)
    BASIS_PLUS = 0
    BASIS_X = 1
    
    # 1. Alice สร้างบิตสุ่มและฐานสุ่ม
    alice_bits = np.random.randint(0, 2, num_photons)
    alice_bases = np.random.randint(0, 2, num_photons)
    
    # 2. การเดินทางผ่านช่องสัญญาณควอนตัม (มีหรือไม่มี Eve)
    transmitted_bits = alice_bits.copy()
    
    if eve_present:
        eve_bases = np.random.randint(0, 2, num_photons)
        for i in range(num_photons):
            if eve_bases[i] != alice_bases[i]:
                # Eve วัดด้วยฐานผิด ฟังก์ชันคลื่นยุบตัวสุ่มผลลัพธ์ใหม่ 50/50
                transmitted_bits[i] = np.random.randint(0, 2)
    
    # 3. Bob สุ่มฐานและทำการวัด
    bob_bases = np.random.randint(0, 2, num_photons)
    bob_measured_bits = np.zeros(num_photons, dtype=int)
    
    for i in range(num_photons):
        if bob_bases[i] == alice_bases[i]:
            bob_measured_bits[i] = transmitted_bits[i]
        else:
            # ฐานไม่ตรงกัน Bob ได้ผลการวัดสุ่ม 50/50
            bob_measured_bits[i] = np.random.randint(0, 2)
            
    # 4. ขั้นตอนการคัดกรองฐาน (Sifting Phase) ผ่านช่องทางสาธารณะ
    matching_bases_mask = (alice_bases == bob_bases)
    alice_sifted = alice_bits[matching_bases_mask]
    bob_sifted = bob_measured_bits[matching_bases_mask]
    
    sifted_length = len(alice_sifted)
    print(f"จำนวนบิตหลังการคัดกรองฐาน (Sifted Key): {sifted_length} บิต ({sifted_length / num_photons * 100:.1f}%)")
    
    # 5. การประเมินความผิดพลาด (QBER Estimation)
    bit_errors = np.sum(alice_sifted != bob_sifted)
    qber = bit_errors / sifted_length
    
    print(f"จำนวนบิตผิดพลาด: {bit_errors} บิต")
    print(f"อัตราความผิดพลาดของบิตควอนตัม (QBER): {qber * 100:.2f}%")
    
    # เกณฑ์วิกฤตความปลอดภัย 11% (Shor-Preskill Threshold)
    if qber < 0.11:
        print(" ผลการประเมิน: ปลอดภัย สามารถดำเนินการแก้ผิดพลาดและสร้าง Shared Key สำเร็จ")
    else:
        print(" ผลการประเมิน: ตรวจพบการแทรกแซงหรือการดักฟัง! ทำการยกเลิกการสื่อสารและทิ้งกุญแจทั้งหมด")
        
    return qber

if __name__ == '__main__':
    # รันกรณีปลอดภัย (ไม่มี Eve)
    simulate_bb84(num_photons=2000, eve_present=False)
    # รันกรณีถูกดักฟัง (มี Eve)
    simulate_bb84(num_photons=2000, eve_present=True)
