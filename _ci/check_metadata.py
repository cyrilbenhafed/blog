#!/usr/bin/env python3
"""
_ci/check_metadata.py
Validates YAML metadata of .qmd files before deployment.
Checks: title present, date valid, category/ies authorized.

Exclusion rules:
- Files prefixed with _ (templates)
- index.qmd at the root of a section folder (listing pages)
- index.qmd in a subfolder = article, subject to checks
"""

import os
import sys
import yaml
import re
from pathlib import Path

# Section folders to scan
SCAN_DIRS = ["articles", "projets", "reviews"]
CATEGORIES_FILE = "_ci/valid_categories.yml"
IGNORE_PREFIXES = {"_"}
ERRORS = []

# Load valid categories
with open(CATEGORIES_FILE) as f:
    valid_categories = set(yaml.safe_load(f)["categories"])

def is_listing_page(filepath, scan_dirs):
    """
    Returns True if the file is a listing index.qmd —
    i.e. an index.qmd directly at the root of a section folder.
    Ex: articles/index.qmd -> listing (ignored)
        articles/my-article/index.qmd -> article (checked)
    """
    p = Path(filepath)
    if p.name != "index.qmd":
        return False
    return p.parent.name in scan_dirs

def extract_frontmatter(filepath):
    content = Path(filepath).read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

def check_file(filepath, scan_dirs):
    stem = Path(filepath).stem

    # Skip templates
    if any(stem.startswith(p) for p in IGNORE_PREFIXES):
        return

    # Skip listing pages (index.qmd at section root)
    if is_listing_page(filepath, scan_dirs):
        return

    rel = os.path.relpath(filepath)
    meta = extract_frontmatter(filepath)

    if meta is None:
        ERRORS.append(f"[{rel}] Missing or invalid YAML frontmatter")
        return

    # Skip drafts
    if meta.get("draft", False):
        return

    # Check title
    if not meta.get("title") or str(meta["title"]).startswith("["):
        ERRORS.append(f"[{rel}] Missing title or unreplaced placeholder")

    # Check date
    if not meta.get("date"):
        ERRORS.append(f"[{rel}] Missing date")

    # Check categories
    cats = meta.get("categories", [])
    if not cats:
        ERRORS.append(f"[{rel}] No category defined")
    else:
        for cat in cats:
            if cat not in valid_categories:
                ERRORS.append(
                    f"[{rel}] Unknown category: '{cat}' "
                    f"(valid: {', '.join(sorted(valid_categories))})"
                )

# Scan
scanned = 0
for scan_dir in SCAN_DIRS:
    for qmd_file in Path(scan_dir).rglob("*.qmd"):
        check_file(qmd_file, SCAN_DIRS)
        scanned += 1

# Result
if ERRORS:
    print("❌ Metadata errors detected:\n")
    for err in ERRORS:
        print(f"  • {err}")
    sys.exit(1)
else:
    print(f"✅ Valid metadata ({scanned} files scanned)")
    sys.exit(0)
