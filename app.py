import gradio as gr
import pandas as pd
import plotly.express as px

# Charger dataset local
df = pd.read_parquet("food_toviz.parquet")
df_country = pd.read_parquet("nutrisc_country.parquet")
df_aliment = pd.read_parquet("aliments_quantity.parquet")


palette_nutriscore = [
    (0.0, "#009E3A"),  # A
    (0.20, "#7ED321"),  # B
    (0.52, "#FFEB3B"),  # C
    (0.84, "#FFA500"),  # D
    (1.0, "#E60000")    # E
]

dict_color = {
    "A": "#009E3A",
    "B": "#7ED321",
    "C": "#FFEB3B",
    "D": "#FFA500",
    "E": "#E60000"
}



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

    if colonne not in df.columns:
        return "Colonne inexistante", None

    res = df[(df[colonne] >= valeur_min) & (df[colonne] <= valeur_max)]
    
    return f"{len(res)} lignes sélectionnées", res


def choisir_shap(avec_cat: bool):
    if avec_cat:
        return "shap_summary_all.png"
    else:
        return "shap_summary_nutriments.png"


def afficher_aliment(id_aliment, quantite):
    selection = df_aliment[
        (df_aliment["id_aliment"] == id_aliment) &
        (df_aliment["quantite"] == quantite)
    ]
    
    if selection.empty:
        return pd.DataFrame({"Features": [], "Values": []})
    
    ligne_dict = selection.iloc[0].to_dict()
    
    df_produit = pd.DataFrame({
        "Features": list(ligne_dict.keys()),
        "Values": list(ligne_dict.values())
    })

    def color_nutriscore(val, row):
        if row["Features"] == "nutriscore_score_pred_grade":
            return f"background-color: {dict_color.get(val, "#fdf1b8")}; color: black;"
        return ""
    
    df_styled = df_produit.style.apply(lambda row: [color_nutriscore(val, row) for val in row], axis=1)

    return df_styled.to_html()

aliments_disponibles = df_aliment["id_aliment"].unique().tolist()
quantites_disponibles = df_aliment["quantite"].unique().tolist()


with gr.Blocks() as demo:
    gr.Markdown("# Nutriscore visualisation")

    with gr.Tabs():  
        # ---- ONGLET 1 ---- ok
        with gr.Tab("🌍 Carte par pays"):
            gr.Markdown("### Nutriscore médian par pays")
            gr.Markdown("*Pays présent dans les données*")
            plot2 = gr.Plot(value=plot_country_map(), label="Carte", elem_classes="w-full")


        # ---- ONGLET 2 ---- ok
        with gr.Tab("🤖 Modèle explication"):
            gr.Markdown("### SHAP value du model")
            with gr.Row():
                btn_cat = gr.Button("Avec catégories")
                btn_sans_cat = gr.Button("Sans catégories")

            sortie_shap = gr.Image(value="shap_summary_all.png", label="SHAP")

            btn_cat.click(fn=choisir_shap, inputs=gr.State(True), outputs=sortie_shap)
            btn_sans_cat.click(fn=choisir_shap, inputs=gr.State(False), outputs=sortie_shap)


        # ---- ONGLET 3 ---- ok
        with gr.Tab("🍕 Un aliment"):
            gr.Markdown("### Analyse d'un aliment")

            aliment_dropdown = gr.Dropdown(label="Nom de l'aliment", 
                                           choices=aliments_disponibles, 
                                           value=aliments_disponibles[0])

            quantite_slider = gr.Slider(label="Quantité (g)", 
                                        minimum=min(quantites_disponibles),
                                        maximum=max(quantites_disponibles), 
                                        step=20, value=100)

            table_html = gr.HTML()

            aliment_dropdown.change(fn=afficher_aliment, 
                                    inputs=[aliment_dropdown, quantite_slider], 
                                    outputs=table_html)
            quantite_slider.change(fn=afficher_aliment, 
                                   inputs=[aliment_dropdown, quantite_slider], 
                                   outputs=table_html)



    gr.Markdown("## Visualisation fixe des données")
    gr.DataFrame(df.head(6), label="La table")
    

if __name__ == "__main__":
    # demo.launch(share=True)
    demo.launch()