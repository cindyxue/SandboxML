import os
from shutil import copyfile

folder = '/data/sandbox/cuckoo_reports/'
targetFolder = '/home/cindy/cuckooml/sample_data/'
f = 'black_1/'
if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

i = 0
cnt = 1
for item in os.listdir(folder):
    if i > 500:
        cnt += 1
        f = 'black_' + str(cnt) + '/'
        i = 0
    cur = folder + item
    print(cur)
    # copyfile(cur, targetFolder + f + item)
    i += 1