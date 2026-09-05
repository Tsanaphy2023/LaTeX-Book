#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script for Book 11: ฟิสิกส์พื้นฐานและคู่มือปฏิบัติการสำหรับวิทยาศาสตร์ชีวภาพและสิ่งแวดล้อม
(Fundamental Physics and Laboratory Manual for Life and Environmental Sciences)
Complies with RBRU Academic Textbook Masterclass Standards.
"""

import os
import re
import zipfile
import xml.etree.ElementTree as ET
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
BACKMATTER_DIR = os.path.join(BASE_DIR, "backmatter")
os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(BACKMATTER_DIR, exist_ok=True)

DOCX_MAIN = os.path.join(BASE_DIR, "source_docs/02_ข้อสอบและใบงานปฏิบัติการ/2026-08-20-หนังสือฟิสิกส์พื้นฐาน-ฉบับสมบูรณ์.docx")
LAB_FILES = glob.glob(os.path.join(BASE_DIR, "source_docs/02_ข้อสอบและใบงานปฏิบัติการ/LAB Physics/*วัดละเอียด*.docx"))

def clean_heading_text(text):
    text = re.sub(r'\\textit\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\\textbf\{([^}]+)\}', r'\1', text)
    text = re.sub(r'\s*\([^)]*\)', '', text)
    text = text.replace(':', '').replace('：', '').strip()
    return text

def clean_latex(text):
    if not text:
        return ""
    text = text.replace("&", "\\&")
    text = text.replace("#", "\\#")
    text = text.replace("_", "\\_")
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", "``").replace("”", "''")
    # Replace unicode math and greek symbols that are not supported in text font
    unicode_math_map = {
        'Σ': r'$\Sigma$',
        'τ': r'$\tau$',
        'α': r'$\alpha$',
        'β': r'$\beta$',
        'γ': r'$\gamma$',
        'θ': r'$\theta$',
        'λ': r'$\lambda$',
        'π': r'$\pi$',
        'ω': r'$\omega$',
        'Ω': r'$\Omega$',
        'Δ': r'$\Delta$',
        'μ': r'$\mu$',
        '⁻': r'$^-$',
        '¹': r'$^1$',
        '²': r'$^2$',
        '³': r'$^3$',
        '⁴': r'$^4$',
        'ₓ': r'$_x$',
        'ᵧ': r'$_y$',
        '⃗': '',
        '°': r'$^\circ$',
        '±': r'$\pm$',
        '×': r'$\times$',
        '÷': r'$\div$',
        '≈': r'$\approx$',
        '≤': r'$\le$',
        '≥': r'$\ge$',
        '≠': r'$\ne$'
    }
    for k, v in unicode_math_map.items():
        text = text.replace(k, v)
        
    text = re.sub(r'(?<!\\)%', r'\\%', text)
    # Remove colons after key words
    for kw in ['ได้แก่', 'ดังนี้', 'วัตถุประสงค์', 'เนื้อหา']:
        text = text.replace(kw + ':', kw).replace(kw + '：', kw)
    return text

def extract_docx_chapters(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        
        paragraphs = []
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            p_text = ''.join([node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]).strip()
            if p_text:
                paragraphs.append(p_text)
                
    # Find all chapter headings
    ch_indices = []
    for idx, p in enumerate(paragraphs):
        if p.startswith('บทที่ '):
            ch_indices.append((idx, p))
            
    # The first 13 are the TOC. Indices 13 to 25 are the actual full content!
    content_chapters = []
    if len(ch_indices) >= 26:
        target_indices = ch_indices[13:26]
    else:
        target_indices = ch_indices[:13]
        
    for i, (start_idx, ch_title) in enumerate(target_indices):
        end_idx = target_indices[i+1][0] if i+1 < len(target_indices) else len(paragraphs)
        ch_paras = paragraphs[start_idx+1:end_idx]
        content_chapters.append((ch_title, ch_paras))
        
    return content_chapters

CHAPTER_META = [
    {
        "ch_num": 1,
        "filename": "ch01_units_measurement.tex",
        "title": "ระบบหน่วยและการวัดทางฟิสิกส์",
        "index": "ระบบหน่วยสากล SI",
        "bio_title": "การวัดและการแปลงหน่วยในงานจุลชีววิทยาและวิทยาศาสตร์สิ่งแวดล้อม",
        "bio_content": r"""ในงานจุลชีววิทยาและวิทยาศาสตร์สิ่งแวดล้อม การวัดขนาดของวัตถุที่มีขนาดเล็กมากระดับไมโครเมตร ($\mu\text{m}$) และนาโนเมตร ($\text{nm}$) มีความสำคัญยิ่ง เช่น การวัดขนาดของแบคทีเรีย \textit{Escherichia coli} ซึ่งมีความยาวเฉลี่ยประมาณ $2.0\,\mu\text{m}$ ($2.0 \times 10^{-6}\,\text{m}$) และเส้นผ่านศูนย์กลางของอนุภาคฝุ่นละออง PM2.5 ที่มีขนาดไม่เกิน $2.5\,\mu\text{m}$ นักศึกษาจำเป็นต้องมีความเชี่ยวชาญในการแปลงหน่วยตามระบบเอสไอและการระบุเลขนัยสำคัญ เพื่อให้ผลการวิเคราะห์มีความแม่นยำและน่าเชื่อถือตามเกณฑ์มาตรฐานสากล"""
    },
    {
        "ch_num": 2,
        "filename": "ch02_vectors.tex",
        "title": "เวกเตอร์ในทางฟิสิกส์และการวิเคราะห์แรง",
        "index": "เวกเตอร์และการรวมแรง",
        "bio_title": "การวิเคราะห์เวกเตอร์ของแรงและความเร็วในกระบวนการทางชีวภาพ",
        "bio_content": r"""การเคลื่อนที่ของสารละลายผ่านเยื่อหุ้มเซลล์และการเคลื่อนที่ของสิ่งมีชีวิตเซลล์เดียว เช่น \textit{Paramecium} ที่ว่ายน้ำด้วยการโบกพัดของซิเลีย (Cilia) สามารถจำลองได้ด้วยเวกเตอร์ความเร็วสองมิติและสามมิติ นอกจากนี้ แรงตึงผิวและแรงดึงดูดของของเหลวในท่อลำเลียงไซเลม (Xylem) ของพืชยังต้องวิเคราะห์ด้วยการแตกแรงเวกเตอร์ในแนวแกนดิ่งและแกนราบ เพื่ออธิบายกลไกการดูดน้ำจากรากขึ้นสู่ยอดไม้สูงกว่า 20 เมตรได้อย่างสอดคล้องกับหลักกลศาสตร์"""
    },
    {
        "ch_num": 3,
        "filename": "ch03_kinematics.tex",
        "title": "จลนศาสตร์และการเคลื่อนที่ของวัตถุ",
        "index": "จลนศาสตร์และการเคลื่อนที่",
        "bio_title": "จลนศาสตร์ของการตกตะกอนในเครื่องหมุนเหวี่ยงและอนุภาคในอากาศ",
        "bio_content": r"""ในห้องปฏิบัติการเทคโนโลยีชีวภาพ เครื่องหมุนเหวี่ยง (Centrifuge) ทำงานโดยอาศัยหลักการความเร่งสู่ศูนย์กลาง $a_c = v^2/r = \omega^2 r$ ซึ่งทำให้เกิดแรงเหวี่ยงหนีศูนย์กลางจำลองที่มีค่าสูงกว่าแรงโน้มถ่วงโลกหลายพันเท่า ($RCF \times g$) ส่งผลให้อนุภาคเซลล์ แบคทีเรีย หรือสารพันธุกรรม DNA ตกตะกอนแยกชั้นตามความหนาแน่นและมวลได้อย่างรวดเร็ว นอกจากนี้ สมการจลนศาสตร์แนวดิ่งยังใช้อธิบายอัตราการตกสัมพัทธ์ของสปอร์เชื้อราและละอองเกสรดอกไม้ในบรรยากาศ"""
    },
    {
        "ch_num": 4,
        "filename": "ch04_newton_laws.tex",
        "title": "กฎการเคลื่อนที่ของนิวตันและแรงกระทำ",
        "index": "กฎการเคลื่อนที่ของนิวตัน",
        "bio_title": "แรงหนืดของสโตกส์และกลศาสตร์การเคลื่อนที่ในของไหลชีวภาพ",
        "bio_content": r"""เมื่อจุลินทรีย์เคลื่อนที่ในน้ำหรือสารคัดหลั่ง แรงเสียดทานหลักที่กระทำต่อเซลล์คือแรงต้านความหนืดตามกฎของสโตกส์ (Stokes' Law) $F_d = 6\pi\eta r v$ เนื่องจากขนาดอนุภาคมีค่าน้อยมาก ค่าเรย์โนลด์สนัมเบอร์ (Reynolds number) ของแบคทีเรียจึงมีค่าน้อยกว่า $10^{-4}$ ซึ่งหมายความว่าแรงหนืดมีความสำคัญเหนือกว่าแรงเฉื่อยอย่างสิ้นเชิง สิ่งมีชีวิตในระดับจุลภาคจึงต้องใช้แฟลกเจลลา (Flagella) หมุนควงแบบเกลียวเพื่อขับเคลื่อนตัวเองไปข้างหน้า"""
    },
    {
        "ch_num": 5,
        "filename": "ch05_momentum_impulse.tex",
        "title": "โมเมนตัมและการดลในระบบกายภาพ",
        "index": "โมเมนตัมและการดล",
        "bio_title": "การถ่ายโอนโมเมนตัมในการแพร่ระดับโมเลกุลและความดันออสโมซิส",
        "bio_content": r"""ในระดับโมเลกุล การชนกันของโมเลกุลน้ำและสารละลายกับผนังเซลล์ทำให้เกิดการถ่ายโอนโมเมนตัม $\Delta p = F\Delta t$ ซึ่งเป็นที่มาของความดันทางจลน์ศาสตร์ (Kinetic Pressure) และแรงดันออสโมซิส (Osmotic Pressure) ตามสมการของฟานต์ฮอฟฟ์ $\Pi = iCRT$ ความเข้าใจเรื่องโมเมนตัมยังช่วยอธิบายการกระจายตัวของอนุภาคละอองลอย (Bioaerosols) เมื่อเกิดการจามหรือการไอในสภาพแวดล้อมปิด"""
    },
    {
        "ch_num": 6,
        "filename": "ch06_equilibrium.tex",
        "title": "สมดุลกลและโมเมนต์ของแรง",
        "index": "สมดุลกลและโมเมนต์",
        "bio_title": "ชีวกลศาสตร์ของระบบโครงร่างและคานงัดในสิ่งมีชีวิต",
        "bio_content": r"""โครงสร้างกระดูก ข้อต่อ และกล้ามเนื้อของมนุษย์และสัตว์ทำหน้าที่เป็นระบบคานงัดทางกลศาสตร์ (Biomechanics Levers) เช่น การยกแขนโดยอาศัยแรงดึงของกล้ามเนื้อไบเซปส์ (Biceps) ซึ่งเป็นคานประเภทที่สามที่เสียเปรียบเชิงกลแต่ได้เปรียบด้านความเร็วและระยะการเคลื่อนที่ การคำนวณจุดศูนย์ถ่วง (Center of Gravity) และโมเมนต์ของแรง $\sum \tau = 0$ ช่วยอธิบายเสถียรภาพในการทรงตัวของสัตว์และการออกแบบสรีรศาสตร์ในการทำงานเกษตรกรรมเพื่อลดการบาดเจ็บของกล้ามเนื้อ"""
    },
    {
        "ch_num": 7,
        "filename": "ch07_work_energy.tex",
        "title": "งานและพลังงานกลในระบบฟิสิกส์",
        "index": "งานและพลังงานกล",
        "bio_title": "ชีวพลังงานและกฎการอนุรักษ์พลังงานในเซลล์สิ่งมีชีวิต",
        "bio_content": r"""พลังงานในระบบชีวภาพสอดคล้องกับกฎการอนุรักษ์พลังงานอย่างเคร่งครัด โดยพลังงานแสงอาทิตย์ถูกเปลี่ยนรูปเป็นพลังงานศักย์เคมีในพันธะของน้ำตาลกลูโคสผ่านกระบวนการสังเคราะห์ด้วยแสง และถูกปลดปล่อยออกมาเป็นพลังงานกลและความร้อนในกระบวนการหายใจระดับเซลล์ (Cellular Respiration) ผ่านสารพลังงานสูง ATP การคำนวณงานทางฟิสิกส์ $W = \int \vec{F} \cdot d\vec{r}$ ยังใช้อธิบายงานในการสูบฉีดเลือดของหัวใจและการลำเลียงน้ำตาลในท่อโฟลเอ็ม (Phloem)"""
    },
    {
        "ch_num": 8,
        "filename": "ch08_power_simple_machines.tex",
        "title": "กำลังและเครื่องกลอย่างง่าย",
        "index": "กำลังและเครื่องกล",
        "bio_title": "กำลังชีวภาพและประสิทธิภาพเชิงกลของเครื่องจักรกลการเกษตร",
        "bio_content": r"""อัตราการทำงานต่อหนึ่งหน่วยเวลาหรือกำลัง $P = W/t$ ในระบบชีวภาพเกี่ยวข้องโดยตรงกับอัตราเมแทบอลิซึมพื้นฐาน (Basal Metabolic Rate: BMR) ในขณะที่งานด้านเกษตรกรรมและวิทยาศาสตร์สิ่งแวดล้อม เครื่องกลอย่างง่าย เช่น รอก พื้นเอียง สกรูลำเลียงเมล็ดพันธุ์ และระบบปั๊มน้ำพลังงานแสงอาทิตย์ ล้วนได้รับการออกแบบโดยคำนึงถึงการได้เปรียบเชิงกลจริง (AMA) และประสิทธิภาพเชิงกล ($e = W_{\text{out}}/W_{\text{in}} \times 100\%$) เพื่อประหยัดพลังงานต้นทุน"""
    },
    {
        "ch_num": 9,
        "filename": "ch09_heat_transfer.tex",
        "title": "ปรากฏการณ์ความร้อนและการถ่ายโอนความร้อน",
        "index": "การถ่ายโอนความร้อน",
        "bio_title": "การควบคุมอุณหภูมิในสิ่งมีชีวิตและการฆ่าเชื้อด้วยความร้อน",
        "bio_content": r"""การถ่ายโอนความร้อนทั้ง 3 รูปแบบ ได้แก่ การนำความร้อน (Conduction) การพาความร้อน (Convection) และการแผ่รังสีความร้อน (Radiation) มีบทบาทสำคัญต่อสรีรวิทยาของสิ่งมีชีวิตในการรักษาอุณหภูมิร่างกายให้อยู่ในภาวะสมดุล (Thermoregulation) นอกจากนี้ ในทางจุลชีววิทยา หลักการความร้อนแฝงของการกลายเป็นไอ (Latent Heat of Vaporization) ถูกนำมาใช้ในหม้อนึ่งความดันไอ (Autoclave) ที่อุณหภูมิ $121^\circ\text{C}$ ความดัน 15 psi เพื่อทำลายสปอร์ของแบคทีเรียได้อย่างสมบูรณ์"""
    },
    {
        "ch_num": 10,
        "filename": "ch10_thermodynamics_gases.tex",
        "title": "อุณหพลศาสตร์และทฤษฎีจลน์ของก๊าซ",
        "index": "อุณหพลศาสตร์และก๊าซ",
        "bio_title": "เอนโทรปี ชีวฟิสิกส์ของเยื่อหุ้มเซลล์ และการแลกเปลี่ยนก๊าซ",
        "bio_content": r"""กฎข้อที่หนึ่งของอุณหพลศาสตร์ $\Delta U = Q - W$ อธิบายงบประมาณพลังงานในสิ่งมีชีวิต ขณะที่กฎข้อที่สองว่าด้วยเอนโทรปี ($\Delta S \ge 0$) อธิบายว่าสิ่งมีชีวิตต้องบริโภคพลังงานอิสระ (Gibbs Free Energy, $\Delta G = \Delta H - T\Delta S$) เพื่อรักษาสภาพระเบียบของระบบเซลล์มิให้พังทลายลง นอกจากนี้ กฎของก๊าซในอุดมคติ $PV = nRT$ และกฎของดอลตันเรื่องความดันย่อย ใช้อธิบายกลไกการแพร่ของก๊าซออกซิเจนและคาร์บอนไดออกไซด์ผ่านถุงลมปอดและปากใบของพืช"""
    },
    {
        "ch_num": 11,
        "filename": "ch11_electrostatics.tex",
        "title": "ไฟฟ้าสถิต สนามไฟฟ้า และศักย์ไฟฟ้า",
        "index": "ไฟฟ้าสถิตและสนามไฟฟ้า",
        "bio_title": "ชีวฟิสิกส์ของศักย์เยื่อหุ้มเซลล์และสมการเนิร์นสต์",
        "bio_content": r"""เยื่อหุ้มเซลล์ของสิ่งมีชีวิตทำหน้าที่เป็นตัวเก็บประจุชีวภาพ (Biological Capacitor) โดยมีสารฟอสโฟลิพิดสองชั้นคั่นระหว่างไอออนบวกและไอออนลบภายในและภายนอกเซลล์ ทำให้เกิดความต่างศักย์เยื่อเซลล์ขณะพัก (Resting Membrane Potential) ประมาณ $-70\,\text{mV}$ ซึ่งสามารถคำนวณได้อย่างแม่นยำด้วยสมการเนิร์นสต์ (Nernst Equation) $V = \frac{RT}{zF} \ln\frac{[C_{\text{out}}]}{[C_{\text{in}}]}$ ความรู้นี้เป็นรากฐานของสรีรวิทยาระบบประสาทและกล้ามเนื้อ"""
    },
    {
        "ch_num": 12,
        "filename": "ch12_current_electricity.tex",
        "title": "ไฟฟ้ากระแสตรงและวงจรไฟฟ้า",
        "index": "ไฟฟ้ากระแสตรงและวงจร",
        "bio_title": "การนำสัญญาณประสาทและเครื่องมือวัดทางชีวการแพทย์",
        "bio_content": r"""การส่งสัญญาณประสาท (Action Potential) ไปตามแอกซอนของเซลล์ประสาทสามารถวิเคราะห์ได้ด้วยแบบจำลองวงจรไฟฟ้า RC ขนานตามทฤษฎีสายเคเบิล (Cable Theory) นอกจากนี้ หลักการของสะพานวีตสโตน (Wheatstone Bridge) และกฎของโอห์ม $V = IR$ ยังเป็นหัวใจสำคัญของการทำงานของหัววัดความชื้นในดิน หัววัดสภาพนำไฟฟ้าของน้ำ (EC Meter) และเครื่องตรวจคลื่นไฟฟ้าหัวใจ (ECG) ในงานวิทยาศาสตร์ชีวภาพ"""
    },
    {
        "ch_num": 13,
        "filename": "ch13_optics_radioactivity.tex",
        "title": "ทัศนศาสตร์ กัมมันตภาพรังสี และการประยุกต์",
        "index": "ทัศนศาสตร์และกัมมันตรังสี",
        "bio_title": "ทัศนศาสตร์ของกล้องจุลทรรศน์และการใช้รังสีในงานชีววิทยา",
        "bio_content": r"""กล้องจุลทรรศน์แบบใช้แสง (Compound Light Microscope) อาศัยการหักเหของแสงผ่านเลนส์ใกล้วัตถุและเลนส์ใกล้ตาเพื่อให้ได้กำลังขยายรวม $M = M_o \times M_e$ ขีดจำกัดในการแยกชัดของกล้อง (Limit of Resolution) ถูกกำหนดโดยเกณฑ์ของเรย์ลีห์ $d = \frac{0.61\lambda}{NA}$ ในขณะที่ปรากฏการณ์กัมมันตภาพรังสี เช่น รังสีแกมมา ถูกนำมาใช้ในการกำจัดเชื้อจุลินทรีย์ในเวชภัณฑ์และผลผลิตทางการเกษตร รวมถึงการใช้ไอโซโทปรังสีคาร์บอน-14 ในการหาอายุซากดึกดำบรรพ์และติดตามเส้นทางเมแทบอลิซึม"""
    }
]

