import matplotlib.pyplot as plt

def grafica(label_final,value_final):
  fig,ax = plt.subplots()
  ax.bar(label_final,value_final,color=['g','g','b','b','y','y','r','r'])
  ax.set_title('Cambio de poblacion de paises en decadas')
  ax.set_ylabel('Poblacion')
  ax.set_xlabel('Años')
  plt.show()

def gra_pastel(eti, val):
  fig,ax1 =plt.subplots()
  ax1.pie(val, labels=eti)
  ax1.axis('equal')
  plt.title('Porcentaje de poblacion mundial')
  plt.show()


  
if __name__ == '__main__':
  grafica(label_final,value_final)
  gra_pastel(eti,val)