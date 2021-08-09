import os, glob


try:
    print('Deleted unneeded sub-directories...')
    os.rmdir('../7255-Documentation_Hub-html5/out')
    os.rmdir('../7255-Documentation_Hub-html5')
    os.remove('../archive.zip')
    
except:
   print('Unable to finish deleting...')
