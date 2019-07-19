import os
import zipfile

def extractReport(path_to_zip_file, zip_file_name, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file + zip_file_name, 'r') as zip_ref:
        listOfFileNames = zip_ref.namelist()
        for fileName in listOfFileNames:
            if fileName.endswith('.json'):
                zip_ref.extract(fileName, directory_to_extract_to)
                md5 = os.path.splitext(zip_file_name)[0]
                # md5 = 'fe04c0fc835669bc27e75db4bebfa696'
                oldName = directory_to_extract_to + fileName
                newName = directory_to_extract_to + md5 + '.json'
                print(oldName)
                print(newName)
                os.rename(oldName, newName) 

def main(): 
    folder = '/data/sandbox/Report_Dir/14/pe32/'
    targetFolder = '/data/sandbox/cuckoo_reports'
    extension = ".zip"

    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)

    for item in os.listdir(folder):
        if item.endswith(extension):
            extractReport(folder, item, targetFolder)
            # try:
            #     extractReport(folder, item, targetFolder)
            # except Exception as e:
            #     print(item)
            #     print(e)


# Driver Code 
if __name__ == '__main__': 
      
    main() 