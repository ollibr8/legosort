'''
#################################################################################
Cam Syntax
funktion.cam_foto(dateiformat)

!!!Das Dateiformat muss ein Standardfotoformat sein (z.B.png,BMP,usw.).
!!!Außerdem koennen andere formate(z.B.txt,sh,usw.) NICHT verarbeitet werden.

???Mit dieser Funktion kann man ein Foto machen(mit dem gewünschten dateiformat).
#################################################################################
Log data Syntax
funktion.log_data(Id)

???Die Funktion wird verwendet um ein Log der Legosortiermachine zu schreiben.
???Mit der Id und der Echtzeit in der sie ausgeführt wird (wurde).
#################################################################################


'''
from tkinter import *
import pygame             
import pygame.camera
from time import asctime
def cam_foto(format_cam):        
    W=160
    H=120
    pygame.init()
    pygame.camera.init()
    CAMERALIST = pygame.camera.list_cameras()
    if CAMERALIST:
       CAMERA = pygame.camera.Camera(CAMERALIST[0],(W,H))
    else :
       print('Keine Kamera')
       exit(1)
    CAMERA.start()    
    SNAP = CAMERA.get_image()    
    pygame.image.save(SNAP,'Camera'+asctime()+format_cam) 

def log_data(id):
    text_f = open('log.txt','w')
    text_f.write("Id:",id,"Time:",asctime())
    
    
    
    
    text_f.close()
log_data(2)
def luncher():
    root = Tk()
    root.title("Luncher")
    root.geometry('700x400')
    Label(root,text="Leog Luncher",font = "Helvetica 30 bold italic",fg = "blue").pack()
    Label(root,text="Process lunch",font = "Helvetica 20",fg = "yellow").pack()
    Button(root, text="Stopp").pack()
    Button(root, text="Start").pack()
    root.mainloop()   
#luncher()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
