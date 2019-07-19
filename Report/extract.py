import os
import zipfile

path_to_zip_file = '/data/sandbox/Report_Dir/14/pe32/fe04c0fc835669bc27e75db4bebfa696.zip'
directory_to_extract_to = '/home/cindy/SandboxML/Report/'

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)