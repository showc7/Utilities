import os
import zipfile
import datetime
import Zipper
from distutils.dir_util import copy_tree

INPUT_FOLDER = 'd:\Deploy\\UAS\\ProjectOnline_Staging'
OUTPUT_FILE = 'd:\Deploy\\UAS\\ProjectOnline_Staging_' + datetime.datetime.now().strftime('%m%d%Y_%H.%M.%S') + '.zip'

CHUNKS_FOLDER = 'd:\\projects\\git\\projectonline\\ProjectOnline.Web\\ProjectOnline.Web\\wwwroot\\lib\\chunks'

if __name__ == '__main__':
    r = input('copy all chunks from \'' + CHUNKS_FOLDER + '\'? y/N: ')

    if r.lower() == 'y':
        print('copying ...')
        fromDirectory = CHUNKS_FOLDER
        toDirectory = 'd:\Deploy\\UAS\\ProjectOnline_Staging\\wwwroot\\lib\\chunks'
        copy_tree(fromDirectory, toDirectory)
        print('done')
    
    zipper = Zipper.Zipper()
    zipper.zip(INPUT_FOLDER, OUTPUT_FILE);
