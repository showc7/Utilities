from xml.dom import minidom
import re
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE, call, check_output
import logging
import msvcrt as m
import os
import zipfile
import datetime
import Zipper
import MsBuild

PUBLISH_CONFIG = 'G:\\projects\\git\\mobileapi\\USAutoSales.MobileAPI\\USAutoSales.MobileAPI\\Properties\\PublishProfiles\\Staging.pubxml'
SOLUTION = 'G:\\projects\\git\\mobileapi\\USAutoSales.MobileAPI\\USAutoSales.MobileAPI.sln'
OUTPUT_FILE = 'g:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging_' + datetime.datetime.now().strftime('%m%d%Y_%H.%M.%S') + '.zip'

#https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks

#COMPILER = 'C:\\Program Files (x86)\\MSBuild\\14.0\\Bin\\MSBuild.exe'
# replace with publish config value
#INPUT_FOLDER = 'g:\Deploy\\UAS\\USAutoSales.Mobile.API_Staging'
#BUILD_COMMAND = '"' + COMPILER + '" /p:DeployOnBuild=true /p:PublishProfile="' + PUBLISH_CONFIG + '" ' + SOLUTION
#OUTPUT_REGEXP = """Build succeeded."""

def wait():
    m.getch()

if __name__ == '__main__':
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.warning('warning')
    logger.info('start building ...')
    logger.error('error')
    logger.debug('debug')
    """

    '''
    tree = minidom.parse(PUBLISH_CONFIG)
    #print(tree)
    INPUT_FOLDER = tree.getElementsByTagName('publishUrl')[0].firstChild.nodeValue
    print(INPUT_FOLDER)
    
    process = Popen(BUILD_COMMAND, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    pattern = re.compile(OUTPUT_REGEXP)
    output = stdout.decode('utf-8')
    ret = pattern.search(output)

    #check it
    ret_code = process.returncode

    if ret != None:
        print('packing')
        zipper = Zipper.Zipper()
        zipper.zip(INPUT_FOLDER, OUTPUT_FILE)
    else:
        print('fail')
        #print(output)
        wait()
    '''
    print('publishing ...')
    
    msbuild = MsBuild.MsBuild()
    result = msbuild.publish(SOLUTION, PUBLISH_CONFIG)

    #print(result)

    if not result[0]:
        print('publish faild')
        exit(1)

    print('publish succeeded')

    print('packing ...')
    zipper = Zipper.Zipper()
    zipper.zip(result[1], OUTPUT_FILE)
    print('packing succeeded')
