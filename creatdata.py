import os
import time
import json
from openpyxl import Workbook
from openpyxl import load_workbook

# DEF
# Output directory
save_dir = r'/mnt/d/Py_prj/xtDataFake/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

test_dict = {'one':1, 'two':2}
print(test_dict)
print(type(test_dict))

time_start = time.time() # Start time mark
with open(save_dir+'record.json',"w") as f:
    json.dump(test_dict,f)
    print("加载入文件完成...")

