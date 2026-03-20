#!/usr/bin/env python3
"""
_ci/check_metadata.py
Valide les métadonnées YAML des fichiers .qmd avant déploiement.
Vérifie : titre présent, date valide, catégorie(s) autorisée(s).
"""

import os
import sys
import yaml
import re
from pathlib import Path

# Dossiers à scanner (hors templates et notes)
SCAN_DIRS = ["articles", "projets", "reviews"]
CATEGORIES_FILE = "_ci/valid_categories.yml"
ERRORS = []

# Charge les catégories valides
with open(CATEGORIES_FILE) as f:
    valid_categories = set(yaml.safe_load(f)["categories"])

def extract_frontmatter(filepath):
    """Extrait le bloc YAML frontmatter d'un fichier .qmd"""
    content = Path(filepath).read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

def check_file(filepath):
    """Valide les métadonnées d'un fichier .qmd"""
    rel = os.path.relpath(filepath)

    # Ignorer les templates et les drafts
    if Path(filepath).stem.startswith("_"):
        return
    
    meta = extract_frontmatter(filepath)
    if meta is None:
        ERRORS.append(f"[{rel}] Frontmatter YAML manquant ou invalide")
        return

    # Ignorer les drafts explicites
    if meta.get("draft", False):
        return

    # Vérification titre
    if not meta.get("title") or meta["title"].startswith("["):
        ERRORS.append(f"[{rel}] Titre manquant ou placeholder non remplacé")

    # Vérification date
    if not meta.get("date"):
        ERRORS.append(f"[{rel}] Date manquante")

    # Vérification catégories
    cats = meta.get("categories", [])
    if not cats:
        ERRORS.append(f"[{rel}] Aucune catégorie définie")
    else:
        for cat in cats:
            if cat not in valid_categories:
                ERRORS.append(
                    f"[{rel}] Catégorie inconnue : '{cat}' "
                    f"(valides : {', '.join(sorted(valid_categories))})"
                )

# Scan des dossiers
for scan_dir in SCAN_DIRS:
    for qmd_file in Path(scan_dir).rglob("*.qmd"):
        check_file(qmd_file)

# Résultat
if ERRORS:
    print("❌ Erreurs de métadonnées détectées :\n")
    for err in ERRORS:
        print(f"  • {err}")
    sys.exit(1)
else:
    print(f"✅ Métadonnées valides ({sum(1 for d in SCAN_DIRS for _ in Path(d).rglob('*.qmd'))} fichiers scannés)")
    sys.exit(0)
