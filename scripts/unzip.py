from zipfile import ZipFile
import fnmatch
import re, os
import glob

def main():
    
    print('Unzipped files...')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('7255-Documentation_Hub-html5_-Upload_to_GitHub.zip', 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()


if __name__ == '__main__':
   main()
