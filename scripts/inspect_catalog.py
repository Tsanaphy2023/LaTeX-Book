#!/usr/bin/env python3
"""
Latex2026 Catalog Inspector & Link Validator
Author: Dr. Chewa Thassana (chewa.t@rbru.ac.th)
Rambhai Barni Rajabhat University
"""

import json
import os
import sys

CATALOG_PATH = os.path.join(os.path.dirname(__file__), "..", "google_drive_catalog.json")

def main():
    if not os.path.exists(CATALOG_PATH):
        print(f"Error: Catalog file not found at {CATALOG_PATH}")
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    print("=" * 80)
    print(f"PROJECT: {catalog.get('project_title')} -> Workspace: {catalog.get('workspace_target')}")
    print(f"OWNER:   {catalog['owner']['name']} ({catalog['owner']['email']})")
    print(f"INSTITUTION: {catalog['owner']['institution']}")
    print(f"ROOT URL:    {catalog['root_google_drive']['url']}")
    print("=" * 80)

    modules = catalog.get("modules", [])
    print(f"Total Registered Modules: {len(modules)}\n")

    for idx, mod in enumerate(modules, 1):
        name = mod.get("name")
        m_type = mod.get("type", "N/A")
        lang = mod.get("language", "-")
        f_id = mod.get("folder_id")
        url = mod.get("url")

        print(f"[{idx:02d}] {name} ({m_type}) | Language: {lang}")
        print(f"     Folder ID: {f_id}")
        print(f"     URL:       {url}")

        if "compiled_pdf" in mod:
            pdf = mod["compiled_pdf"]
            print(f"     Compiled PDF: {pdf['file_name']} -> {pdf['view_url']}")

        if "chapters" in mod:
            print(f"     Chapters Count: {len(mod['chapters'])}")
            for ch in mod["chapters"]:
                ch_title = ch.get("title_th") or ch.get("title_en") or ch.get("name")
                print(f"       - Chapter {ch['chapter']}: {ch_title} (ID: {ch['folder_id']})")
        print("-" * 80)

if __name__ == "__main__":
    main()
