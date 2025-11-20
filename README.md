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

poetry shell
poetry env remove python
poetry env use 3.10
poetry install
poetry lock
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

Verif remote existant
> git remote -v

si no exist 
> git remote add github https://github.com/username/nutriscore-app.git
> git remote add huggingface https://huggingface.co/spaces/lililoving/nutriscore-app

si error
> git remote remove huggingface

cmd git :
>git add .
>git commit -m "Mise à jour"
>git push github main  # Vers GitHub
>git push huggingface main  # Vers Hugging Face

> git pull huggingface main