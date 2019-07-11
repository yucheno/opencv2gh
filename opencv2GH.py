"""
__author__ = "YU"
__version__ = "2019.07.11"
"""

# coding: utf-8

# In[1]:


import cv2
import socket
import pickle 
import math


# In[2]:


def UDP_client(IP, port,message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(message, "utf-8"),(IP,port))


# In[3]:


def center_radious(x,y,w,h):
    center_x = (2*x+w)/2
    center_y = (2*y+h)/2 
    r = math.sqrt(w**2+h**2)
    return center_x, center_y, r


# In[12]:


cap = cv2.VideoCapture(0)
#assign your local IP and using port
IP = ""
port = 5000


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    face_detection = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detection.detectMultiScale(frame, 1.2, 7)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 3)
        data = center_radious(x,y,w,h)
        
        message = "{},{},{},{},{}".format(int(data[0]),int(data[1]),int(data[2]),width,height) 
        UDP_client(IP, port, message)
    
    cv2.imshow("test", frame)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows() 


# In[ ]:




