import pandas as pd
import glob


import os
data_dir = '00-Data/csv_data'
def csv_convert_feather(data_dir):
    data_dir += "/*.csv"
    
    if not os.path.exists('00-Data/feather_data'):
        os.makedirs('00-Data/feather_data')

    for file in glob.glob(data_dir):
        #data = pd.read_csv(file)
        #data.to_feather('00-Data/feather_data' + re.findall('\w+', file)[3] + '.feather')
        data_str = re.findall('\w+', file)[3]

        print(file)
        
csv_convert_feather(data_dir)


import re


string = '00-Data\cliente_tabla.csv'
data_str = re.findall('(.*)\.', string)
data_str


'00-Data\\cliente_tabla'


data


string = '00-Data/csv_data/cliente_tabla.csv'
data = pd.read_csv(string)


data.head()


data.to_feather('00-Data/csv_data\cliente_tabla.csv')







