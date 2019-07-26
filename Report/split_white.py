import os
from shutil import copyfile

folder = '/data/sandbox/sandbox_white_report/'
targetFolder = '/home/cindy/cuckooml/sample_data/'
f = 'white_1/'
if not os.path.exists(targetFolder + f):
        os.makedirs(targetFolder + f)

i = 0
cnt = 1
for item in os.listdir(folder):
    if i > 1000:
        cnt += 1
        i = 0
        f = 'white_' + str(cnt) + '/'
        if not os.path.exists(targetFolder + f):
            os.makedirs(targetFolder + f)
    cur = folder + item
    print(targetFolder + f + item)
    # copyfile(cur, targetFolder + f + item)
    i += 1