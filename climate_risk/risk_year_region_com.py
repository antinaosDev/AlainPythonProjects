import pandas as pd 
import read_csv

def comb_risk(data,year,region,comuna):
    
    df_dates = pd.to_datetime(data['Fecha'],format='%d-%m-%Y')
    df_years = df_dates.dt.year
    data['Año'] = df_years
    
    #Se realiza filtro por año y Región
    filter_year_region = data[(data['Año'] == year) & (data['Region'] == region)]
    filter_year = filter_year_region.groupby(['Region','Año','Sit']).agg({'Sit':'count'})
    filter_year= filter_year.rename(columns = {'Sit':'count'}).reset_index().sort_values('count',ascending = False)
  
    
    #Se filtra por año y comuna
    filter_year_region_comuna = data[(data['Año'] == year) & (data['Comuna'] == comuna)]
    filter_comuna = filter_year_region_comuna.groupby(['Comuna','Año','Sit']).agg({'Sit':'count'})
    filter_comuna = filter_comuna.rename(columns = {'Sit':'count'}).reset_index().sort_values('count',ascending = False)
    lista_com = sorted(filter_comuna['Comuna'].unique().tolist(),reverse=False)
  
    
    
    
    return filter_year,filter_comuna,lista_com
    
       

if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    comb = comb_risk(data,2012,'IX','Cholchol')
    print(comb)