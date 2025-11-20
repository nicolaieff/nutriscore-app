import gradio as gr
import pandas as pd
import plotly.express as px

# Charger dataset local
df = pd.read_parquet("food_toviz.parquet")
df_country = pd.read_parquet("nutrisc_country.parquet")


palette_nutriscore = [
    (0.0, "#009E3A"),  # A
    (0.20, "#7ED321"),  # B
    (0.52, "#FFEB3B"),  # C
    (0.84, "#FFA500"),  # D
    (1.0, "#E60000")    # E
]


def plot_country_map():
    df = df_country.copy()
    fig = px.choropleth(
        df,
        locations="country_iso3",
        color="nutriscore_mediane",
        hover_name="country_0",
        hover_data=["nutriscore_moyen", "nb_produits"],
        color_continuous_scale=palette_nutriscore,
        # title="Qualité nutritionnelle médiane par pays (Nutriscore)",
        )
    fig.update_layout(
        geo=dict(
            bgcolor="beige",
            lakecolor="beige",
            showland=True,
            landcolor="beige",
            showocean=True,
            oceancolor="lightblue",
            showframe=False,
            projection_type="natural earth"
        ),
        paper_bgcolor="beige",
        margin={"r":0,"t":0,"l":0,"b":0}  # gauche, droite, haut, bas
        )
    return fig


def filtrer_dataframe(colonne, valeur_min, valeur_max):
    # Vérification de colonne
    if colonne not in df.columns:
        return "Colonne inexistante", None
    
    # Filtrage pandas classique
    res = df[(df[colonne] >= valeur_min) & (df[colonne] <= valeur_max)]
    
    return f"{len(res)} lignes sélectionnées", res


def choisir_shap(avec_cat: bool):
    if avec_cat:
        return "shap_summary_all.png"
    else:
        return "shap_summary_nutriments.png"


with gr.Blocks() as demo:
    gr.Markdown("# Nutriscore")

    with gr.Tabs():  
        # ---- ONGLET 1 ---- ok
        with gr.Tab("🌍 Carte par pays"):
            gr.Markdown("### Nutriscore médian par pays")
            gr.Markdown("*Affichage des pays avec au moins 20 000 produits*")
            plot2 = gr.Plot(value=plot_country_map(), label="Carte", elem_classes="w-full")


        # ---- ONGLET 2 ---- ok
        with gr.Tab("🤖 Modèle explication"):
            gr.Markdown("### SHAP value")
            with gr.Row():
                btn_cat = gr.Button("Avec catégories")
                btn_sans_cat = gr.Button("Sans catégories")

            sortie_shap = gr.Image(value="shap_summary_all.png", label="SHAP")

            btn_cat.click(fn=choisir_shap, inputs=gr.State(True), outputs=sortie_shap)
            btn_sans_cat.click(fn=choisir_shap, inputs=gr.State(False), outputs=sortie_shap)


        # ---- ONGLET 3 ----
        with gr.Tab("🍕 Un aliment"):
            gr.Markdown("### Analyse d'un aliment")

            aliment = gr.Textbox(label="Nom de l'aliment")
            bouton3 = gr.Button("Analyser")
            sortie3 = gr.Textbox(label="Résultat")

            # bouton3.click(analyse_aliment, inputs=aliment, outputs=sortie3)

    gr.Markdown("## Visualisation fixe global")
    gr.DataFrame(df.head(6), label="Les données")
    

if __name__ == "__main__":
    # demo.launch(share=True)
    demo.launch()