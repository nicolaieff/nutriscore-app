# nutriscore_sim/app.py

import gradio as gr
import matplotlib.pyplot as plt

products = ["Produit A", "Produit B", "Produit C"]
base_scores = [70, 50, 30]

def update_nutriscore(q1, q2, q3):
    quantities = [q1, q2, q3]
    scores = [max(0, s - q*2) for s, q in zip(base_scores, quantities)]

    fig, ax = plt.subplots()
    ax.bar(products, scores, color='green')
    ax.set_ylim(0, 100)
    ax.set_ylabel("Nutri-Score estimé")
    ax.set_title("Impact des quantités sur le Nutri-Score")
    return fig

interface = gr.Interface(
    fn=update_nutriscore,
    inputs=[
        gr.Slider(0, 10, step=1, label="Quantité Produit A"),
        gr.Slider(0, 10, step=1, label="Quantité Produit B"),
        gr.Slider(0, 10, step=1, label="Quantité Produit C"),
    ],
    outputs=gr.Plot(),
    title="Simulation Nutri-Score",
    description="Ajustez les quantités des produits pour voir l’impact sur leur Nutri-Score estimé.",
    live=True
)

if __name__ == "__main__":
    interface.launch()
