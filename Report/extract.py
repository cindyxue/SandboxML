import os
import zipfile

path_to_zip_file = '/data/sandbox/Report_Dir/14/pe32/'
name = 'fd8ebf23a27e9c6dfbf9ef7779eb2455.zip'
directory_to_extract_to = '/home/cindy/SandboxML/Report/'

with zipfile.ZipFile(path_to_zip_file + zip_file_name, 'r') as zip_ref:
    listOfFileNames = zip_ref.namelist()
    for fileName in listOfFileNames:
        if fileName.endswith('.json'):
            zip_ref.extract(fileName, directory_to_extract_to)
            # md5 = os.path.splitext(fileName)[0]
            md5 = 'fe04c0fc835669bc27e75db4bebfa696'
            oldName = directory_to_extract_to + fileName
            newName = directory_to_extract_to + md5 + '.json'
            print("old: " + oldName)
            print("new: " + newName)
            os.rename(oldName, newName) 
