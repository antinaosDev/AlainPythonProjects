import read_csv
import matplotlib.pyplot as plt
import os
import Chart
import Risk_per_region
import Risk_per_town
import Risk_per_year
import risk_year_region_com

def run():
    data = read_csv.read_csv('agro_emergency.csv')
    data_year = Risk_per_year.risk_year(data)
    year_list = sorted(data_year['Año'].unique().tolist(),reverse=False)
    data_region = Risk_per_region.risk_region(data)
    region_list = sorted(data_region['Region'].unique().tolist(),reverse=False)
    data_comuna,comuna_list = Risk_per_town.risk_comuna(data,'IX')
    
    
    print('*'*90)
    print('Bienvenido al programa que genera datos estadísticos sobre riesgos agroclimaticos')
    print('*'*90)
    
    choice = ('Y','N')
    consulta = input('Quieres realizar un analisis por año? (y/n): ').upper().strip()
    
    while consulta not in choice:
        print('Ingrese una opción válida \n')
        consulta = input('Quieres realizar un analisis por año? (y/n): ').upper().strip()
    else:
        if consulta == 'Y':
            print(f'La lista de años es: {year_list}')
            consulta = int(input('Indique el año a consultar: '))
            
            while consulta not in year_list:
                print('Ingrese una opción válida \n')
                print(f'La lista de años es: {year_list}')
                consulta = int(input('Indique el año a consultar: '))
            else:
                year = data_year[data_year['Año'] == consulta] 
                labels = year['Sit'].tolist()
                values = year['count_sit_year'].tolist()
                df = year[['Sit','count_sit_year']]
                print(df)
                Chart.bar_chart(labels,values,consulta)
                
            
        else:
            consulta = input('Quieres realizar un analisis historico por región? (y/n): ').upper().strip()
            
            while consulta not in choice:
                print('Ingrese una opción válida \n')
                consulta = input('Quieres realizar un analisis historico por región? (y/n): ').upper().strip()
            else:
                if consulta == 'Y':
                    print(f'La lista de regiones es: {region_list}')
                    consulta = input('Indique la región a consultar: ')
                    
                    while consulta not in region_list:
                        print('Ingrese una opción válida \n')
                        print(f'La lista de regiones es: {region_list}')
                        consulta = input('Indique la región a consultar: ')
                    else:
                        region = data_region[data_region['Region'] == consulta]
                        labels = region['Sit'].tolist()
                        values = region['count_sit_r'].tolist()
                        df = region[['Sit','count_sit_r']]
                        print(df)
                        Chart.bar_chart(labels,values,consulta)
                    
                else:
                    consulta = input('Quieres realizar un analisis anual por región? (y/n): ').upper().strip()
                    
                    while consulta not in choice:
                        print('Ingrese una opción válida \n')
                        consulta = input('Quieres realizar un analisis anual por región? (y/n): ').upper().strip()
                    else:
                        if consulta == 'Y':
                            print(f'La lista de años es: {year_list}')
                            consulta_año = int(input('Indique el año a consultar: '))
                            print(f'La lista de regiones es: {region_list}')
                            consulta_r = input('Indique la región a consultar: ')
                            
                            while consulta_año not in year_list or consulta_r not in region_list:
                                print('Ingrese opciones válidas \n')
                                print(f'La lista de años es: {year_list}')
                                consulta_año = int(input('Indique el año a consultar: '))
                                print(f'La lista de regiones es: {region_list}')
                                consulta_r = input('Indique la región a consultar: ')
                            else:
                                filter_year_region,filter_y_r_comuna,list = risk_year_region_com.comb_risk(data,consulta_año,consulta_r,'Cholchol')
                                labels = filter_year_region['Sit'].tolist()
                                values = filter_year_region['count'].tolist()
                                df = filter_year_region[['Region','Año','Sit','count']]
                                print(df)
                                Chart.bar_chart(labels,values,consulta_r)
                    
                        
                        else:
                            consulta = input('Quieres realizar un analisis por comuna? (y/n): ').upper().strip()
                            
                            while consulta not in choice:
                                print('Ingrese una opción válida \n')
                                consulta = input('Quieres realizar un analisis historico por comuna? (y/n): ').upper().strip()
                            else:
                                if consulta == 'Y':
                                    print(f'La lista de regiones es: {region_list}')
                                    consulta_r = input('Indique la región de la comuna a consultar: ')
                                    comuna_bd,lista_c = Risk_per_town.risk_comuna(data,consulta_r)
                                    print(f'La lista de comunas es: {lista_c}')
                                    consulta = input('Indique la comuna a consultar: ')
                                    
                                    while consulta_r not in region_list or consulta not in lista_c:
                                        print('Ingrese una opción válida \n')
                                        print(f'La lista de regiones es: {region_list}')
                                        consulta_r = input('Indique la región de la comuna a consultar: ')
                                        comuna,lista_c = Risk_per_town.risk_comuna(data,consulta_r)
                                        print(f'La lista de comunas es: {lista_c}')
                                        consulta = input('Indique la comuna a consultar: ')
                                    else:
                                        comuna = comuna_bd[comuna_bd['Comuna'] == consulta]
                                        labels = comuna['Sit'].tolist()
                                        values = comuna['count_sit_comuna'].tolist()
                                        df = comuna[['Sit','count_sit_comuna']]
                                        print(df)
                                        Chart.bar_chart(labels,values,consulta)
                                        
                                else:
                                    consulta = input('Quieres realizar un analisis anual por comuna? (y/n): ').upper().strip()
                                    
                                    while consulta not in choice:
                                        print('Ingrese una opción válida \n')
                                        consulta = input('Quieres realizar un analisis anual por comuna? (y/n): ').upper().strip()
                                    else:
                                        if consulta == 'Y':
                                            print(f'La lista de años es: {year_list}')
                                            consulta_año = int(input('Indique el año a consultar: '))
                                            lista_comuna = sorted(data['Comuna'].unique().tolist(),reverse=False)
                                            print(f'La lista de comunas es: {lista_comuna}')
                                            consulta = input('Indique la comuna a consultar: ')
                                            
                                            while consulta not in lista_comuna or consulta_año not in year_list:
                                                print('Ingrese una opción válida \n')
                                                print(f'La lista de años es: {year_list}')
                                                consulta_año = int(input('Indique el año a consultar: '))
                                                lista_comuna = sorted(data['Comuna'].unique().tolist(),reverse=False)
                                                print(f'La lista de comunas es: {lista_comuna}')
                                                consulta = input('Indique la comuna a consultar: ')
                                            else:
                                                filter_year_region,filter_y_r_comuna,list = risk_year_region_com.comb_risk(data,consulta_año,'IX',consulta)
                                                labels = filter_y_r_comuna['Sit'].tolist()
                                                values = filter_y_r_comuna['count'].tolist()
                                                df = filter_y_r_comuna[['Comuna','Año','Sit','count']]
                                                print(df)
                                                Chart.bar_chart(labels,values,consulta)
                                        
                                        else:
                                            return 'Gracias por utilizar el software'
                                                
                                    
                                            
                                        
                                        
if __name__ == '__main__':
    print(run())
    