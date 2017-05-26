import os
import zipfile
import datetime

#INPUT_FOLDER = 'd:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging'
#OUTPUT_FILE = 'd:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging_' + datetime.datetime.now().strftime('%m%d%Y_%H.%M.%S') + '.zip'

class Zipper:
    def __init__(self):
        pass

    def zipdir(self, path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file),
                    os.path.join(path, '..'))
                )

    def zip(self, intpuFolder, outputFile):
        zipf = zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED)
        self.zipdir(intpuFolder, zipf)
        zipf.close()

if __name__ == '__main__':
    input('this module can not be run directly')
    
    #zipf = zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED)
    #zipdir(INPUT_FOLDER, zipf)
    #zipf.close()
