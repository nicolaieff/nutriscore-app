---
title: NutriScore App
emoji: 🥗
colorFrom: green
colorTo: red
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
---

# Nutri-Score Simulator

Application interactive pour visualiser l’impact des quantités sur un Nutri-Score estimé.

## Démarrage local

```bash
poetry install
poetry run python app.py
```

Memo - Resumé des commandes POETRY :
. pour entrer dans le shell virtuel Poetry
> poetry shell

. ajouter une lib
> poetry add gradio matplotlib

. reinstaller les dépendances manquantes
> poetry install

. recrée l'env propre
poetry env remove python
poetry install

. pour voir une installation
> poetry run python -c "import gradio; print(gradio.__version__)"


Memo GIT :
> git init && git add . && git commit -m "First commit"

Pour générer le requirement a partir de poetry :
poetry self add poetry-plugin-export
poetry export --without-hashes -f requirements.txt --output requirements.txt

git add .
git commit -m "Mise à jour"
git push github main  # Vers GitHub
git push huggingface main  # Vers Hugging Face
