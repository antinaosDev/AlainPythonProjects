import Risk_per_region
import read_csv

def risk_town(func_reg,comuna_c):
    var1,var2,region,var3,var4 = func_reg
    
    length_region = len(list(region))
    
    lista_comunas = []
    for i in range(length_region):
         comuna = region[i]['Comuna']
         lista_comunas.append(comuna)
        
    riesgos = []
    for i in range(length_region):
        riesgo  = region[i]['Sit']
        comuna = region[i]['Comuna']
        if comuna == comuna_c:
            riesgos.append(riesgo)

    
    contador = 0
    dict_inc = {}
    for j in range(length_region):
        riesgo  = region[j]['Sit']
        comuna = region[j]['Comuna']
        if comuna == comuna_c and riesgo in riesgos:
            contador += 1
            dict_inc[riesgo] = contador
        
        
    lables = dict_inc.keys()
    values = dict_inc.values()
    comunas = list(set(lista_comunas))
    
    return lables,values,comunas

if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    region = Risk_per_region.risk_region(data,'IX')
    comuna = risk_town(region,'Cholchol')
    print(comuna)