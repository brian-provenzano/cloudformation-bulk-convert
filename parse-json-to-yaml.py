#!/usr/bin/python3

"""
parse-json-to-yaml.py
-----------------------
Very simple script that converts files to yaml using cfn_flip library
https://github.com/awslabs/aws-cfn-template-flip
-----------------------

Usage:
-----------------------
Drop script into parent directory that needs files to be converted to yaml; it will recurse and convert.
NOTE: Overwrites if files exists!!

BJP - 11/9/18 
TODOs - future features?
"""

import os
#third party 
from cfn_flip import flip, to_yaml

def main():
    exclude = set([".git",".vscode"])
    for root, dirs, files in os.walk(os.getcwd()):
        dirs[:] = [d for d in dirs if d not in exclude]
        for f in files:
            current_filepath = "{0}/{1}".format(root,f)
            with open(current_filepath,"r") as current_file:
                try:
                    yaml_converted = to_yaml(current_file.read())
                    new_filepath = "{0}/{1}.yaml".format(root,f)
                    print("\033[32m >> Converting file to yaml [{0}] << \033[0m".format(current_filepath))
                    with open(new_filepath,"w") as new_file:
                        new_file.write("# NOTE: Converted using cfn_flip + parse-json-to-yaml.py script\n")
                        new_file.writelines(yaml_converted)
                except Exception:
                    print("\033[31m >> Bad or not able to convert to yaml (may already be yaml?) - skipping file [{0}]<< \033[0m".format(current_filepath))
                    continue

if __name__ == '__main__':
    main()