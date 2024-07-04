import pandas as pd
import read_csv

def risk_comuna(data,region):
    data_r = data[data['Region'] == region]
    data_comuna = data_r.groupby(['Comuna','Sit']).agg({'Sit':'count'})
    data_comuna = data_comuna.rename(columns = {'Sit':'count_sit_comuna'}).reset_index().sort_values('count_sit_comuna',ascending = False)
    
    comuna_list = sorted(data_r['Comuna'].unique().tolist(),reverse=False)
    
    return data_comuna,comuna_list  


if __name__ == '__main__':
    data = read_csv.read_csv('agro_emergency.csv')
    comuna= risk_comuna(data,'IX')
    print(comuna)