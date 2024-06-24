import read_csv

def population(func,pais):
  #Se define la longitud del documento para iterar en cada elemento
  lenght = len(func)
  #Se creará un diccionario que almacena pais como clave y poblacion como valores
  dict_country = {}

  #Se itera sobre cada elemento para obtener los valores para el diccionario
  for index in range(lenght):
    #Se obtiene el primer pais de la lista de diccionarios
    country = func[index]['Country']
    #Se obtiene un diccionario con el elemento de cada fila de poblacion 
    dict_population = {}
    
    #Se obtiene la poblacion de cada año de cada elemento
    dict_population['1970'] = int(func[index]['1970 Population'])
    dict_population['1980'] = int(func[index]['1980 Population'])
    dict_population['1990'] = int(func[index]['1990 Population'])
    dict_population['2000'] = int(func[index]['2000 Population'])
    dict_population['2010'] = int(func[index]['2010 Population'])
    dict_population['2015'] = int(func[index]['2015 Population'])
    dict_population['2020'] = int(func[index]['2020 Population'])
    dict_population['2022'] = int(func[index]['2022 Population'])

    #Se va ingresando cada pais con el valor de su diccionario
    dict_country[country] = dict_population

  #Se obtienen los valores para poder graficar
  labels = list(dict_country[pais].keys())
  values = list(dict_country[pais].values())

  return labels, values
    


def growth_perc(func):
  #Se define la longitud del documento para iterar en cada elemento
  lenght = len(func)
  #Se obtiene un diccionario que contendrá el pais y su porcentaje de crecimiento
  dict_world_per = {}
  #Se genera una iteración de los elementos
  for index in range(lenght):
    #Se obtiene el pais
    country = func[index]['Country']
    #Se obtiene el porcentaje de crecimiento
    growth_country = float(func[index]['World Population Percentage'])

    #Se ingrese la info de pais y porcentaje de crecimiento al diccionario
    dict_world_per[country] = growth_country

  #Se obtienen los valores para poder graficar
  labels = list(dict_world_per.keys())
  values = list(dict_world_per.values())

  return labels,values



if __name__ == '__main__':
  func = read_csv.read_csv('./project_data_population/data_pop.csv')
  print(population(func,'Chile'))