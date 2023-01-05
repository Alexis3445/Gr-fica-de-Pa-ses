import lectura
import filtro
import grafica

def run():
  lista = lectura.lectura('./Data.csv') #Primeramente se obtiene la obtencion de los datos generales-
  
  #------------------Variables para grafica de poblacion--------------------------------
  country_1 = input('Seleccione país para graficar: ') #seleccion del país.
  country = '' 
  
  for n in country_1.split():
    country += n[0].upper() + n[1:] #Hacer que el pais se tome aunque sea minusculas
  
  poblaciones = filtro.pais(lista,country) #La poblacion se filtrada se selecciona despues de seleccionar al país.    
  #Formula el diccionario  del resultado
  resultado = filtro.solo_poblacion(poblaciones)
  #del resultado se obtiene la clave valor
  label = resultado.keys()
  value = resultado.values()
  #Se limpia el dato de la poblacion para que queden solo los años en formato str
  label_final = list(map(lambda x: x.replace(' Population', ''),label))
  #Se colcoan los valores en tipo entero
  value_final = [int(y) for y in value] 
  
  
  #----------------Variables para grafica de % poblacion --------------------------------
  continente_1 = input("Escriba el continente para saber el porcentaje de poblacion de cada pais: ")
  continente = '' 
  for n in continente_1.split():
    continente += n[0].upper() + n[1:]
  seleccion= filtro.continente(lista,continente)
  resultado_2= filtro.porcentaje(seleccion)
  #Se obtinenen la clave valor de cada item
  eti = list(resultado_2.values())
  val= list(resultado_2.keys())
  #Se limpia el dato ara que sea entero
  val_final = [float(n) for n in val]
  
  #--------------------PORCESO PARA GRAFICAR--------------------------------
  
  if len(country) >0:
    chose = input('Seleccione 1 para graficar pais \nSeleccione 2 para graficar el porcentaje: ')
    if chose == '1':
   #Se acciona la funcion de la grafica
      grafica.grafica(label_final,value_final)
    
    elif chose == '2':
      grafica.gra_pastel(eti,val_final)
    else:
      print('seleccione 1 o 2')
    
  else:
    print('Escriba un país por favor')
  
  
  
if __name__ == '__main__':
  run()