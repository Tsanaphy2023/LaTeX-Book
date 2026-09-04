# LaTeX-Book

## Latex2026 Academic Project Repository

> **ที่มาและการเชื่อมโยงข้อมูล:** เอกสารและโครงสร้างโปรเจกต์นี้ได้รับการสกัดและสังเคราะห์เชิงระบบจากคลังข้อมูล Google Drive:  
> 🔗 **Google Drive Folder:** [Latex-2025 Project (Google Drive)](https://drive.google.com/drive/folders/1KoQFuMCyeBISNVKdenKzrIlFbLbTI1Ko?usp=sharing)  
> **เจ้าของโครงการ / ผู้แต่ง:** ดร.ชีวะ ทัศนา (`chewa.t@rbru.ac.th`)  
> **หน่วยงาน:** สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี (RBRU)

---

## 1. ภาพรวมโครงสร้างโครงการ (Project Architecture Overview)

คลังข้อมูลนี้จัดระเบียบชุดตำราวิชาการ หนังสือเรียน และคู่มือปฏิบัติการขั้นสูงตามมาตรฐานวิชาการระดับสากลและระเบียบมหาวิทยาลัยราชภัฏรำไพพรรณี (RBRU) โดยบูรณาการการเรียนรู้เชิงรุก (Active Learning), โมเดลทางคณิตศาสตร์, ฟิสิกส์ยุคใหม่ และเทคโนโลยีความจริงเสริม (Augmented & Extended Reality: AR/XR) ร่วมกับภาษา Python

```
Latex2026/
├── google_drive_catalog.json                 # แคตตาล็อกข้อมูลเชิงลึกพร้อม Google Drive IDs ครบทุกโฟลเดอร์
├── README.md                                 # คู่มือหลักและดัชนีภาพรวมโครงการ
├── 01_Mathematics_for_Physics_Thai/          # ตำรา: คณิตศาสตร์สำหรับฟิสิกส์ (ฉบับภาษาไทย 9 บทสมบูรณ์)
│   ├── main.tex                              # รหัสต้นฉบับหลักระดับโปรดักชัน (XeLaTeX / LuaLaTeX)
│   ├── chapters/                             # ch01 - ch09 (พิกัด, เวกเตอร์, อนุกรม, เชิงซ้อน, เมทริกซ์, แคลคูลัส, ODEs)
│   ├── frontmatter/                          # ปก, คำนำ, สารบัญ, วัตถุประสงค์การเรียนรู้
│   ├── styles/                               # แพ็กเกจจัดหน้าและธีมสี RBRU (rbru_book_style.sty)
│   └── assets/                               # แผนภาพ TikZ, เวกเตอร์ SVG และรูปประกอบ
├── 02_Mathematics_for_Physics_Eng/           # Textbook: Mathematics for Physics (English Edition)
│   ├── main.tex                              # Master English Edition Book Template
│   ├── chapters/                             # ch01 - ch09 (Coordinate Systems through Second-Order ODEs)
│   ├── styles/                               # English Math Layout & Theorem styling
│   └── assets/                               # Formula diagrams & TikZ vector graphs
├── 03_Modern_Physics_with_AR_XR_Python/      # ตำรา: ฟิสิกส์ยุคใหม่ ผสาน AR/XR และการคำนวณด้วย Python (7 บท)
│   ├── main.tex                              # Master Book Template พร้อมระบบไฮไลต์โค้ด Python
│   ├── chapters/                             # ch01 - ch07 (สัมพัทธภาพ, ควอนตัม, อนุภาค, AR/XR, นิวเคลียร์, ควอนตัมคอมพิวติง, ดาราศาสตร์)
│   ├── python_code/                          # สคริปต์จำลองฟิสิกส์ (Relativity, Schrödinger Equation, Quantum States)
│   ├── frontmatter/                          # ปกและคำนำ
│   └── styles/                               # สไตล์จัดหน้า Modern Physics
├── 04_OpenXR_STEM_Book/                      # โครงการตำราการศึกษา STEM ผ่านมาตรฐาน OpenXR
│   ├── main.tex                              # Master Template สำหรับโมดูล OpenXR 3D Interaction
│   ├── chapters/                             # สาระการเรียนรู้ระบบจำลองภาพ 3 มิติและการตรวจจับพิกัดมือ
│   └── python_code/                          # สคริปต์เชื่อมต่อและประมวลผลข้อมูลเซนเซอร์
├── 05_ARwithAI_manual/                       # คู่มือเชิงปฏิบัติการ: การพัฒนา AR ร่วมกับระบบปัญญาประดิษฐ์ (AI)
│   ├── main.tex                              # Master Manual Template
│   ├── chapters/                             # สถาปัตยกรรม Computer Vision, MediaPipe Hands และ Three.js/A-Frame
│   └── python_code/                          # การประมวลผลโมเดล AI สู่การแสดงผล AR แบบ Real-time
├── 06_Physics_Monograph/                     # โครงร่างเอกสารตำราฟิสิกส์ฉบับสมบูรณ์ (Monograph Framework)
│   ├── preamble/                             # การตั้งค่าฟอนต์ TH Sarabun New, ระยะขอบหน้าคู่-คี่ (1.5 นิ้ว)
│   ├── cover/                                # สถาปัตยกรรมหน้าปกวิชาการระดับพรีเมียม
│   ├── chapters/                             # โครงสร้างเนื้อหารองรับบทเรียนย่อย
│   ├── appendices/                           # ภาคผนวก, ค่าคงที่ทางฟิสิกส์ และตารางคณิตศาสตร์
│   ├── bibliography/                         # รายการเอกสารอ้างอิงและบรรณานุกรมมาตรฐาน APA
│   └── figures/                              # ไฟล์ภาพเวกเตอร์ความละเอียดสูง
├── assets/                                   # คลังทรัพยากรภาพส่วนกลาง (Shared Assets & Covers)
│   └── images/                               # ภาพพื้นหลังปก (cover_background_0, cover_background4)
└── scripts/                                  # เครื่องมืออัตโนมัติ (Python Utilities)
    └── inspect_catalog.py                    # ตรวจสอบและดึงข้อมูลแคตตาล็อก Google Drive
```

---

## 2. ตารางเชื่อมโยงทรัพยากรคลาวด์ (Google Drive Resource Matrix)

| โมดูล / โครงการ | ประเภท | ภาษา | Google Drive Folder ID | เอกสารที่คอมไพล์แล้ว (PDF) |
| :--- | :---: | :---: | :---: | :---: |
| **01. Mathematics for Physics (ไทย)** | ตำราวิชาการ | ไทย | [`19tnEqexZXVO4hEyt1EZ3-8Q61dknuZNF`](https://drive.google.com/drive/folders/19tnEqexZXVO4hEyt1EZ3-8Q61dknuZNF) | [ดาวน์โหลด main.pdf](https://drive.google.com/file/d/1bA8fNWuZHcsrnTG8MwqanXB-AR-jyKog/view) |
| **02. Mathematics for Physics (Eng)** | Textbook | อังกฤษ | [`1bKv91GbbTWlGHvhZVLAEmnheycCxSEpV`](https://drive.google.com/drive/folders/1bKv91GbbTWlGHvhZVLAEmnheycCxSEpV) | แหล่งรวมชุดบทเรียน 9 บทภาษาอังกฤษ |
| **03. Modern Physics with AR/XR & Python** | ตำรา / คู่มือ | ไทย/Eng | [`1jPF1wvO4uaJXWzl4lCXUqriYE5BAj6by`](https://drive.google.com/drive/folders/1jPF1wvO4uaJXWzl4lCXUqriYE5BAj6by) | [ดาวน์โหลด main.pdf](https://drive.google.com/file/d/13KlncT5qHyjMThhkJsVNii5TEuSr8mfT/view) |
| **04. OpenXR STEM Book** | โครงการตำรา | ไทย/Eng | [`1bsATvQ8KMg5Z6Gr3cmFHwfQ02JUle6sI`](https://drive.google.com/drive/folders/1bsATvQ8KMg5Z6Gr3cmFHwfQ02JUle6sI) | โครงสร้าง OpenXR Frameworks |
| **05. AR with AI Manual** | คู่มือเชิงปฏิบัติการ | ไทย/Eng | [`16JC_gWrid2L_ziUUyuLy1FtH23DsVn-9`](https://drive.google.com/drive/folders/16JC_gWrid2L_ziUUyuLy1FtH23DsVn-9) | คู่มือ MediaPipe, AI & AR |
| **06. Mathematics for Physics III** | ตำราขั้นสูง | ไทย | [`1aASZVL-47TJHZ0r9mO807Sukp1b35icr`](https://drive.google.com/drive/folders/1aASZVL-47TJHZ0r9mO807Sukp1b35icr) | โครงร่างคณิตศาสตร์ฟิสิกส์ขั้นสูง |
| **07. Physics Monograph** | แม่แบบเอกสารวิจัย/ตำรา | ไทย | [`12mnxgEPV4W3PtxEyTyXt8jVoPcx3bPi7`](https://drive.google.com/drive/folders/12mnxgEPV4W3PtxEyTyXt8jVoPcx3bPi7) | โครงร่าง Monograph ครบวงจร |
| **08. Shared Images & Cover Art** | ทรัพยากรภาพ | - | [`1TA-zxlcHbOODa7grrAc4IODO3TpZi1k6`](https://drive.google.com/drive/folders/1TA-zxlcHbOODa7grrAc4IODO3TpZi1k6) | [Cover 0](https://drive.google.com/file/d/1WP-zwU4YgfloBlQKA-TKhlGaEB_6Ey4G/view), [Cover 4](https://drive.google.com/file/d/1BXECNT1xPgBlOGezHXyNjkANj1FyQzph/view) |
| **09. doc-pdf Output** | ปลายทางส่งมอบ | PDF | [`1r0IyIvJvOhBsQ77KF6hNyBRBhIrJ6LLI`](https://drive.google.com/drive/folders/1r0IyIvJvOhBsQ77KF6hNyBRBhIrJ6LLI) | โฟลเดอร์รองรับไฟล์ PDF ผลลัพธ์ |
| **10. jason Metadata** | ข้อมูลเมทาดาตา | JSON | [`1dyHl4rOivHSi3gTBmiNEMvsGNO0LRuIv`](https://drive.google.com/drive/folders/1dyHl4rOivHSi3gTBmiNEMvsGNO0LRuIv) | ฐานข้อมูลการจัดเก็บค่าดัชนี |

---

## 3. สารบัญเนื้อหาหลักในแต่ละชุดตำรา

### 3.1 Mathematics for Physics (คณิตศาสตร์สำหรับฟิสิกส์ 9 บท)
1. **บทที่ 1: ระบบพิกัดและการแปลงพิกัด (Coordinate Systems and Transformations)**
   - พิกัดคาร์ทีเซียน (Cartesian), พิกัดทรงกระบอก (Cylindrical), พิกัดทรงกลม (Spherical) และตัวประกอบมาตราส่วน (Scale Factors)
2. **บทที่ 2: เวกเตอร์และการวิเคราะห์เวกเตอร์ (Vector Calculus & Operators)**
   - ด็อตโพรดักต์, ครอสโพรดักต์, การดำเนินการเกรเดียนต์ (Gradient), ไดเวอร์เจนซ์ (Divergence), เคิร์ล (Curl) และทฤษฎีบทการแปลง (Gauss & Stokes)
3. **บทที่ 3: อนุกรมพื้นฐานและอนุกรมกำลัง (Basic Series & Approximations)**
   - อนุกรมเรขาคณิต, อนุกรมเทย์เลอร์และแมคลอริน (Taylor & Maclaurin Series), การประมาณค่าในทางฟิสิกส์
4. **บทที่ 4: จำนวนเชิงซ้อนและฟังก์ชันตัวแปรเชิงซ้อน (Complex Numbers & Applications)**
   - สูตรของออยเลอร์ (Euler's Formula), ระนาบเชิงซ้อน, การประยุกต์ในการสั่นฮาร์มอนิกและไฟฟ้ากระแสสลับ
5. **บทที่ 5: เมทริกซ์และพีชคณิตเชิงเส้น (Matrices & Linear Transformations)**
   - การคูณเมทริกซ์, ดีเทอร์มิแนนต์, ค่าเจาะจงและเวกเตอร์เจาะจง (Eigenvalues & Eigenvectors) ในกลศาสตร์ควอนตัม
6. **บทที่ 6: แคลคูลัสเชิงอนุพันธ์ (Differential Calculus)**
   - อนุพันธ์ย่อย (Partial Derivatives), อนุพันธ์ระบุทิศทาง, กฎลูกโซ่หลายมิติ
7. **บทที่ 7: แคลคูลัสเชิงปริพันธ์ (Integral Calculus)**
   - ปริพันธ์หลายชั้น (Multiple Integrals), ปริพันธ์ตามเส้น (Line Integrals), ปริพันธ์ตามผิว (Surface Integrals)
8. **บทที่ 8: สมการเชิงอนุพันธ์สามัญอันดับหนึ่ง (First-Order ODEs)**
   - วิธีแยกตัวแปรได้, สมการเอกพันธ์, สมการเชิงเส้น และตัวประกอบปริพันธ์ (Integrating Factor)
9. **บทที่ 9: สมการเชิงอนุพันธ์สามัญอันดับสอง (Second-Order ODEs)**
   - สมการเชิงเส้นสัมประสิทธิ์คงที่, การสั่นแบบหน่วงและถูกบังคับ (Damped & Forced Oscillations)

### 3.2 Modern Physics with AR/XR & Python (ฟิสิกส์ยุคใหม่ผสาน AR/XR 7 บท)
1. **บทที่ 1: ทฤษฎีสัมพัทธภาพพิเศษ (Special Relativity)**
   - การแปลงแบบลอเรนซ์ (Lorentz Transformation), การยืดของเวลา, การหดสั้นของความยาว, สัมพัทธภาพของโมเมนตัมและพลังงาน $E = mc^2$ พร้อมการจำลองด้วย Python
2. **บทที่ 2: กลศาสตร์ควอนตัมเบื้องต้น (Quantum Mechanics)**
   - ทวิภาวะคลื่น-อนุภาค, กลศาสตร์คลื่นเดอบรอยล์, สมการชเรอดิงเงอร์ (Schrödinger Equation) และการจำลองบ่อศักย์แบบ 3 มิติ
3. **บทที่ 3: ฟิสิกส์ของอนุภาค (Particle Physics)**
   - แบบจำลองมาตรฐาน (Standard Model), ควาร์ก, เลปตอน, โบซอนเกจ และอันตรกิริยาพื้นฐาน 4 แรง
4. **บทที่ 4: สถาปัตยกรรม AR/XR ในการศึกษาวิชาฟิสิกส์ (AR/XR Educational Frameworks)**
   - WebXR, Three.js, A-Frame, MediaPipe Hand Tracking และการโต้ตอบแบบ 60 FPS ไร้สัมผัส
5. **บทที่ 5: ฟิสิกส์นิวเคลียร์และปฏิกิริยานิวเคลียร์ (Nuclear Physics)**
   - พลังงานยึดเหนี่ยว, การสลายตัวกัมมันตรังสี, ปฏิกิริยาฟิชชันและฟิวชัน
6. **บทที่ 6: การคำนวณเชิงควอนตัมเบื้องต้น (Introduction to Quantum Computing)**
   - คิวบิต (Qubits), การซ้อนทับ (Superposition), การพัวพันเชิงควอนตัม (Quantum Entanglement) และควอนตัมเกต
7. **บทที่ 7: ดาราศาสตร์ฟิสิกส์และจักรวาลวิทยา (Astrophysics & Cosmology)**
   - วิวัฒนาการของดวงดาว, หลุมดำ, การขยายตัวของเอกภพ และการตรวจวัดคลื่นความโน้มถ่วง

---

## 4. ข้อกำหนดและการคอมไพล์เอกสาร (Compilation & Tooling Requirements)

- **TeX Engine แนะนำ:** `XeLaTeX` หรือ `LuaLaTeX`
- **ชุดฟอนต์มาตรฐานวิชาการไทย:** `TH Sarabun New` หรือ `TH Sarabun PSK`
- **แพ็กเกจหลักใน LaTeX:**
  - `fontspec`, `polyglossia` / `xecjk` / `babel` สำหรับระบบอักษรไทย
  - `amsmath`, `amssymb`, `mathtools` สำหรับสูตรคณิตศาสตร์และฟิสิกส์
  - `tcolorbox`, `tikz` สำหรับกล่องนิยาม ทฤษฎีบท ตัวอย่าง และภาพประกอบเวกเตอร์
  - `listings`, `minted` สำหรับกล่องโค้ดภาษา Python
  - `geometry` ตั้งค่าระยะขอบ: ซ้าย 1.5 นิ้ว (เย็บเล่ม), ขวา 1.0 นิ้ว, บน 1.5 นิ้ว, ล่าง 1.0 นิ้ว ตามระเบียบผลงานทางวิชาการ มรภ.รำไพพรรณี (RBRU)
