import os
import zipfile

folder = '/data/sandbox/Report_Dir/14/pe32'
targetFolder = '/data/sandbox/cuckoo_reports'
extension = ".zip"

if not os.path.exists(targetFolder):
    os.makedirs(targetFolder)

for item in os.listdir(folder):
    if item.endswith(extension):
        try:
            
        except:
            print(item)
            print(e)