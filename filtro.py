#Seleccion de pais por entrada input
def pais(lista,country):
  paises = list(filter(lambda x:x['Country'] == country, lista))
  return paises[0]

#Filtro de seleccion solo de poblacion
def solo_poblacion(poblaciones):
  filtro_poblacion = dict(filter(lambda y:'Population' in y[0] and not 'World Population Percentage' in y[0], poblaciones.items()))
  return filtro_poblacion


  
#seleccion de continente input-----
def continente (lista,continente):
  #Filtar todos los continentes por seleccion
  filtro_continente =list(filter(lambda x:x['Continent'] == continente,lista))
  return filtro_continente

  
  #Seleccion de porcentajes------
def porcentaje(seleccion):
  #tomar los porcentajes de ese continente
  por = list(map(lambda z:z['World Population Percentage'],seleccion))
  #Tomar todos los paises de ese continente
  Pa = list(map(lambda z:z['Country'],seleccion))

  union = dict(zip(por,Pa))
  union.items()
  return union


  




  
  