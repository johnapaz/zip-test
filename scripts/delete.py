import os, glob


try:
    print('Deleted unneeded sub-directories...')
    os.rmdir('./7255-Documentation_Hub-html5/out')
    os.rmdir('./7255-Documentation_Hub-html5')
    os.remove('./7255-Documentation_Hub-html5_-Upload_to_GitHub.zip')
    
except:
   print('Unable to finish deleting...')
