import os
import re
import glob

base_dir = "08_MicroEnvi"
source_dir = os.path.join(base_dir, "source_docs", "Micro_Lab")
chapters_dir = os.path.join(base_dir, "chapters")
os.makedirs(chapters_dir, exist_ok=True)

def clean_text_for_latex(text):
    # Escape special LaTeX characters if not in math or commands
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('_', '\\_')
    text = text.replace('#', '\\#')
    # Fix degrees Celsius
    text = text.replace('°C', '$^{\\circ}$C')
    text = text.replace('°', '$^{\\circ}$')
    # Fix arrows
    text = text.replace('→', '$\\rightarrow$')
    text = text.replace('←', '$\\leftarrow$')
    text = text.replace('±', '$\\pm$')
    text = text.replace('μ', '$\\mu$')
    text = text.replace('µ', '$\\mu$')
    text = text.replace('×', '$\\times$')
    text = text.replace('≤', '$\\le$')
    text = text.replace('≥', '$\\ge$')
    return text

def sanitize_heading(heading):
    # Remove colons
    h = heading.replace(':', '').replace('：', '')
    # Remove leading numbers like 1.1, 1.2.3, etc.
    h = re.sub(r'^[0-9]+(\.[0-9]+)*\s*', '', h)
    # Remove parentheses with English or acronyms from heading
    # e.g., "กฎระเบียบ (Biosafety Guidelines)" -> "กฎระเบียบ"
    english_match = re.search(r'\(([^)]*[a-zA-Z]+[^)]*)\)', h)
    eng_term = ""
    if english_match:
        eng_term = english_match.group(1).strip()
        h = re.sub(r'\(([^)]*[a-zA-Z]+[^)]*)\)', '', h).strip()
    return h.strip(), eng_term

print("Helper functions ready.")
