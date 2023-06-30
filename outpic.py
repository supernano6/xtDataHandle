import os
import time
import pandas as pd
import matplotlib.pyplot as plt

# DEF
# Input directory
file_dir = r'/mnt/d/Py_prj/xtDataOut2/'
# Output directory
save_dir = r'/mnt/d/Py_prj/xtDataOut3/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

file_list = os.listdir(file_dir) # File list
file_num = len(file_list) # File number
time_start = time.time() # Start time mark

for n in  range(file_num):
    df = pd.read_csv(file_dir+file_list[n])
    fig = df.iloc[:, 3:5].plot()
    fig.figure.savefig(save_dir+file_list[n][:-4]+".png")
    plt.close()