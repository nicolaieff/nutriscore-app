import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger dataset local
df = pd.read_parquet("food_toviz.parquet")


def filtrer_dataframe(colonne, valeur_min, valeur_max):
    # Vérification de colonne
    if colonne not in df.columns:
        return "Colonne inexistante", None
    
    # Filtrage pandas classique
    res = df[(df[colonne] >= valeur_min) & (df[colonne] <= valeur_max)]
    
    return f"{len(res)} lignes sélectionnées", res



def stats_pays(pays):
    return f"Statistiques du pays : {pays}"

def stats_modele(param):
    return f"Performances du modèle avec paramètre : {param}"

def analyse_aliment(nom):
    return f"Analyse nutritionnelle de l’aliment : {nom}"


with gr.Blocks() as demo:
    gr.Markdown("# Tableau de bord Nutrition")

    with gr.Tabs():  
        # ---- ONGLET 1 ----
        with gr.Tab("Pays - Stats"):
            gr.Markdown("### Statistiques par pays")
            pays = gr.Dropdown(["France", "Italie", "Espagne", "USA"], label="Choisir un pays")
            bouton1 = gr.Button("Afficher")
            sortie1 = gr.Textbox(label="Résultat")
            bouton1.click(stats_pays, inputs=pays, outputs=sortie1)

        # ---- ONGLET 2 ----
        with gr.Tab("Modèle - Stats"):
            gr.Markdown("### Statistiques du modèle")
            param = gr.Slider(0, 1, step=0.1, label="Paramètre du modèle")
            bouton2 = gr.Button("Calculer")
            sortie2 = gr.Textbox(label="Résultat")
            bouton2.click(stats_modele, inputs=param, outputs=sortie2)

        # ---- ONGLET 3 ----
        with gr.Tab("Aliment - Analyse"):
            gr.Markdown("### Analyse d’un aliment")
            aliment = gr.Textbox(label="Nom de l’aliment")
            bouton3 = gr.Button("Analyser")
            sortie3 = gr.Textbox(label="Résultat")
            bouton3.click(analyse_aliment, inputs=aliment, outputs=sortie3)

    gr.Markdown("## Visualisation et filtrage d’un dataset local (pandas)")
    
    # Aperçu initial : 50 premières lignes
    gr.DataFrame(df.head(50), label="Aperçu du dataset (50 premières lignes)")
    
    # Widgets
    colonne = gr.Dropdown(choices=df.columns.tolist(), label="Choisir une colonne")
    min_val = gr.Number(label="Valeur min")
    max_val = gr.Number(label="Valeur max")

    bouton = gr.Button("Filtrer")

    # Sorties
    sortie_texte = gr.Textbox(label="Résultat")
    sortie_table = gr.DataFrame(label="DataFrame filtrée")

    # Callbacks
    bouton.click(
        filtrer_dataframe,
        inputs=[colonne, min_val, max_val],
        outputs=[sortie_texte, sortie_table]
    )

if __name__ == "__main__":
    # demo.launch(share=True)
    demo.launch()