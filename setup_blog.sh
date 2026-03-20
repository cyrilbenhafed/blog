#!/usr/bin/env bash
# setup_blog.sh — Génère la structure du projet blog benhafed.com
# Usage : bash setup_blog.sh [nom_du_dossier]
# Par défaut, crée le projet dans ./blog

set -e

PROJECT="${1:-blog}"

echo "🏗️  Création de la structure du blog dans ./${PROJECT}/"
echo ""

# ── Dossiers ────────────────────────────────────────────────────────────────

mkdir -p "${PROJECT}/articles"
mkdir -p "${PROJECT}/projets"
mkdir -p "${PROJECT}/reviews"
mkdir -p "${PROJECT}/notes"
mkdir -p "${PROJECT}/assets"
mkdir -p "${PROJECT}/_ci"
mkdir -p "${PROJECT}/.github/workflows"

# ── Fichiers racine — PLACEHOLDER ───────────────────────────────────────────

cat > "${PROJECT}/_quarto.yml" << 'EOF'
PLACEHOLDER — remplacer par _quarto.yml généré
EOF
echo "  📄 _quarto.yml              [PLACEHOLDER]"

cat > "${PROJECT}/custom.scss" << 'EOF'
PLACEHOLDER — remplacer par custom.scss généré
EOF
echo "  📄 custom.scss              [PLACEHOLDER]"

cat > "${PROJECT}/index.qmd" << 'EOF'
PLACEHOLDER — remplacer par index.qmd généré
EOF
echo "  📄 index.qmd                [PLACEHOLDER]"

# ── .gitignore ───────────────────────────────────────────────────────────────

cat > "${PROJECT}/.gitignore" << 'EOF'
# Quarto output
_site/
_freeze/
.quarto/

# Cache
*_cache/
*.~lock*

# macOS
.DS_Store

# R
.Rhistory
.RData
.Rproj.user/

# Python
__pycache__/
*.pyc
.env

# Editors
.vscode/
*.swp
EOF
echo "  📄 .gitignore               ✅"

# ── Articles ─────────────────────────────────────────────────────────────────

cat > "${PROJECT}/articles/index.qmd" << 'EOF'
PLACEHOLDER — remplacer par articles/index.qmd généré
EOF
echo "  📄 articles/index.qmd       [PLACEHOLDER]"

cat > "${PROJECT}/articles/_template_article.qmd" << 'EOF'
PLACEHOLDER — remplacer par articles/_template_article.qmd généré
EOF
echo "  📄 articles/_template_article.qmd  [PLACEHOLDER]"

# ── Projets ──────────────────────────────────────────────────────────────────

cat > "${PROJECT}/projets/index.qmd" << 'EOF'
PLACEHOLDER — remplacer par projets/index.qmd généré
EOF
echo "  📄 projets/index.qmd        [PLACEHOLDER]"

cat > "${PROJECT}/projets/_template_projet.qmd" << 'EOF'
PLACEHOLDER — remplacer par projets/_template_projet.qmd généré
EOF
echo "  📄 projets/_template_projet.qmd    [PLACEHOLDER]"

# ── Reviews ──────────────────────────────────────────────────────────────────

cat > "${PROJECT}/reviews/index.qmd" << 'EOF'
PLACEHOLDER — remplacer par reviews/index.qmd généré
EOF
echo "  📄 reviews/index.qmd        [PLACEHOLDER]"

cat > "${PROJECT}/reviews/_template_review.qmd" << 'EOF'
PLACEHOLDER — remplacer par reviews/_template_review.qmd généré
EOF
echo "  📄 reviews/_template_review.qmd    [PLACEHOLDER]"

# ── Notes ────────────────────────────────────────────────────────────────────

cat > "${PROJECT}/notes/index.qmd" << 'EOF'
PLACEHOLDER — remplacer par notes/index.qmd généré
EOF
echo "  📄 notes/index.qmd          [PLACEHOLDER]"

cat > "${PROJECT}/notes/_template_note.qmd" << 'EOF'
PLACEHOLDER — remplacer par notes/_template_note.qmd généré
EOF
echo "  📄 notes/_template_note.qmd [PLACEHOLDER]"

# ── Assets ───────────────────────────────────────────────────────────────────

touch "${PROJECT}/assets/favicon.ico"
touch "${PROJECT}/assets/og-image.png"
echo "  📄 assets/favicon.ico       [À remplacer par ta favicon]"
echo "  📄 assets/og-image.png      [À remplacer par ton image OG 1200×630px]"

# ── CI ───────────────────────────────────────────────────────────────────────

cat > "${PROJECT}/_ci/valid_categories.yml" << 'EOF'
PLACEHOLDER — remplacer par _ci/valid_categories.yml généré
EOF
echo "  📄 _ci/valid_categories.yml [PLACEHOLDER]"

cat > "${PROJECT}/_ci/check_metadata.py" << 'EOF'
PLACEHOLDER — remplacer par _ci/check_metadata.py généré
EOF
echo "  📄 _ci/check_metadata.py    [PLACEHOLDER]"

# ── GitHub Actions ───────────────────────────────────────────────────────────

cat > "${PROJECT}/.github/workflows/deploy-dev.yml" << 'EOF'
PLACEHOLDER — remplacer par .github/workflows/deploy-dev.yml généré
EOF
echo "  📄 .github/workflows/deploy-dev.yml   [PLACEHOLDER]"

cat > "${PROJECT}/.github/workflows/deploy-prod.yml" << 'EOF'
PLACEHOLDER — remplacer par .github/workflows/deploy-prod.yml généré
EOF
echo "  📄 .github/workflows/deploy-prod.yml  [PLACEHOLDER]"

# ── Vale ─────────────────────────────────────────────────────────────────────

cat > "${PROJECT}/.vale.ini" << 'EOF'
PLACEHOLDER — remplacer par .vale.ini généré
EOF
echo "  📄 .vale.ini                [PLACEHOLDER]"

# ── Résumé ───────────────────────────────────────────────────────────────────

echo ""
echo "✅ Structure créée dans ./${PROJECT}/"
echo ""
echo "📋 Fichiers PLACEHOLDER à remplacer par les artefacts générés :"
echo "   grep -rl 'PLACEHOLDER' ./${PROJECT}/"
echo ""
echo "📋 Fichiers assets à remplacer manuellement :"
echo "   • assets/favicon.ico       → ta favicon"
echo "   • assets/og-image.png      → image Open Graph 1200×630px"
echo ""
echo "📋 Prochaines étapes :"
echo "   1. Remplacer les PLACEHOLDERs par les fichiers générés"
echo "   2. Créer le repo GitHub et pousser sur la branche dev"
echo "   3. Configurer le CNAME blog.benhafed.com chez ton registrar"
echo "   4. Activer GitHub Pages sur le repo (branche gh-pages)"
echo "   5. Renseigner repo-id et category-id Giscus quand le moment vient"
