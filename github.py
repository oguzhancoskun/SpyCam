'''
Created on 27 Haz 2013

@author: onuragtas
'''
import os, sys
__usage__ = "github.py clone:y|n commit"
if len(sys.argv) < 3:
    print __usage__
else:
    if sys.argv[1] == "y":
        url = input()
        os.system("git clone "+url)
    os.system("git add -A")
    os.system('git commit -m "'+sys.argv[2]+'"')
    os.system("git push")
