# RBRU Academic Textbook & AI Agent Operational Rules

## 📌 กฎเหล็กประจำ Workspace (Mandatory Operational Rules)

1. **อัปเดตสกิลทุกครั้งที่มีการปรับปรุง แก้ไข (Always Update Skills):**
   - ทุกครั้งที่มีการแก้ไขรูปแบบ, เพิ่มกฎเกณฑ์การจัดหน้า, ปรับแต่ง LaTeX Style, หรือเพิ่มเทคนิคใหม่ๆ (เช่น การย่อหน้า 1 Tab = 1.25cm, การจัด alignment เลขหัวข้อ, การแก้คำกำพร้า/orphan words, การลบโคลอน, การจัดตาราง ฯลฯ)
   - **ต้องอัปเดตไฟล์สกิลที่เกี่ยวข้องเสมอ** ได้แก่:
     - `/Users/chewathassana/.gemini/config/skills/<skill-name>/SKILL.md` (Active runtime skill ของ Agent)
     - `my_skill2026/skills/<skill-name>/SKILL.md` (Git Skill Repository)
   - สกิลหลักที่เกี่ยวข้องกับงานตำรา ได้แก่:
     - `rbru-latex-textbook-builder`
     - `rbru-academic-formatter`
     - `modern-academic-textbook`
     - `physics-textbook-layout-architect`

2. **Commit & Push ทั้งตำราและคลังสกิลขึ้น GitHub ทุกครั้ง (Auto-sync to GitHub):**
   - หลังปรับปรุงงานและคอมไพล์ผ่าน:
     1. ทำการ commit & push โปรเจกต์ตำราใน workspace: `https://github.com/Tsanaphy2023/LaTeX-Book.git`
     2. ทำการ commit & push คลังสกิลใน `my_skill2026`: `https://github.com/Tsanaphy2023/my_skill2026.git`

3. **มาตรฐานเลย์เอาต์ตำรา มรภ.รำไพพรรณี (RBRU Masterclass Layout Standards):**
   - **ขอบกระดาษ:** ซ้าย/ใน 1.5 นิ้ว, บน 1.5 นิ้ว, ขวา/นอก 1.0 นิ้ว, ล่าง 1.0 นิ้ว
   - **การย่อหน้า:** 1 Tab = `1.25cm` (ต้องใช้ `\RequirePackage{indentfirst}` เพื่อย่อหน้าพารากราฟแรกใต้หัวข้อ)
   - **การจัดตำแหน่งหัวข้อ:** ใช้ `\makebox[1.25cm][l]{\thesection}` เพื่อให้ตัวอักษรแรกของชื่อหัวข้อเริ่มที่ 1.25cm และตรงกับแนวขอบซ้ายของเนื้อหาที่ย่อหน้า 1 Tab เสมอ
   - **ภาษาไทยวิชาการ:** ไม่ใส่เครื่องหมายทวิภาค (`:`) ท้ายคำว่า "ได้แก่", "ดังนี้", "วัตถุประสงค์", "เนื้อหา" ฯลฯ และป้องกันคำกำพร้าท้ายบรรทัด
   - **การคอมไพล์:** ต้องคอมไพล์ผ่าน 100% (0 errors, ตรวจสอบ overfull hbox)
