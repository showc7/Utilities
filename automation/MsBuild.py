from xml.dom import minidom
import xml.etree.ElementTree as ET
from subprocess import Popen, PIPE, call, check_output
import os

COMPILER = 'C:\\Program Files (x86)\\MSBuild\\14.0\\Bin\\MSBuild.exe'

class MsBuild:

    def __init__(self, msbuild_path = None):
        if msbuild_path is not None:
            self.msbuild = msbuild_path
        else:
            self.msbuild = COMPILER

        if not os.path.isfile(self.msbuild):
            raise Exception('MsBuild not found by path: ' + self.msbuild)
    
    def publish(self, solution_file, publish_profile):
        if solution_file is None:
            raise Exception('solution_file is None')
        
        if not os.path.isfile(solution_file):
            raise Exception('solution file not found by path: ' + solution_file)
        
        if publish_profile is None:
            raise Exception('solution is None')
        
        if not os.path.isfile(publish_profile):
            raise Exception('Publish profile not found by path: ' + publish_profile)

        # getting publish_output_folder from publish profile
        tree = minidom.parse(publish_profile)
        publish_output_folder = tree.getElementsByTagName('publishUrl')[0].firstChild.nodeValue

        # running publish process
        argument0 = '/p:DeployOnBuild=true'
        argument1 = '/p:PublishProfile=' + publish_profile

        p = Popen([self.msbuild, argument0, argument1, solution_file], stdout=PIPE, stderr=PIPE, shell=True)
        output, err = p.communicate()
        self.returncode = p.returncode
        #print(ret_code)
        #print(output)
        
        if self.returncode is not 0:
            return (False, None)

        return (True, publish_output_folder)

if __name__ == '__main__':
    input('this module can not be run directly')