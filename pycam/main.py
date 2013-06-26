# -*- coding: cp1254 -*-
'''
Created on 26 Haz 2013

@author: onuragtas
'''
from cv2 import *
import os, paramiko, time
# initialize the camera
host = "10.1.255.166"
user="onuragtas"
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
	    namedWindow("test",CV_WINDOW_AUTOSIZE)
	    imshow("test",img)
	    destroyWindow("test")
	    imwrite("filename"+str(i)+".jpg",img) #save image
	    filepath = 'filename'+str(i)+'.jpg'
	    localpath = '/home/onuragtas/resim'+str(i)+'.jpg'
	    sftp.put(filepath, localpath)
	    os.system("rm -R filename"+str(i)+".jpg")
	    i=i+1	   
sftp.close()
transport.close()