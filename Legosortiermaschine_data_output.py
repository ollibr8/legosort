from tkinter import *
from subprocess import call
r_output = "hallo"
text_output = r_output





def ausführen_():
    print("output",e1.get())



root = Tk()

root.title('Legosortiermaschine Steuerung')

root.geometry('500x300')

but1 = Button(root, text="ausführen",command=ausführen_)

Label(root, text="Commando:").grid(row=0)

Label(root, text="ich")


e1 = Entry(root)

e1.grid(row=0 ,column=1)

but1.grid()

print("output",e1.get())
if (e1.get().strip().lower() == "close"):
    print("dfhsd")
    





root.mainloop()