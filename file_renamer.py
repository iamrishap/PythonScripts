import glob
import os
import re

PATH = "C:\\Users\\Administrator\\Desktop\\W5\\"
list_of_files = glob.glob(PATH + "*.*")
sorted_latest_list_of_files = sorted(list_of_files, key=os.path.getmtime)
i = 1
for file in sorted_latest_list_of_files:
    filename = file.split('\\')[-1]
    print(filename)
    filename = re.sub(r"^(m101 [0-9 ]*)?", "", filename).replace(' - YouTube', '')
    print(PATH + str(i) + '. ' + filename.capitalize())
    os.rename(file, PATH + str(i) + '. ' + filename.capitalize())
    i += 1
#print(sorted_latest_list_of_files)
#os.rename(latest_file, 'Sydney.txt')
#print(latest_file)
