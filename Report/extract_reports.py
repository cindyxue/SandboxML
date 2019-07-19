import os
import zipfile

folder = '/data/sandbox/Report_Dir/14/pe32'
extension = ".zip"

for item in os.listdir(folder):
    if item.endswith(extension):
        print(item)