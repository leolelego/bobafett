# -*- coding: utf-8 -*-
import os, shutil, urllib, time, sys
def reporthook(count, block_size, total_size):
    global start_time

    if count == 0:
        start_time = time.time()
        return 
    
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" % (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.urlretrieve(url, filename, reporthook)


folderToUpdate=["_includes","_layouts","index.html","_less/bootstrapVariables.less","_less/colors.less","_less/main.less","_updateScript/updateFromBoba.py"]
sourcesHTTP='https://github.com/leoderbois/Boba-Fett-Theme-For-Jekyll/archive/gh-pages.zip'


def backup(workspace,workspaceScript):
    try:

        print "workspace" + workspaceScript
        backupDir=os.path.join(workspaceScript,"_backup")
        print "--- Create backup at " + backupDir

        if(os.path.exists(backupDir)):
            shutil.rmtree(backupDir)
            print "Erasing  backup directory"
        print "Creating backup directory"
        os.mkdir(backupDir);

        for file in folderToUpdate:
            src=os.path.join(workspace,file)
            dst=os.path.join(backupDir,file)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))
                shutil.copy(src, dst)


        return True
    except ValueError:
            print "Oops!  Error occured :" + str(e)
            return False

def downloadSources(workspaceScript):
     try:
        print "--- downloading source at " + sourcesHTTP
        downloadDir=os.path.join(workspaceScript,"_download")
        sourcesZip=os.path.join(downloadDir,"sources.zip")
        if(os.path.exists(downloadDir)):
            shutil.rmtree(downloadDir)
        os.mkdir(downloadDir);

        save(sourcesHTTP, sourcesZip)

     except ValueError:
        print "Oops!  Error occured :" + str(e)
        return False
def main():
    # parse command line options
    workspaceScript = os.getcwd()
    workspace= os.path.dirname(os.getcwd())
    print "--- Updating Your BobaFettFork from original --- "
    
    print "path is to your resume : "+ workspace
    canContinu=True 
    if not backup(workspace,workspaceScript):
        canContinu=False

    if not downloadSources(workspaceScript):
        canContinu=False

    print "Continu"


if __name__ == "__main__":
    main()