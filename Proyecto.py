def Guardar_csv():
    Lista_Guardada = []
    # Abrir el archivo de forma segura
    with open('Prueba.csv', mode='r', encoding='utf-8') as archivo:
        for fila in archivo:
         datos = fila.strip().split(',')
         for i in datos:
             i = i.split(';')  
             Lista_Guardada.append(i)  
             #print(i)
    Lista_Guardada.pop(0) 
    #print(Lista_Guardada)
    return Lista_Guardada

def Guardar_visa():
    Lista_Guardada = []
    # Abrir el archivo de forma segura
    with open('Visa.csv', mode='r', encoding='utf-8') as archivo:
        for fila in archivo:
         datos = fila.strip().split(',')
         for i in datos:
             i = i.split(';')  
             Lista_Guardada.append(i)  
             #print(i)
    Lista_Guardada.pop(0) 
    #print(Lista_Guardada)
    return Lista_Guardada

def dijkstra_menos_viajes(origen, destino, lista_guardada, lista_visa, visa ):
 lista = [] #se guarda los nodos conectados al origen
 ruta = [] #se guarda la ruta a seguir
 finalizar = False
 no_se_puede_viajar = False
 ruta.append(origen)

 #se revisa que el destino sea alcanzable sin visa, si no lo es se termina el programa
 
 for i in lista_visa:
    if i[0] == destino:
         if visa == False and i[2] == "Requiere Visa":
             no_se_puede_viajar = True
             break
 
 if no_se_puede_viajar:
      return print("No se puede viajar a ese destino sin tarjeta Visa")
 
 #se guarda los nodos conectados al origen en una lista
 for i in lista_guardada:
        if i[0] == origen or i[1] == origen:
         lista.append(i)
 #print(lista)

 #se revisa si el destino esta conectado al origen, si lo esta se termina el programa
 for i in lista:
            #print("linea 28")
            if i[1] == destino:
             ruta.append(i[1])
             finalizar = True
            if i[0] == destino:
             ruta.append(i[0])
             finalizar = True
 
 #se revisa cada uno de los nodos adyacentes al origen
 while True:
     if finalizar:
         break
     #print("bucle") 
     lista2 = []
     for i in lista:
         for k in lista_visa:
                 #se revisa si el destino es accesible sin visa
                 if finalizar:
                     break
                 if k[0] != origen:
                     if k[0] == i[1] or k[0] == i[0]  :
                         print(k)
                         if visa == False and k[2] == "Requiere Visa":
                             a = 0
                         else:
                             for j in lista_guardada:
                                 #se revisa si el nodo esta conectado con el nodo adyacente
                                 if j[0] == i[1] or j[1] == i[1] or j[0] == i[0] or j[1] == i[0]:
                                     #print(j)

                                     #se revisa si es el nodo destino
                                     
                                     if j[1] == destino:
                                         #print("linea 37")
                                         ruta.append(j[0])
                                         ruta.append(j[1])
                                         finalizar = True
                                         break
                                     if j[0] == destino:
                                         #print(j)
                                         #print("linea 39")
                                         ruta.append(j[1])
                                         ruta.append(j[0])
                                         finalizar = True
                                         break 
                                     
                                     #se guarda los nodos adyacentes al nodo adyacente
                                     
                                     lista2.append(j)
                                     #print(lista2)
                         
                                 if finalizar:
                                     break
         if finalizar:
             break
     if finalizar:
         break
 print("La ruta con menos viajes es: ")
 print(ruta)

def main():
 Lista_Guardada = Guardar_csv()
 Lista_Visa = Guardar_visa()
 visa = False
 #print(Lista_Guardada)
 while True:
     x = input("Coloque el codigo del aeropuerto de origen:  \n")
     listo = False
     x = x.upper()  
     for i in Lista_Guardada:
         if x == i[0]:
             listo = True
             break
     if listo:
         break
     else:
         print("Codigo no valido")
 while True:
     y = input("Coloque el codigo del aeropuerto de destino:  \n")
     y = y.upper()
     listo = False
     for i in Lista_Guardada:
         if y == i[1]:
             listo = True
             break
     if listo:
         break
     else:
         print("Codigo no valido")
 while True:
     listo = False
     z = input("Coloque: \n 1- si tiene tarjeta Visa, \n2-  no tiene tarjeta Visa \n") 
     if z == "1":
         visa = True
         listo = True
     elif z == "2":
         listo = True
     else:
          print("Opcion no valida")
     if listo:
          break
 while True:
     z = input("Coloque: \n 1- si desea el menor precio posible, \n2- si desea el menor tiempo posible \n")
     listo = False
     if z == "1":
         print("El menor precio posible es: ")
         listo = True
     elif z == "2":
         dijkstra_menos_viajes(x, y, Lista_Guardada, Lista_Visa, visa)
         listo = True
     else:
          print("Opcion no valida")
     if listo:
          break

main()