def cargar_csv(archivo: str) -> dict:
    grafo = {}
    with open(archivo, mode='r', encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas[1:]:  # Saltar la primera línea (encabezado)
            origen, destino, precio = linea.strip().split(';')
            precio = int(precio)
            if origen not in grafo:
                grafo[origen] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[origen][destino]= precio
            grafo[destino][origen]= precio
    return grafo

def cargar_visa(archivo: str) -> list:
    lista_visa = []
    with open(archivo, mode='r', encoding='utf-8') as f:
        lineas = f.readlines()
        for linea in lineas[1:]:  # Saltar la primera línea (encabezado)
            codigo, nombre, visa_requerida = linea.strip().split(';')
            if visa_requerida.lower() == 'requiere visa':
                visa_requerida = True
            else:
                visa_requerida = False
            lista_visa.append((codigo, nombre, visa_requerida))
    #print(lista_visa)
    return lista_visa

def dijkstra(tipo: str, grafo: dict, inicio: str, destino: str, lista_visa: list, visa: bool) -> tuple:

    nodos_con_visa = {pais[0] for pais in lista_visa if pais[2]}  # Crear un conjunto de códigos de países que requieren visa

    distancia = {}
    for nodo in grafo:
        distancia[nodo] = float('inf')
    padres = {}
    for nodo in grafo:
        padres[nodo] = None
    visitados = set()
    distancia[inicio] = 0
    
    while len(visitados) < len(grafo):
        # Encontrar el nodo no visitado con la distancia más pequeña
        nodo_actual = None
        for nodo in grafo:
            if nodo not in visitados:
                if nodo_actual is None or distancia[nodo] < distancia[nodo_actual]:
                    nodo_actual = nodo

        # Si la distancia mínima es infinito, el resto de nodos son inalcanzables
        if nodo_actual is None or distancia[nodo_actual] == float('inf'):
            break

        if nodo_actual == destino:
            break

        visitados.add(nodo_actual)

        # Explorar vecinos
        for vecino, peso in grafo.get(nodo_actual, {}).items():
            if vecino in nodos_con_visa and not visa:
                print(f"No se puede viajar a {vecino} sin tarjeta Visa")
                continue  # Si el vecino requiere visa y no se tiene, saltar'
            if tipo == "escalas":
                peso = 1  # Para minimizar escalas, cada arista tiene peso 1
            if vecino in visitados:
                continue
            camino = distancia[nodo_actual] + peso
            if camino < distancia[vecino]:
                distancia[vecino] = camino
                padres[vecino] = nodo_actual

    # Reconstrucción de la ruta
    ruta = []
    actual = destino
    if distancia[destino] == float('inf'):
        print("No hay ruta disponible")
        return [], float('inf') 
    else:
        while actual is not None:
            ruta.insert(0, actual)
            actual = padres[actual]
         
    print("La ruta óptima es:")
    print(" -> ".join(ruta))
    return ruta, distancia[destino]