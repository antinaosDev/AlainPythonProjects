import read_csv
import Chart
import Risk_per_region
import Risk_per_town
import Risk_per_year

def run():
    data = read_csv.read_csv('agro_emergency.csv')
    c_año = input('Quieres consultar los riesgos de un año en especifico (y/n): ').upper().strip()
    region = Risk_per_region.risk_region(data,'IX')
    
    if c_año == 'Y':
        var1,var2,lista_años = Risk_per_year.risk_year(region,2010)
        print('Los meses son los siguientes:',sorted(lista_años,reverse=False))
        año = int(input('Ingrese el año a analizar: '))
        
        labels,Values,lista_años = Risk_per_year.risk_year(region,año)
        datos = list(zip(labels,Values))
        print('\nAño analizado:',año)
        print('-'*25)
        for i in range(len(datos)):
            print(datos[i])
        print('-'*25)
        
        Chart.bar_chart(labels,Values,año)
    
    else:
        c_region = input('\nQuieres consultar los registros de alguna region? (y/n): ').upper().strip()
        
        if c_region == 'Y':
            var1,var2,var3,var4,lista_regiones = region
            print('\nlas Regiones son las siguientes:',sorted(lista_regiones,reverse=False))
            region_S = input('\nIngrese la region a analizar: ').upper().strip()
            labels_r,values_r,var3,var4,var5 = Risk_per_region.risk_region(data,region_S)
            datos_r = list(zip(labels_r,values_r))
            
            print('\nRegión analizada:',region_S)
            print('-'*25)
            for i in range(len(datos_r)):
                print(datos_r[i])
            print('-'*25)
            
            Chart.bar_chart(labels_r,values_r,region_S)
            
            
            c_town = input(f'\nQuieres consultar los registros alguna comuna de la región {region_S}? (y/n): ').upper().strip()
            
            if c_town == 'Y':
                var1,var2,comunas = Risk_per_town.risk_town(Risk_per_region.risk_region(data,region_S),'Cholchol')
                print('\nlas Comunas son las siguientes:',comunas)  
                comuna_t = input('\nIngrese la comuna a analizar: ')
                labels_t,values_t,var3 = Risk_per_town.risk_town(Risk_per_region.risk_region(data,region_S),comuna_t)
                datos_t = list(zip(labels_t,values_t))
                print('\nComuna analizada:',comuna_t)
                print('-'*25)
                for i in range(len(datos_t)):
                    print(datos_t[i])
                print('-'*25)
                
                Chart.bar_chart(labels_t,values_t,comuna_t)
                    
            else:
                return 'Se cierra programa'
        else:
            return 'Se cierra programa'
    

    
        
if __name__ == '__main__':
    print(run())
    