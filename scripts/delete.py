import os, glob


try:
    print('Deleted unneeded sub-directories...')
<<<<<<< HEAD
    os.rmdir('../7255-Documentation_Hub-html5/out')
    os.rmdir('../7255-Documentation_Hub-html5')
    os.remove('../7255-Documentation_Hub-html5_-Upload_to_GitHub.zip')
=======
    os.rmdir('./7255-Documentation_Hub-html5/out')
    os.rmdir('./7255-Documentation_Hub-html5')
    os.remove('./archive.zip')
>>>>>>> d0add90111130cd606363e03e84d0f981bc2cd9c
    
except:
   print('Unable to finish deleting...')
