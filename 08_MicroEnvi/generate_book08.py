#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for 08_MicroEnvi - Environmental Microbiology and Water Quality Analysis
Compliant with RBRU Academic Textbook Masterclass Standards.
"""

import os
import re
import glob

base_dir = "/Applications/XAMPP/xamppfiles/htdocs/04_Education_Exam/Latex2026/08_MicroEnvi"
source_dir = os.path.join(base_dir, "source_docs", "Micro_Lab")
chapters_dir = os.path.join(base_dir, "chapters")
backmatter_dir = os.path.join(base_dir, "backmatter")
images_dir = os.path.join(base_dir, "images")

available_images = set(os.listdir(images_dir)) if os.path.exists(images_dir) else set()

chapter_meta = [
    (1, "ch01_lab_safety_basics.tex", "ความปลอดภัยและเทคนิคพื้นฐานในปฏิบัติการจุลชีววิทยา", "chap:ch01"),
    (2, "ch02_microbial_dispersion.tex", "การแพร่กระจายของจุลินทรีย์ในสิ่งแวดล้อมและอากาศ", "chap:ch02"),
    (3, "ch03_environmental_survey.tex", "การสำรวจจุลินทรีย์ในแหล่งน้ำธรรมชาติและดิน", "chap:ch03"),
    (4, "ch04_microbial_staining.tex", "กล้องจุลทรรศน์และเทคนิคการย้อมสีจุลินทรีย์", "chap:ch04"),
    (5, "ch05_microbial_morphology.tex", "สัณฐานวิทยาและโครงสร้างพิเศษของเซลล์จุลินทรีย์", "chap:ch05"),
    (6, "ch06_isolation_cultivation.tex", "การแยกเชื้อบริสุทธิ์และการเพาะเลี้ยงจุลินทรีย์", "chap:ch06"),
    (7, "ch07_culture_media.tex", "การเตรียมอาหารเลี้ยงเชื้อจุลินทรีย์และการควบคุมคุณภาพ", "chap:ch07"),
    (8, "ch08_microbial_growth.tex", "การเจริญและจลนพลศาสตร์การเพิ่มจำนวนของแบคทีเรีย", "chap:ch08"),
    (9, "ch09_anaerobic_microbiology.tex", "จุลชีววิทยาแบบไม่ใช้ออกซิเจนและการเพาะเลี้ยง", "chap:ch09"),
    (10, "ch10_metabolism_biochemical.tex", "สรีรวิทยา เมแทบอลิซึม และการทดสอบทางชีวเคมี", "chap:ch10"),
    (11, "ch11_microbial_control.tex", "การควบคุมจุลินทรีย์ด้วยวิธีทางกายภาพ สารเคมี และยาต้านจุลชีพ", "chap:ch11"),
    (12, "ch12_water_bioremediation_bioblock.tex", "อาณาจักรฟังไจและการประยุกต์บำบัดน้ำเสียด้วยนวัตกรรมชีวภาพ", "chap:ch12"),
]

def sanitize_thai_text(text):
    # Escape characters
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    # Symbols
    text = text.replace('°C', '$^{\\circ}$C')
    text = text.replace('°', '$^{\\circ}$')
    text = text.replace('→', '$\\rightarrow$')
    text = text.replace('←', '$\\leftarrow$')
    text = text.replace('±', '$\\pm$')
    text = text.replace('μ', '$\\mu$')
    text = text.replace('µ', '$\\mu$')
    text = text.replace('×', '$\\times$')
    text = text.replace('≤', '$\\le$')
    text = text.replace('≥', '$\\ge$')
    text = text.replace('~', '$\\sim$')
    # Remove colons from specific Thai academic phrases
    text = re.sub(r'ได้แก่\s*[:：]', 'ได้แก่ ', text)
    text = re.sub(r'ดังนี้\s*[:：]', 'ดังนี้ ', text)
    text = re.sub(r'วัตถุประสงค์\s*[:：]', 'วัตถุประสงค์ ', text)
    text = re.sub(r'เนื้อหา\s*[:：]', 'เนื้อหา ', text)
    text = re.sub(r'ขั้นตอน\s*[:：]', 'ขั้นตอน ', text)
    return text

def parse_markdown_table(lines):
    # Parse simple markdown table to tabularx
    rows = []
    for line in lines:
        if re.match(r'^\s*\|?\s*:?-+:?\s*\|', line):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if cells and any(cells):
            rows.append(cells)
    if not rows:
        return ""
    num_cols = max(len(r) for r in rows)
    # Normalise row lengths
    for r in rows:
        while len(r) < num_cols:
            r.append("")
    
    col_def = "X" * num_cols
    # First column can be Y (left-aligned), others Z or Y
    if num_cols == 2:
        col_def = "p{0.4\\textwidth} X"
    elif num_cols == 3:
        col_def = "p{0.3\\textwidth} X p{0.2\\textwidth}"
    elif num_cols == 4:
        col_def = "p{0.25\\textwidth} X X p{0.2\\textwidth}"
    else:
        col_def = " ".join(["Y"] * num_cols)

    latex_table = ["\\begin{table}[H]", "\\centering", "\\small",
                   f"\\begin{{tabularx}}{{\\textwidth}}{{{col_def}}}",
                   "\\toprule"]
    # Header
    latex_table.append(" & ".join([f"\\textbf{{{clean_heading(c)}}}" for c in rows[0]]) + " \\\\")
    latex_table.append("\\midrule")
    # Body
    for r in rows[1:]:
        latex_table.append(" & ".join([sanitize_thai_text(c) for c in r]) + " \\\\")
    latex_table.append("\\bottomrule")
    latex_table.append("\\end{tabularx}")
    latex_table.append("\\end{table}")
    return "\n".join(latex_table)

def clean_heading(h):
    h = h.replace(':', '').replace('：', '').strip()
    h = re.sub(r'^[0-9]+(\.[0-9]+)*\s*', '', h)
    # Extract English in parenthesis
    h = re.sub(r'\(([^)]*[a-zA-Z]+[^)]*)\)', '', h).strip()
    return sanitize_thai_text(h)

print("Generator script setup complete.")
