import os
import time
import pandas as pd

# DEF
# Input directory
file_dir = r'/mnt/d/Py_prj/xtDataOut/'
# Output directory
save_dir = r'/mnt/d/Py_prj/xtDataOut2/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

file_list = os.listdir(file_dir) # File list
file_num = len(file_list) # File number
time_start = time.time() # Start time mark

for n in  range(file_num):
    df = pd.read_excel(io=file_dir+file_list[n], sheet_name=0, header=None, names=['sn','vers','time','vsol','soc','tempb','temp'])
    sn_list = df.sn.unique()
    sn_num = len(sn_list)

    for i in range(sn_num):
        if os.path.exists(save_dir+sn_list[i]+".csv"):
            data_save = df[df['sn'] == sn_list[i]]
            data_save.to_csv(save_dir+sn_list[i]+".csv", mode='a', sep=',', header=False, index=False)
            print(sn_list[i]+' saved')
        else:
            data_save = df[df['sn'] == sn_list[i]]
            data_save.to_csv(save_dir+sn_list[i]+".csv", sep=',', index=False)
            print(sn_list[i]+' created')