def generate_chapters(docx_chapters):
    for meta in CHAPTER_META:
        ch_idx = meta["ch_num"] - 1
        raw_title, paras = docx_chapters[ch_idx] if ch_idx < len(docx_chapters) else ("บทที่ " + str(meta["ch_num"]), [])
        
        filepath = os.path.join(CHAPTERS_DIR, meta["filename"])
        print(f"Generating Book 11 Chapter {meta['ch_num']:02d}: {filepath}")
        
        # Structure paragraphs
        objectives = []
        body_paras = []
        worked_examples = []
        review_questions = []
        references = []
        
        mode = "body"
        for p in paras:
            p_strip = p.strip()
            if "วัตถุประสงค์การเรียนรู้" in p_strip:
                mode = "objectives"
                continue
            elif "ตัวอย่างที่" in p_strip or "ตัวอย่างโจทย์" in p_strip:
                mode = "example"
                worked_examples.append([p_strip])
                continue
            elif "แบบฝึกหัดท้ายบท" in p_strip or "คำถามท้ายบท" in p_strip:
                mode = "review"
                continue
            elif "เอกสารอ้างอิง" in p_strip or "บรรณานุกรมประจำบท" in p_strip:
                mode = "references"
                continue
                
            if mode == "objectives":
                objectives.append(p_strip)
            elif mode == "example":
                if worked_examples:
                    worked_examples[-1].append(p_strip)
                else:
                    body_paras.append(p_strip)
            elif mode == "review":
                review_questions.append(p_strip)
            elif mode == "references":
                references.append(p_strip)
            else:
                body_paras.append(p_strip)
                
        with open(filepath, "w", encoding="utf-8") as f:
            clean_ch_title = clean_heading_text(meta["title"])
            f.write(f"\\chapter{{{clean_ch_title}}}\n")
            f.write(f"\\label{{ch:{meta['filename'].replace('.tex', '')}}}\n")
            f.write(f"\\index{{{meta['index']}}}\n\n")
            
            # Objectives Box
            f.write("\\begin{conceptbox}[title=วัตถุประสงค์การเรียนรู้ประจำบท]\n")
            f.write("เมื่อสิ้นสุดการศึกษาบทเรียนนี้ นักศึกษาสามารถ\n")
            f.write("\\begin{enumerate}\n")
            if objectives:
                for obj in objectives[:5]:
                    f.write(f"    \\item {clean_latex(obj)}\n")
            else:
                f.write(f"    \\item เข้าใจและอธิบายหลักการพื้นฐานของ{clean_ch_title}ได้อย่างถูกต้องตามหลักฟิสิกส์\n")
                f.write(f"    \\item ประยุกต์ใช้สมการและความสัมพันธ์ทางคณิตศาสตร์ในการแก้โจทย์ปัญหาได้อย่างเป็นระบบ\n")
                f.write(f"    \\item เชื่อมโยงหลักการทางฟิสิกส์เข้ากับปรากฏการณ์ในสิ่งมีชีวิตและงานวิทยาศาสตร์สิ่งแวดล้อม\n")
            f.write("\\end{enumerate}\n")
            f.write("\\end{conceptbox}\n\n")
            
            # Theoretical Body Paragraphs
            f.write("\\section{ทฤษฎีและหลักการพื้นฐาน}\n\n")
            
            para_count = 0
            for p in body_paras[:12]:
                if len(p) > 20:
                    f.write(f"{clean_latex(p)}\n\n")
                    para_count += 1
                    if para_count == 4:
                        f.write(f"\\section{{การวิเคราะห์เชิงกลศาสตร์และสมการสำคัญ}}\n\n")
                    elif para_count == 8:
                        f.write(f"\\section{{การทดลองและการสังเกตการณ์ในห้องปฏิบัติการ}}\n\n")
            
            # Life Sciences & Environmental Application Box
            f.write("\\begin{bioappbox}\n")
            f.write(f"\\textbf{{{meta['bio_title']}}}\n\n")
            f.write(f"{meta['bio_content']}\n")
            f.write("\\end{bioappbox}\n\n")
            
            # Precision Lab Skills Box
            f.write("\\begin{labbox}\n")
            f.write("1. ตรวจสอบตำแหน่งศูนย์ (Zero Error) ของเครื่องมือวัดทุกชนิดก่อนเริ่มบันทึกข้อมูล\n")
            f.write("2. ทำการวัดซ้ำอย่างน้อย 3 ถึง 5 ครั้งในแต่ละจุดทดลองเพื่อคำนวณหาค่าเฉลี่ยและค่าเบี่ยงเบนมาตรฐาน\n")
            f.write("3. บันทึกผลการวัดพร้อมระบุหน่วยเอสไอ (SI Units) และค่าความคลาดเคลื่อนของการวัดเสมอ\n")
            f.write("\\end{labbox}\n\n")
            
            # Worked Example
            f.write("\\section{ตัวอย่างโจทย์และการวิเคราะห์เชิงฟิสิกส์}\n\n")
            f.write("\\begin{examplebox}\n")
            if worked_examples and len(worked_examples[0]) >= 2:
                ex_text = "\n\n".join([clean_latex(line) for line in worked_examples[0][:4]])
                f.write(f"{ex_text}\n")
            else:
                f.write(f"\\textbf{{โจทย์ตัวอย่าง:}} จงคำนวณปริมาณทางฟิสิกส์ที่เกี่ยวข้องกับ{clean_ch_title} โดยกำหนดข้อมูลตัวแปรตามเงื่อนไขมาตรฐาน\n\n")
                f.write("\\textbf{วิธีทำ:}\n")
                f.write("1. ระบุตัวแปรที่โจทย์กำหนดและแปลงให้อยู่ในระบบหน่วยเอสไอ (SI Units)\n")
                f.write("2. เลือกใช้สมการทางฟิสิกส์ที่สัมพันธ์กับตัวแปรที่ทราบค่าและตัวแปรที่ต้องการหา\n")
                f.write("3. แทนค่าตัวแปรลงในสมการและคำนวณผลลัพธ์พร้อมตรวจสอบเลขนัยสำคัญ\n")
            f.write("\\end{examplebox}\n\n")
            
            # Review Questions
            f.write("\\section{แบบฝึกหัดทบทวนและคำถามท้ายบท}\n\n")
            f.write("\\begin{enumerate}\n")
            if review_questions:
                for q in review_questions[:6]:
                    f.write(f"    \\item {clean_latex(q)}\n")
            else:
                f.write(f"    \\item จงอธิบายความหมายและนิยามสำคัญของ{clean_ch_title} พร้อมยกตัวอย่างประกอบ\n")
                f.write("    \\item จงเปรียบเทียบความแตกต่างระหว่างปริมาณสเกลาร์และปริมาณเวกเตอร์ในหัวข้อนี้\n")
                f.write("    \\item จงแสดงการพิสูจน์สมการฟิสิกส์ที่สำคัญประจำบทเรียนนี้อย่างละเอียดเป็นขั้นตอน\n")
                f.write("    \\item ยกตัวอย่างปรากฏการณ์ในสิ่งมีชีวิตที่สามารถอธิบายได้ด้วยกฎทางฟิสิกส์ในบทนี้ 2 ตัวอย่าง\n")
                f.write("    \\item หากทำการทดลองแล้วพบว่าผลคลาดเคลื่อนจากทฤษฎี 15\\% จงวิเคราะห์สาเหตุที่เป็นไปได้\n")
            f.write("\\end{enumerate}\n\n")
            
            # End of chapter
            f.write("% สิ้นสุดบทเรียน\n")

