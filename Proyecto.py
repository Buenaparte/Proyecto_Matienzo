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

def dijkstra_menos_viajes(origen, destino, lista_guardada):
 lista = []
 ruta = []
 finalizar = False
 ruta.append(origen)
 for i in lista_guardada:
        if i[0] == origen:
         lista.append(i)
 while True:
     for i in lista:
            #print("linea 28")
            if i[1] == destino:
             ruta.append(i[1])
             finalizar = True
             break
     if finalizar:
         break 
     lista2 = []
     for i in lista:
         for j in lista_guardada:
             if j[0] == i[1] or j[1] == i[1]:
                 #print(j)
                 if j[1] == destino:
                        #print("linea 37")
                        ruta.append(j[0])
                        ruta.append(j[1])
                        finalizar = True
                        break
                 if j[0] == destino:
                        #print("linea 37")
                        ruta.append(j[1])
                        ruta.append(j[0])
                        finalizar = True
                        break 
                 lista2.append(j)
     
         if finalizar:
             break
     lista = lista2
     if finalizar:
         break
 print("La ruta con menos viajes es: ")
 print(ruta)

def main():
 Lista_Guardada = Guardar_csv()
 #print(Lista_Guardada)
 while True:
     x = input("Coloque el codigo del aeropuerto de origen:  \n")
     listo = False
     x = x.upper()  
     for i in Lista_Guardada:
         if x in i:
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
         if y in i:
             listo = True
             break
     if listo:
         break
     else:
         print("Codigo no valido")
 while True:
     z = input("Coloque: \n1- si desea el menor precio posible, \n2- si desea el menor tiempo posible \n")
     listo = False
     if z == "1":
         print("El menor precio posible es: ")
         listo = True
     elif z == "2":
         dijkstra_menos_viajes(x, y, Lista_Guardada)
         listo = True
     else:
          print("Opcion no valida")
     if listo:
          break

main()