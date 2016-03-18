﻿import sys

number_of_elements  = int(input())  
number_of_fileNames = int(input()) 

file_extensions_association_array = {}

for i in range(number_of_elements):
    inputs = input().split()
    file_extensions_association_array[inputs[0].lower()] = inputs[1] # file extension and MIME type.
    
for i in range(number_of_fileNames):
    file_name = input()  # One file name per line.
    extension = "";
    
    if (file_name.find(".") != -1): # Checking for a dot
        extension = file_name[file_name.rfind(".") + 1 : len(file_name)].lower() # Including a dot
        
    print(file_extensions_association_array[extension] if file_extensions_association_array.get(extension) else "UNKNOWN")