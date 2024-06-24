import matplotlib.pyplot as plt

def bar_chart(name,labels,values):
  #Se idica la extructura en esta caso figura y eje
  fig, ax = plt.subplots()
  #Se indican los ejes y el tipo de grafico
  ax.bar(labels,values) 
  #Se muestra la grafica
  plt.savefig(f'./imgs/bc_{name}.png')
  plt.close()
  

def pie_chart(name,labels,values):
  #Se indica la estrucrura de la figura
  fig, ax = plt.subplots()
  #Se indica el eje el tipo de grafico
  ax.pie(values,labels = labels)
  #Se centra el eje
  ax.axies=('equal')
  #Se muestra la gráfica
  plt.savefig(f'./imgs/pc_{name}.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a','b','c']
  values = [100,200,300]
  print(bar_chart(name,labels,values))