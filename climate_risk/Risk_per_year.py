import pandas as pd
import read_csv

def risk_year(data):
    df_dates = pd.to_datetime(data['Fecha'],format='%d-%m-%Y')
    df_years = df_dates.dt.year
    data['Año'] = df_years
    
    data_year = data.groupby(['Año','Sit']).agg({'Sit':'count'})
    data_year = data_year.rename(columns = {'Sit':'count_sit_year'}).reset_index().sort_values('count_sit_year',ascending = False) 
  
    return data_year


if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    year = risk_year(data)
    print(year) 