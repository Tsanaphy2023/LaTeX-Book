# จุลชีววิทยาสำหรับการเกษตร (Microbiology for Agriculture - LaTeX Source)

- **ผู้แต่ง:** ผศ.ดร.จิรภัทร จันทมาลี และ ดร.ชีวะ ทัศนา (`chewa.t@rbru.ac.th`)
- **สถาบัน:** มหาวิทยาลัยราชภัฏรำไพพรรณี (RBRU)
- **แหล่งที่มา Google Drive:** [`1IVzxkHogt7yoNrVD44y9wD3FpPctJbFn`](https://drive.google.com/drive/folders/1IVzxkHogt7yoNrVD44y9wD3FpPctJbFn)
- **ไฟล์ผลลัพธ์ PDF ฉบับเต็ม:** [ดาวน์โหลด main.pdf](https://drive.google.com/file/d/1MO0Gzf7xjlLn-KKJeydU4P9tvbXmfVCh/view) | [หน้าปก coverpage.pdf](https://drive.google.com/file/d/1f3qcZyYbwFRs8P4MQifCULA8PaOUIroO/view)

---

## โครงสร้างไฟล์ต้นฉบับ LaTeX ทั้งหมด

```
07_Microbiology_for_Agriculture_LaTeX/
├── main.tex                    # Master LaTeX Document (XeLaTeX / Polyglossia / Thai Sarabun New)
├── coverpage.tex               # หน้าปกวิชาการมาตรฐาน RBRU
├── preamble/
│   └── preamble.tex            # การตั้งค่า Geometry 1.5 นิ้ว, TikZ Section, หัวบท และภาษาไทย
├── prefaces/
│   ├── preface.tex             # คำนำตำราวิชาการ
│   └── acknowledgements.tex    # กิตติกรรมประกาศ (Drive ID: 1uMphpf3LxT1LxMtT4Qk1SH6sgFIa8a_M)
├── chapters/                   # ไฟล์เนื้อหาบทเรียน 9 บท + บทนำ
│   ├── introduction.tex        # บทนำ (Drive ID: 1piUVaKVvdfGmnmMyo73v_GwkWofOhMUk)
│   ├── chapter1.tex            # บทที่ 1 (Drive ID: 1VZbFWEe0_47ELc3-_W0uPq1KfOHDed5g)
│   ├── chapter2.tex            # บทที่ 2 (Drive ID: 1X7yxm1a9CoN5c0k-Li5I3wPo8_pFJ5TZ)
│   ├── chapter3.tex            # บทที่ 3 (Drive ID: 1MrZvwOHGlzPbpy5UlINfCd6gPRADODmn)
│   ├── chapter4.tex            # บทที่ 4 (Drive ID: 1ZTAGQ5Wby-QQ_sOd591kw7YdZ-c28XLp)
│   ├── chapter5.tex            # บทที่ 5 (Drive ID: 1jhF786kY4xAUOLkiT-HQ0gNvrhodJZZv)
│   ├── chapter6.tex            # บทที่ 6 (Drive ID: 1lq6UMLhiUXpIY2Rv0mAFBSOZMFWIB9md)
│   ├── chapter7.tex            # บทที่ 7 (Drive ID: 11WAaFBJ6-zA0Pcll0ozrDgSY8EIT7HZZ)
│   ├── chapter8.tex            # บทที่ 8 (Drive ID: 1dY3Hk_4gqPlcDyu_RCMFU_GYJ93yC2Xz)
│   └── chapter9.tex            # บทที่ 9 (Drive ID: 1FnfQUgXpl9K0SmmgaBKoJUUDIOuRZn2b)
├── appendices/                 # ภาคผนวก 4 ชุด
│   ├── appendixA.tex           # ภาคผนวก ก (Drive ID: 159G8BjtQMHlQHPOCTtox4pt_pge7d6pj)
│   ├── appendixB.tex           # ภาคผนวก ข (Drive ID: 1cyxw0CjMIRHzoQM6EwSBRAul3zDVN4m9)
│   ├── appendixC.tex           # ภาคผนวก ค (Drive ID: 1a0y1UORwItL51rXfIddgilCju5leHwtE)
│   └── appendixD.tex           # ภาคผนวก ง (Drive ID: 1aOSjRdZALmFWEGvwfThVaaRb2NeAwxUS)
├── bibliography/
│   └── references.bib          # รายการอ้างอิงและบรรณานุกรม BibTeX (Drive ID: 127JTttVqjXZpOwGHBNvwGpIDgoZgLf06)
└── figures/
    └── background.jpg          # ภาพประกอบปก (Drive ID: 14g40a6YxaPb5Udov_2gmdT7x7TV-PCMy)
```

---

## การคอมไพล์เอกสาร (XeLaTeX)
```bash
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```
