import read_csv
import pandas as pd 

def risk_region(data):
    
    # Agrupamos por 'Region' y 'Sit' y contamos las ocurrencias
    data_region = data.groupby(['Region', 'Sit']).agg({'Sit': 'count'})
    data_region = data_region.rename(columns={'Sit': 'count_sit_r'}).reset_index().sort_values('count_sit_r',ascending = False)  
   
    return data_region


if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    region = risk_region(data)
    print(region)