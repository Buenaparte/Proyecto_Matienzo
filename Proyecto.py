from validations import cargar_csv, cargar_visa, dijkstra

def main():
    grafo = cargar_csv('Prueba.csv')
    lista_visa= cargar_visa('Visa.csv')
    visa = bool
    print("Bienvenido al programa de rutas aéreas: \nLos aeropuertos disponibles son: \n")
    for pais in lista_visa:
        print(f"{pais[0]} - {pais[1]} - { 'Requiere Visa' if pais[2] else 'No requiere Visa' }")
    print("\n")

    # Revisión de origen
    while True:
        origen = input("Coloque el código del aeropuerto de origen:  \n> ")
        origen = origen.upper()  
        if origen in grafo:
            break
        else:
            print("Código no encontrado")
   

    #Revisión de destino
    while True:
        destino = input("Coloque el código del aeropuerto de destino:  \n> ")
        destino = destino.upper()
        if destino in grafo:
            break
        else:
            print("Código no encontrado")

    #Revisión de visa
    while True:
        visa = input("¿Posee visa? \n1- Sí \n2- No \n> ") 
        if visa == "1":
            visa = True
            break
        elif visa == "2":
            visa = False
            break
        else:
            print("Opción no válida")

    #Se revisa que el destino sea alcanzable sin visa, si no lo es se termina el programa
    for i in lista_visa:
        if i[0] == destino and visa == False and i[2] == True:
            print("No se puede viajar a ese destino sin visa")
            return  # Termina el programa si el destino no es alcanzable sin visa

    #Revisión de consulta
    while True:
           
        consulta = input("Coloque: \n1- si desea el menor precio posible \n2- si desea el menor tiempo posible \n> ")
        if consulta == "1":
            print("Menor precio: ")
            print(dijkstra("precio", grafo, origen, destino, lista_visa, visa))
            break
        elif consulta == "2":
            print("Menos escalas: ")
            print(dijkstra("escalas", grafo, origen, destino, lista_visa, visa))
            break
        else:
            print("Opción no válida")

main()