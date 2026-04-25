#!/usr/bin/env python3
"""
_ci/check_metadata.py
Valide les métadonnées YAML des fichiers .qmd avant déploiement.
Vérifie : titre présent, date valide, catégorie(s) autorisée(s).

Règles d'exclusion :
- Fichiers préfixés par _ (templates)
- index.qmd à la racine directe d'un dossier de section (pages de listing)
- index.qmd dans un sous-dossier = article valide, soumis aux checks
"""

import os
import sys
import yaml
import re
from pathlib import Path

# Dossiers de section à scanner
SCAN_DIRS = ["articles", "projets", "reviews"]
CATEGORIES_FILE = "_ci/valid_categories.yml"
IGNORE_PREFIXES = {"_"}
ERRORS = []

# Charge les catégories valides
with open(CATEGORIES_FILE) as f:
    valid_categories = set(yaml.safe_load(f)["categories"])

def is_listing_page(filepath, scan_dirs):
    """
    Retourne True si le fichier est un index.qmd de listing —
    c'est-à-dire un index.qmd directement à la racine d'un dossier de section.
    Ex : articles/index.qmd → listing (ignoré)
         articles/mon-article/index.qmd → article (vérifié)
    """
    p = Path(filepath)
    if p.name != "index.qmd":
        return False
    # Le parent direct est-il un dossier de section ?
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

    # Ignorer les templates
    if any(stem.startswith(p) for p in IGNORE_PREFIXES):
        return

    # Ignorer les pages de listing (index.qmd à la racine d'une section)
    if is_listing_page(filepath, scan_dirs):
        return

    rel = os.path.relpath(filepath)
    meta = extract_frontmatter(filepath)

    if meta is None:
        ERRORS.append(f"[{rel}] Frontmatter YAML manquant ou invalide")
        return

    # Ignorer les drafts
    if meta.get("draft", False):
        return

    # Vérification titre
    if not meta.get("title") or str(meta["title"]).startswith("["):
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

# Scan
scanned = 0
for scan_dir in SCAN_DIRS:
    for qmd_file in Path(scan_dir).rglob("*.qmd"):
        check_file(qmd_file, SCAN_DIRS)
        scanned += 1

# Résultat
if ERRORS:
    print("❌ Erreurs de métadonnées détectées :\n")
    for err in ERRORS:
        print(f"  • {err}")
    sys.exit(1)
else:
    print(f"✅ Métadonnées valides ({scanned} fichiers scannés)")
    sys.exit(0)
