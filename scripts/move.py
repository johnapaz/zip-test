import shutil, os, glob


def moveAllFilesinDir(srcDir, dstDir):
# Check if both the are directories

    print('Moved files from unzipped directory to root...')
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
    # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '/*'):
        # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("srcDir & dstDir should be Directories")

sourceDir = '/7255-Documentation_Hub-html5/out'
destDir =  '/'

moveAllFilesinDir(sourceDir,destDir)
