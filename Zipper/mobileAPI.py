import os
import zipfile
import datetime
import Zipper

INPUT_FOLDER = 'd:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging'
OUTPUT_FILE = 'd:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging_' + datetime.datetime.now().strftime('%m%d%Y_%H.%M.%S') + '.zip'

if __name__ == '__main__':
    zipper = Zipper.Zipper()
    zipper.zip(INPUT_FOLDER, OUTPUT_FILE);
