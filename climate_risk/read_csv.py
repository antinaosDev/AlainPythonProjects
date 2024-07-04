import pandas as pd


def read_csv(path):
    #Se realiza la lectura del csv
    data = pd.read_csv(path,encoding='latin-1',sep=';')
    
    return data

if __name__ == '__main__':
    data = read_csv('agro_emergency.csv')
    print(data)