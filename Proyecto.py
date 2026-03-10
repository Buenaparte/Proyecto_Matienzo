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

def main():
 Lista_Guardada = Guardar_csv()
 #print(Lista_Guardada)
 #x = input("Coloque el codigo del aeropuerto de origen:  \n")
 #y = input("Coloque el codigo del aeropuerto de destino:  \n")
 #z = input("Coloque: \n1- si desea el menor precio posible, \n2- si desea el menor tiempo posible \n")
 #if z == "1":
     #print("El menor precio posible es: ")
 #elif z == "2":
     #print("El menor tiempo posible es: ")
 #else:
     #print("Opcion no valida")
