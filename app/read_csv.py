def read_csv(path):
  ''' 
  La siguiente funcion lee el archivo y lo guarda en un formato lista de diccionarios para poder operar con el documento.
  '''
  import csv
  
  #Se realiza lectura del archivo
  with open(path) as archivo_csv:
    #Se genera una variable que contendrá el documento
    lector = csv.reader(archivo_csv,delimiter=',')
    #Se obtiene el encabezado de la tabla 
    header = next(lector)
    #Se crea una lista que guardará los valores del documento
    data = []
  
    for row in lector:
      #Se genera union de pares valor encabezado
      union = zip(header,row)
      #Se crea un diccionario elemento por elemento de la variable union
      dict_doc = {key:value for key,value in union}
      #Se añade cada diccionario a la lista data
      data.append(dict_doc)
    return data
      
      
if __name__ == '__main__':
  data = read_csv('./project_data_population/data_pop.csv')
  print(data)