def generate_backmatter():
    # Appendix A: Laboratory Manual
    appA_path = os.path.join(BACKMATTER_DIR, "appendixA.tex")
    print(f"Generating Appendix A: {appA_path}")
    with open(appA_path, "w", encoding="utf-8") as f:
        f.write(r"""\chapter{คู่มือปฏิบัติการวัดละเอียดทางฟิสิกส์}
\label{app:lab_manual}
\index{คู่มือปฏิบัติการวัดละเอียด}

คู่มือปฏิบัติการฉบับนี้จัดทำขึ้นเพื่อฝึกทักษะการใช้เครื่องมือวัดละเอียดพื้นฐานสำหรับนักศึกษาสาขาวิทยาศาสตร์ชีวภาพ จุลชีววิทยา และสิ่งแวดล้อม ประกอบด้วยเวอร์เนียร์คาลิปเปอร์ ไมโครมิเตอร์ และสเฟียโรมิเตอร์

\section{ปฏิบัติการที่ 1: การวัดขนาดวัตถุอย่างละเอียด}

\subsection{วัตถุประสงค์การทดลอง}
\begin{enumerate}
    \item เพื่อศึกษาและฝึกทักษะการวัดขนาดวัตถุด้วยเวอร์เนียร์คาลิปเปอร์ (Vernier Caliper) และไมโครมิเตอร์ (Micrometer)
    \item เพื่อศึกษาการใช้สเฟียโรมิเตอร์ (Spherometer) ในการวัดรัศมีความโค้งของเลนส์และผิวโค้งทรงกลม
    \item เพื่อฝึกการวิเคราะห์และรายงานค่าความคลาดเคลื่อนตามหลักเลขนัยสำคัญ
\end{enumerate}

\subsection{ทฤษฎีและหลักการของเครื่องมือวัด}
\begin{enumerate}
    \item \textbf{เวอร์เนียร์คาลิปเปอร์:} เครื่องมือวัดความยาว ความหนา เส้นผ่านศูนย์กลางภายใน ภายนอก และความลึก มีความละเอียดของสเกลเวอร์เนียร์ (Least Count) คำนวณจาก:
    \begin{equation}
        LC = \frac{\text{ความยาว 1 ช่องสเกลหลัก}}{\text{จำนวนช่องสเกลเวอร์เนียร์}} = \frac{1\,\text{mm}}{20} = 0.05\,\text{mm}
    \end{equation}
    
    \item \textbf{ไมโครมิเตอร์:} เครื่องมือวัดละเอียดที่อาศัยหลักการเกลียวละเอียด (Screw Pitch) หนึ่งรอบการหมุนเลื่อนแกนวัดได้ $0.5\,\text{mm}$ ปลอกหมุนแบ่งเป็น 50 ช่องสเกล ความละเอียดต่ำสุดคือ:
    \begin{equation}
        LC = \frac{0.5\,\text{mm}}{50} = 0.01\,\text{mm} = 10\,\mu\text{m}
    \end{equation}
\end{enumerate}

\begin{table}[H]
\centering
\small
\begin{tabularx}{\textwidth}{l c c c Y}
\toprule
\textbf{เครื่องมือวัด} & \textbf{สเกลหลัก} & \textbf{สเกลละเอียด} & \textbf{Least Count} & \textbf{การนำไปใช้ในงานชีวภาพ} \\
\midrule
ไม้บรรทัดเหล็ก & 1 mm & - & 0.5 mm & วัดความยาวตัวอย่างราก/ลำต้น \\
เวอร์เนียร์คาลิปเปอร์ & 1 mm & 20 หรือ 50 ช่อง & 0.05 หรือ 0.02 mm & วัดขนาดเส้นผ่านศูนย์กลางผล/หลอดทดลอง \\
ไมโครมิเตอร์ & 0.5 mm & 50 ช่อง & 0.01 mm & วัดความหนาของแผ่นสไลด์/ใบพืช \\
สเฟียโรมิเตอร์ & 1 mm & 100 ช่อง & 0.005 mm & วัดรัศมีความโค้งผิวเลนส์กล้องจุลทรรศน์ \\
\bottomrule
\end{tabularx}
\caption{คุณลักษณะและความละเอียดของเครื่องมือวัดละเอียดในห้องปฏิบัติการ}
\end{table}

\subsection{ตารางบันทึกผลการทดลอง}

\begin{table}[H]
\centering
\small
\begin{tabularx}{\textwidth}{c Y c c c}
\toprule
\textbf{ครั้งที่} & \textbf{ชิ้นงานตัวอย่าง} & \textbf{ค่าที่วัด (mm)} & \textbf{$\bar{x}$ (mm)} & \textbf{$S_D$ (mm)} \\
\midrule
1 & ความหนากระจกสไลด์ (ไมโครมิเตอร์) & 1.22 & \multirow{3}{*}{1.223} & \multirow{3}{*}{$\pm 0.006$} \\
2 & ความหนากระจกสไลด์ (ไมโครมิเตอร์) & 1.23 & & \\
3 & ความหนากระจกสไลด์ (ไมโครมิเตอร์) & 1.22 & & \\
\midrule
1 & เส้นผ่านศูนย์กลางหลอดทดลอง (เวอร์เนียร์) & 15.45 & \multirow{3}{*}{15.47} & \multirow{3}{*}{$\pm 0.020$} \\
2 & เส้นผ่านศูนย์กลางหลอดทดลอง (เวอร์เนียร์) & 15.50 & & \\
3 & เส้นผ่านศูนย์กลางหลอดทดลอง (เวอร์เนียร์) & 15.45 & & \\
\bottomrule
\end{tabularx}
\caption{ตัวอย่างตารางบันทึกผลการวัดละเอียดและการคำนวณค่าทางสถิติ}
\end{table}
""")

    # Appendix B: Life Sciences Problem Sets
    appB_path = os.path.join(BACKMATTER_DIR, "appendixB.tex")
    print(f"Generating Appendix B: {appB_path}")
    with open(appB_path, "w", encoding="utf-8") as f:
        f.write(r"""\chapter{ชุดโจทย์และข้อสอบประยุกต์ฟิสิกส์สำหรับวิทยาศาสตร์ชีวภาพ}
\label{app:bio_problems}
\index{ชุดโจทย์ประยุกต์ชีวภาพ}

\section{ชุดโจทย์คัดสรรข้อสอบกลางภาคและปลายภาค}

\begin{enumerate}
    \item \textbf{กลศาสตร์ของไหลและการดูดซึม:} ท่อลำเลียงไซเลมของต้นยางพารามีรัศมีเฉลี่ย $r = 25\,\mu\text{m}$ หากน้ำยางมีแรงตึงผิว $\gamma = 0.072\,\text{N/m}$ และมุมสัมผัส $\theta = 0^\circ$ จงคำนวณหาความสูงสูงสุดที่ของเหลวสามารถขึ้นไปได้ด้วยปรากฏการณ์คาพิลลารี (Capillary Action) กำหนดความหนาแน่น $\rho = 1,000\,\text{kg/m}^3$ และ $g = 9.8\,\text{m/s}^2$
    
    \item \textbf{เครื่องหมุนเหวี่ยงแยกตะกอน:} เครื่อง Centrifuge หมุนด้วยความถี่ $6,000\,\text{rpm}$ รัศมีการหมุนของหลอดทดลอง $r = 12\,\text{cm}$ จงคำนวณหาความเร่งสู่ศูนย์กลางในหน่วยเท่าของแรงโน้มถ่วงโลก ($RCF \times g$)
    
    \item \textbf{ไฟฟ้าชีวภาพ:} เยื่อหุ้มเซลล์ประสาทมีความหนา $d = 8.0\,\text{nm}$ มีความต่างศักย์ขณะพัก $V = -70\,\text{mV}$ จงคำนวณขนาดของสนามไฟฟ้าที่ตั้งฉากกับเยื่อหุ้มเซลล์ในหน่วยโวลต์ต่อเมตร ($\text{V/m}$) พร้อมอธิบายว่าสนามไฟฟ้านี้ส่งผลต่อการเคลื่อนที่ของไอโซเลท $\text{Na}^+$ และ $\text{K}^+$ อย่างไร
    
    \item \textbf{อุณหพลศาสตร์และการสังเคราะห์แสง:} ใบพืชได้รับพลังงานแสงอาทิตย์เฉลี่ย $800\,\text{W/m}^2$ หากใบพืชมีพื้นที่ผิวรวม $0.05\,\text{m}^2$ และมีประสิทธิภาพในการเปลี่ยนพลังงานแสงเป็นพลังงานเคมี $3.5\%$ จงคำนวณพลังงานเคมีที่สังเคราะห์ได้ในเวลา 1 ชั่วโมง
    
    \item \textbf{ทัศนศาสตร์กล้องจุลทรรศน์:} เลนส์ใกล้วัตถุของกล้องจุลทรรศน์มีค่า Numerical Aperture ($NA = 1.25$) เมื่อใช้แสงสีน้ำเงินความยาวคลื่น $\lambda = 450\,\text{nm}$ จงคำนวณขีดจำกัดในการแยกชัดของกล้อง (Resolving Limit) ตามเกณฑ์ของเรย์ลีห์
\end{enumerate}
""")

    # References
    ref_path = os.path.join(BACKMATTER_DIR, "references.tex")
    print(f"Generating References: {ref_path}")
    with open(ref_path, "w", encoding="utf-8") as f:
        f.write(r"""\chapter*{บรรณานุกรม}
\addcontentsline{toc}{chapter}{บรรณานุกรม}

\begin{enumerate}
    \item ชีวะ ทัศนา. (2566). \textit{เอกสารประกอบการสอน วิชาฟิสิกส์ 1 ปฏิบัติการ วัดละเอียด}. สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี.
    \item ชีวะ ทัศนา. (2566). \textit{คู่มือปฏิบัติการฟิสิกส์พื้นฐาน 1 และ 2 สำหรับนักศึกษาสาขาวิทยาศาสตร์}. จันทบุรี: มหาวิทยาลัยราชภัฏรำไพพรรณี.
    \item สถาบันส่งเสริมการสอนวิทยาศาสตร์และเทคโนโลยี (สสวท.). (2562). \textit{หนังสือเรียนรายวิชาเพิ่มเติมวิทยาศาสตร์และเทคโนโลยี ฟิสิกส์ เล่ม 1-6}. กรุงเทพฯ: โรงพิมพ์แห่งจุฬาลงกรณ์มหาวิทยาลัย.
    \item Halliday, D., Resnick, R., \& Walker, J. (2018). \textit{Fundamentals of Physics} (11th ed.). Hoboken, NJ: John Wiley \& Sons.
    \item Serway, R. A., \& Jewett, J. W. (2018). \textit{Physics for Scientists and Engineers with Modern Physics} (10th ed.). Boston, MA: Cengage Learning.
    \item Tipler, P. A., \& Mosca, G. (2008). \textit{Physics for Scientists and Engineers} (6th ed.). New York: W. H. Freeman and Company.
    \item Giancoli, D. C. (2014). \textit{Physics: Principles with Applications} (7th ed.). Boston: Pearson.
    \item Nelson, P. (2014). \textit{Biological Physics: Energy, Information, Life}. New York: W. H. Freeman.
    \item Cotterill, R. (2002). \textit{Biophysics: An Introduction}. Chichester: John Wiley \& Sons.
    \item Herman, I. P. (2016). \textit{Physics of the Human Body} (2nd ed.). Cham: Springer International Publishing.
\end{enumerate}
""")

    # Biography
    bio_path = os.path.join(BACKMATTER_DIR, "biography.tex")
    print(f"Generating Biography: {bio_path}")
    with open(bio_path, "w", encoding="utf-8") as f:
        f.write(r"""\chapter*{ประวัติผู้เขียน}
\addcontentsline{toc}{chapter}{ประวัติผู้เขียน}

\begin{center}
    \begin{tcolorbox}[
        enhanced,
        colback=softSmoke,
        colframe=physRoyalBlue,
        arc=4mm,
        boxrule=1.2pt,
        width=\textwidth,
        drop shadow={black!15}
    ]
        \vspace{6pt}
        \textbf{\Large ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา}\\[6pt]
        {\large สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี}\\[8pt]
        
        \textbf{คุณวุฒิการศึกษา}
        \begin{itemize}
            \item ปร.ด. (ฟิสิกส์ประยุกต์) มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี
            \item วท.ม. (ฟิสิกส์ประยุกต์) สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
            \item วท.บ. (ฟิสิกส์) มหาวิทยาลัยศรีนครินทรวิโรฒ
        \end{itemize}
        
        \textbf{ความเชี่ยวชาญทางวิชาการและการสอน}
        \begin{itemize}
            \item การสอนวิชาฟิสิกส์พื้นฐานและฟิสิกส์ประยุกต์สำหรับนักศึกษาสาขาวิทยาศาสตร์
            \item การพัฒนาเครื่องมือวัดละเอียดและระบบห้องปฏิบัติการฟิสิกส์อัจฉริยะ (Physics Smart Lab)
            \item ฟิสิกส์เชิงอนุภาค การตรวจวัดอนุภาคละอองลอย PM2.5 และการวิเคราะห์ภาพถ่ายดิจิทัล
            \item การแปรรูปพลังงานชีวมวลและวัสดุคาร์บอนขั้นสูงเพื่อสิ่งแวดล้อม
        \end{itemize}
        \vspace{6pt}
    \end{tcolorbox}
\end{center}
""")

if __name__ == "__main__":
    print("Starting generation of Book 11...")
    docx_chapters = extract_docx_chapters(DOCX_MAIN)
    print(f"Extracted {len(docx_chapters)} chapters from docx.")
    generate_chapters(docx_chapters)
    generate_backmatter()
    print("ALL DONE FOR 11_General_Physics_LifeSciences!")
