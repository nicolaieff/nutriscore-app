import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def afficher_graphique(nb_points=10):
    x = np.linspace(0, 10, nb_points)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Exemple de graphique")
    plt.xlabel("X")
    plt.ylabel("sin(X)")
    plt.grid(True)
    return plt

demo = gr.Interface(
    fn=afficher_graphique,
    inputs=gr.Slider(5, 100, value=10, step=1, label="Nombre de points"),
    outputs=gr.Plot(),
    title="Mon App de Graphiques",
    description="Ajuste le nombre de points pour voir le graphique de sin(x)."
)

demo.launch()
