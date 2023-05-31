import os
import time
import json
from openpyxl import Workbook
from openpyxl import load_workbook

file_dir = '/mnt/d/Py_prj/xtData/'
file_list = os.listdir(file_dir)
# print(file_list)
# print(type(file_list))
time_start = time.time()
try:
    wbr = load_workbook(file_dir+file_list[0])
except FileNotFoundError:
    print("File_%s not found!" %(file_list[0]))
else:
    wsr = wbr.active
    time_1 = time.time()
    print("Open %s Pasted time %.3f s" %(file_list[0], time_1-time_start))
    for row in wsr.iter_rows(values_only=True):
        for cell in row:
            cell_dict = json.loads(cell)
            print(cell_dict['first_connect_time'])
    time_2 = time.time()
    print("Pasted time %.3f s" %(time_2-time_1))
