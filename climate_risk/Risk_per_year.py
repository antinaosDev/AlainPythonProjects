import Risk_per_region
import read_csv

def risk_year(func_reg,year_c):
    var1,var2,var3,format,var5 = func_reg

    length = len(format)
    riesgos = []
    
    list_year = []
    
    for i in range(length):
        year = format[i]['Año']
        list_year.append(year)
        
    
    for i in range(length):
        riesgo  = format[i]['Sit']
        year = format[i]['Año']
        if year == year_c:
            riesgos.append(riesgo)
    
    lista_riesgos = set(riesgos)
    contador = 0
    dict_inc = {}

    for j in range(length):
        riesgo  = format[j]['Sit']
        year = format[j]['Año']
        if riesgo in lista_riesgos and year == year_c:
            contador +=1
            dict_inc[riesgo] = contador
        
    lables = dict_inc.keys()
    values = dict_inc.values()
    
    return lables,values,list(set(list_year))

if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    region = Risk_per_region.risk_region(data,'IX')
    year = risk_year(region,2008)
    print(year)