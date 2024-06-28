def read_csv(path):
    import csv
    with open(path,'r',encoding='latin-1') as csv_file:
        read = csv.reader(csv_file,delimiter=';')
        header = next(read)
        data_list = []
        
        for row in read:
            iterable = zip(header,row)
            dict = {key:value for key,value in iterable}
            data_list.append(dict)
            
    return data_list

if __name__ == '__main__':
    data = read_csv('agro_emergency.csv')
    print(data)
