# Structure du projet blog — benhafed.com

## Environnement Python

Un seul venv centralisé à la racine, géré par uv.

```bash
uv sync                  # installer / mettre à jour les dépendances
uv add <package>         # ajouter une dépendance
```

Commandes Quarto à lancer depuis la racine :

```bash
uv run quarto preview    # prévisualisation locale
uv run quarto render     # build complet
```

Dans VSCode : sélectionner `.venv/bin/python` comme interpréteur Python
(Cmd+Shift+P → "Python: Select Interpreter" → `./.venv/bin/python`).

---

blog/
├── _quarto.yml                       configuration principale
├── pyproject.toml                    dépendances Python centralisées (uv)
├── uv.lock                           lockfile uv (commité)
├── custom.scss                       identité visuelle
├── index.qmd                         page d'accueil du blog
│
├── articles/
│   ├── index.qmd                     listing articles (grid + image)
│   ├── _template_article.qmd         template — titre, date, catégorie, image cover
│   └── YYYY-MM-DD-slug/
│       ├── index.qmd                 article
│       └── cover.png                 image IA — 1200×630px
│
├── projets/
│   ├── index.qmd                     listing projets (grid)
│   ├── _template_projet.qmd          template — structure cohérente
│   └── nom-projet/
│       ├── index.qmd                 page projet
│       └── cover.png                 image optionnelle
│
├── reviews/
│   ├── index.qmd                     listing reviews (grid)
│   ├── _template_review.qmd          template
│   └── YYYY-titre.qmd                une review = un fichier
│
├── notes/
│   ├── index.qmd                     listing notes (grid, titre + tag)
│   ├── _template_note.qmd            template minimal — titre court, date, tag
│   └── YYYY-MM-DD-slug.qmd           une note = un fichier
│
├── assets/
│   ├── favicon.ico
│   └── og-image.png                  image Open Graph par défaut (1200×630px)
│
├── _ci/
│   ├── valid_categories.yml          catégories autorisées (extensible)
│   └── check_metadata.py             validation YAML avant déploiement
│
├── .github/
│   └── workflows/
│       ├── deploy-dev.yml            CI/CD → preprod (push sur dev)
│       └── deploy-prod.yml           CI/CD → prod (merge sur main)
│
├── .vale.ini                         config correcteur orthographique FR
└── .gitignore
