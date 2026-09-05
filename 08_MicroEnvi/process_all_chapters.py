#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process and generate all 12 chapters for 08_MicroEnvi.
"""

import os
import re
import glob

base_dir = "/Applications/XAMPP/xamppfiles/htdocs/04_Education_Exam/Latex2026/08_MicroEnvi"
source_dir = os.path.join(base_dir, "source_docs", "Micro_Lab")
chapters_dir = os.path.join(base_dir, "chapters")
images_dir = os.path.join(base_dir, "images")

available_images = set(os.listdir(images_dir)) if os.path.exists(images_dir) else set()

chapters_info = [
    {
        "num": 1,
        "filename": "ch01_lab_safety_basics.tex",
        "title": "ความปลอดภัยและเทคนิคพื้นฐานในปฏิบัติการจุลชีววิทยา",
        "label": "chap:ch01",
        "folder": "chapter1",
        "main_md": "chapter01_intro_to_lab_micro.md",
        "ebook_md": "chapter01_ebook.md",
        "syllabus_md": "chapter01_syllabus.md"
    },
    {
        "num": 2,
        "filename": "ch02_microbial_dispersion.tex",
        "title": "การแพร่กระจายของจุลินทรีย์ในสิ่งแวดล้อมและอากาศ",
        "label": "chap:ch02",
        "folder": "chapter2",
        "main_md": "chapter02_microbial_dispersion.md",
        "ebook_md": "chapter02_ebook.md",
        "syllabus_md": "chapter02_syllabus.md"
    },
    {
        "num": 3,
        "filename": "ch03_environmental_survey.tex",
        "title": "การสำรวจจุลินทรีย์ในแหล่งน้ำธรรมชาติและดิน",
        "label": "chap:ch03",
        "folder": "chapter3",
        "main_md": "chapter03_microbial_survey.md",
        "ebook_md": "chapter03_ebook.md",
        "syllabus_md": "chapter03_syllabus.md"
    },
    {
        "num": 4,
        "filename": "ch04_microbial_staining.tex",
        "title": "กล้องจุลทรรศน์และเทคนิคการย้อมสีจุลินทรีย์",
        "label": "chap:ch04",
        "folder": "chapter4",
        "main_md": "chapter04_microbial_staining.md",
        "ebook_md": "chapter04_ebook.md",
        "syllabus_md": "chapter04_syllabus.md"
    },
    {
        "num": 5,
        "filename": "ch05_microbial_morphology.tex",
        "title": "สัณฐานวิทยาและโครงสร้างพิเศษของเซลล์จุลินทรีย์",
        "label": "chap:ch05",
        "folder": "chapter5",
        "main_md": "chapter05_microbial_structure.md",
        "ebook_md": "chapter05_ebook.md",
        "syllabus_md": "chapter05_syllabus.md"
    },
    {
        "num": 6,
        "filename": "ch06_isolation_cultivation.tex",
        "title": "การแยกเชื้อบริสุทธิ์และการเพาะเลี้ยงจุลินทรีย์",
        "label": "chap:ch06",
        "folder": "chapter6",
        "main_md": "chapter06_microbial_isolation.md",
        "ebook_md": "chapter06_ebook.md",
        "syllabus_md": "chapter06_syllabus.md"
    },
    {
        "num": 7,
        "filename": "ch07_culture_media.tex",
        "title": "การเตรียมอาหารเลี้ยงเชื้อจุลินทรีย์และการควบคุมคุณภาพ",
        "label": "chap:ch07",
        "folder": "chapter7",
        "main_md": "chapter07_culture_media.md",
        "ebook_md": "chapter07_ebook.md",
        "syllabus_md": "chapter07_syllabus.md"
    },
    {
        "num": 8,
        "filename": "ch08_microbial_growth.tex",
        "title": "การเจริญและจลนพลศาสตร์การเพิ่มจำนวนของแบคทีเรีย",
        "label": "chap:ch08",
        "folder": "chapter8",
        "main_md": "chapter08_microbial_growth.md",
        "ebook_md": "chapter08_ebook.md",
        "syllabus_md": "chapter08_syllabus.md"
    },
    {
        "num": 9,
        "filename": "ch09_anaerobic_microbiology.tex",
        "title": "จุลชีววิทยาแบบไม่ใช้ออกซิเจนและการเพาะเลี้ยง",
        "label": "chap:ch09",
        "folder": "chapter9",
        "main_md": "chapter09_anaerobe.md",
        "ebook_md": "chapter09_ebook.md",
        "syllabus_md": "chapter09_syllabus.md"
    },
    {
        "num": 10,
        "filename": "ch10_metabolism_biochemical.tex",
        "title": "สรีรวิทยา เมแทบอลิซึม และการทดสอบทางชีวเคมี",
        "label": "chap:ch10",
        "folder": "chapter10",
        "main_md": "chapter10_microbial_metabolism.md",
        "ebook_md": "chapter10_ebook.md",
        "syllabus_md": "chapter10_syllabus.md"
    },
    {
        "num": 11,
        "filename": "ch11_microbial_control.tex",
        "title": "การควบคุมจุลินทรีย์ด้วยวิธีทางกายภาพ สารเคมี และยาต้านจุลชีพ",
        "label": "chap:ch11",
        "folder": "chapter11",
        "main_md": "chapter11_control_of_microorganisms.md",
        "ebook_md": "chapter11_ebook.md",
        "syllabus_md": "chapter11_syllabus.md"
    },
    {
        "num": 12,
        "filename": "ch12_water_bioremediation_bioblock.tex",
        "title": "อาณาจักรฟังไจและการประยุกต์บำบัดน้ำเสียด้วยนวัตกรรมชีวภาพ",
        "label": "chap:ch12",
        "folder": "chapter12",
        "main_md": "chapter12_fungi.md",
        "ebook_md": "chapter12_ebook.md",
        "syllabus_md": "chapter12_syllabus.md"
    }
]

print("Setup chapter metadata complete. Total:", len(chapters_info))
