import os


os.makedirs(os.path.join('..', 'data'), exist_ok=True) #创建一个data目录
data_file = os.path.join('..', 'data', 'house_tiny.csv') #定义路径（house_tiny.csv）csv means columns separated
with open(data_file, 'w') as f:                          #open the files , f represent its name
    f.write('NumRooms,Alley,Price\n')                    # 列名
    f.write('NA,Pave,127500\n')                          # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

import pandas as pd

data = pd.read_csv(data_file)
print(data)