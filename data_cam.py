import funktion
import os
import pygame             
import pygame.camera
from time import asctime
input_ = input("Befehl!") #!!!Am Ende entfaellt dies
pfad_sicherung = os.getcwd()


if(input_=="Foto" or "foto"):
    funktion.cam_foto(png)
    print("Foto wurde geschossen :)")
else:
    print("Befehl:",input_,"wurde nicht gefunden")



    
os.chdir(pfad_sicherung)

 
