import os
import re
import glob
import pandas as pd


data_dir = '../00-Data/csv_data/'
def csv_convert_feather(data_dir):
    data_dir_glob = data_dir + "*.csv"
    
    if not os.path.exists('../00-Data/feather_data'):
        os.makedirs('../00-Data/feather_data')

    for file in glob.glob(data_dir_glob):
        data = pd.read_csv(file)
        data.to_feather('../00-Data/feather_data/' + re.findall('\w+', file)[3] + '.feather')
        
csv_convert_feather(data_dir)
