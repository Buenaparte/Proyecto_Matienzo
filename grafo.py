import networkx as nx
import matplotlib.pyplot as plt
from validations import cargar_csv

def dibujar_grafo(grafo_dict):
    # 1. Crear el objeto de grafo de NetworkX
    # Usamos DiGraph() si es dirigido o Graph() si no lo es
    G = nx.Graph() 

    # 2. Añadir aristas desde tu diccionario
    for nodo, vecinos in grafo_dict.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    # 3. Definir el diseño (layout)
    pos = nx.spring_layout(G)  # Distribuye los nodos de forma estética

    # 4. Dibujar nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='skyblue', 
            node_size=2000, edge_color='gray', font_size=15, font_weight='bold')

    # 5. Dibujar los pesos (los costos de los caminos)
    etiquetas_pesos = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_pesos)

    plt.title("Visualización del Grafo")
    plt.show()

dibujar_grafo(cargar_csv('Prueba.csv'))