import os
from shutil import copyfile

folder = '/data/sandbox/sandbox_black_report'
targetFolder = '/home/cindy/cuckooml/sample_data/five_hundred_test/'
if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

i = 0
for item in os.listdir(folder):
    if i > 500:
        break
    cur = folder + item
    print(cur)
    copyfile(cur, targetFolder + item)
    i += 1