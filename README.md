# Nutri-Score Simulator

Application interactive pour visualiser l’impact des quantités sur un Nutri-Score estimé.

## Démarrage local

```bash
poetry install
poetry run python nutriscore_sim/app.py
```

Memo
Resumé des commandes :
poetry add gradio matplotlib

git init && git add . && git commit -m "First commit"

Pour générer le requirement a partir de poetry :

poetry self add poetry-plugin-export
poetry export --without-hashes -f requirements.txt --output requirements.txt
