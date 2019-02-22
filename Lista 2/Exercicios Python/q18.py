import sys
import random
import os
import datetime
 
date_str = input(': ')
format_str = '%d/%m/%Y' 
datetime_obj = datetime.datetime.strptime(date_str, format_str)
 
print(datetime_obj.strftime("%d/%m/%Y"))

os.system('pause')