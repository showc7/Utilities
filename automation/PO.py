import os
import zipfile
import datetime
import Zipper
from distutils.dir_util import copy_tree

INPUT_FOLDER = 'g:\Deploy\\UAS\\ProjectOnline_Staging'
OUTPUT_FILE = 'g:\Deploy\\UAS\\ProjectOnline_Staging_' + datetime.datetime.now().strftime('%m%d%Y_%H.%M.%S') + '.zip'

CHUNKS_FOLDER = 'g:\\projects\\git\\projectonline\\ProjectOnline.Web\\ProjectOnline.Web\\wwwroot\\lib\\chunks'

if __name__ == '__main__':

    # clear chunks    
    #r = input('clear all chunks in \'' + CHUNKS_FOLDER + '\'? y/N: ')

    #if r.lower() == 'y':
    #    print('removing old chunks ...')
    #    sourceDirectory = CHUNKS_FOLDER
    #    for(dirpath, dirnames, filenames) in os.walk(sourceDirectory):
    #        print(dirpath)
    #        for fileName in filenames:
    #            print(fileName)
    #            os.unlink(os.path.join(dirpath, fileName))
    #    print('done')
    #    exit(0)

    # copy chunks
    r = input('copy all chunks from \'' + CHUNKS_FOLDER + '\'? y/N: ')

    if r.lower() == 'y':
        print('copying ...')
        fromDirectory = CHUNKS_FOLDER
        toDirectory = 'g:\Deploy\\UAS\\ProjectOnline_Staging\\wwwroot\\lib\\chunks'
        copy_tree(fromDirectory, toDirectory)
        print('done')
    
    zipper = Zipper.Zipper()
    zipper.zip(INPUT_FOLDER, OUTPUT_FILE);
