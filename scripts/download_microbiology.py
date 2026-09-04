#!/usr/bin/env python3
import os
import urllib.request
import ssl

ssl_context = ssl._create_unverified_context()

BASE_DIR = "/Applications/XAMPP/xamppfiles/htdocs/04_Education_Exam/Latex2026/07_Microbiology_for_Agriculture_LaTeX"

FILES_MAP = {
    # Prefaces
    "prefaces/preface.tex": "1B-kT3TZP85GtvrkMwbMPd-a3L5VRpWL6",
    "prefaces/acknowledgements.tex": "1uMphpf3LxT1LxMtT4Qk1SH6sgFIa8a_M",
    # Chapters
    "chapters/introduction.tex": "1piUVaKVvdfGmnmMyo73v_GwkWofOhMUk",
    "chapters/chapter1.tex": "1VZbFWEe0_47ELc3-_W0uPq1KfOHDed5g",
    "chapters/chapter2.tex": "1X7yxm1a9CoN5c0k-Li5I3wPo8_pFJ5TZ",
    "chapters/chapter3.tex": "1MrZvwOHGlzPbpy5UlINfCd6gPRADODmn",
    "chapters/chapter4.tex": "1ZTAGQ5Wby-QQ_sOd591kw7YdZ-c28XLp",
    "chapters/chapter5.tex": "1jhF786kY4xAUOLkiT-HQ0gNvrhodJZZv",
    "chapters/chapter6.tex": "1lq6UMLhiUXpIY2Rv0mAFBSOZMFWIB9md",
    "chapters/chapter7.tex": "11WAaFBJ6-zA0Pcll0ozrDgSY8EIT7HZZ",
    "chapters/chapter8.tex": "1dY3Hk_4gqPlcDyu_RCMFU_GYJ93yC2Xz",
    "chapters/chapter9.tex": "1FnfQUgXpl9K0SmmgaBKoJUUDIOuRZn2b",
    # Appendices
    "appendices/appendixA.tex": "159G8BjtQMHlQHPOCTtox4pt_pge7d6pj",
    "appendices/appendixB.tex": "1cyxw0CjMIRHzoQM6EwSBRAul3zDVN4m9",
    "appendices/appendixC.tex": "1a0y1UORwItL51rXfIddgilCju5leHwtE",
    "appendices/appendixD.tex": "1aOSjRdZALmFWEGvwfThVaaRb2NeAwxUS",
    # Bibliography
    "bibliography/references.bib": "127JTttVqjXZpOwGHBNvwGpIDgoZgLf06",
    # Background
    "figures/background.jpg": "14g40a6YxaPb5Udov_2gmdT7x7TV-PCMy"
}

def download_file(file_id, dest_path):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ssl_context) as response, open(dest_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
        print(f"Downloaded {dest_path}: {len(data)} bytes")

for rel_path, file_id in FILES_MAP.items():
    dest = os.path.join(BASE_DIR, rel_path)
    try:
        download_file(file_id, dest)
    except Exception as e:
        print(f"Error downloading {rel_path}: {e}")
