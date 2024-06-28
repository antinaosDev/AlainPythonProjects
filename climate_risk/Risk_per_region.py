import read_csv

def risk_region(data,reg):
    from datetime import datetime
    
    length = len(data)
    dict_region = {}
    dict_format = []
    
    
    for i in range(length):
        region = data[i]['Region']
        
        fecha = data[i]['Fecha']
        fecha_obj = datetime.strptime(fecha,"%d-%m-%Y")
        year = fecha_obj.year
        
        dict_values = {}
        
        #dict_values['Region'] = data[i]['Region']
        dict_values['Provincia'] = data[i]['Provincia']
        dict_values['Comuna'] = data[i]['Comuna']
        dict_values['Año'] = year
        dict_values['Sit'] = data[i]['Sit']
        
        dict_format.append(dict_values)
        
        if region not in dict_region:
            dict_region[region] = []
        dict_region[region].append(dict_values)
        
    length_region = len(list(dict_region[reg]))
    riesgos = []
    
    
    for j in range(length_region):
        region_consultada = dict_region[reg]
        situacion = region_consultada[j]['Sit']
        riesgos.append(situacion)
    
    
    lista_riesgos = list(set(riesgos))   
    
 
    dict_inc = {}
    contador_incidentes = 0
    for k in range(length_region):
        region_consultada = dict_region[reg]
        situacion = region_consultada[k]['Sit']
        if situacion in lista_riesgos:
            contador_incidentes += 1
            dict_inc[situacion] = contador_incidentes
    

    labels = dict_inc.keys()
    values = dict_inc.values()
    region = dict_region[reg]
    lista_regiones = list(dict_region.keys())
    
    return labels,values,region,dict_format,lista_regiones

            
    
if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    region = risk_region(data,'IX')
    print(region)