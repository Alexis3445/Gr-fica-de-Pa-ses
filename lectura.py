import csv

def lectura(path):
  with open (path, 'r') as lectura:
    lector = csv.reader(lectura, delimiter = ',')
    lista =[]
    columna = next(lector) # Se posiciona en la primera columna
    for fila in lector:
      diccionario = dict(zip(columna,fila))
      lista.append(diccionario)
    #print(lista[0])
    return(lista)

if __name__ == '__main__':
  lectura('./Data.csv')
  
      
