import charts
import country_pop
import read_csv


def run_bar_chart():
  #Se realiza la lectura del documento
  data = read_csv.read_csv('data_pop.csv')

  #Se le consulta al usuario por el pais a consultar
  question = input('Ingrese el pais que desea consultar: ')

  #Se obtiene la poblacion por cada pais
  country, population = country_pop.population(data,question)
  
  #Se obtiene la gráfica de crecimiento del pais consultado
  return charts.bar_chart(question,country,population)


def run_pie_chart():
  #Se realiza la lectura del documento
  data = read_csv.read_csv('data_pop.csv')
  
  #Se genera un filtro por continente
  filtrado = []
  longitud = len(data)
  continente = input('Ingrese un continente: ')
  for row in range(longitud):
    if data[row]['Continent'] != continente:
      continue
    else:
      filtrado.append(data[row])
    
  #Se obtiene la tasa de crecimiento de los paises
  country, growth = country_pop.growth_perc(filtrado)

  #Se obtiene la gráfica de crecimiento del pais consultado
  return charts.pie_chart(continente,country,growth)

if __name__ == '__main__':
  print(run_bar_chart())
  print(run_pie_chart())

