from Tkinter import *
import ttk
import subprocess

##subprocess.call("xinput --set-prop 'QDtech MPI5001' 'Coordinate Transformation Matrix'  0 -1 1 1 0 0 0 0 1", shell=True)


## GUI Definitions
win = Tk()
win.title("Kasper's Bartender")
win.geometry("480x750+0+0")

photo = PhotoImage(file="billede.png")

labelPhoto = Label(win, image=photo)
labelPhoto.grid(row=1, columnspan=2)

## Labels

labelDrinkName=Label(win,text = "Drink Navn", font=("Helvetica", 40))
labelDrinkName.grid(row=0,columnspan=2)



labelPrep1=Label(win,text = "Beskrivelse af den drinks du har valgt",font=("Helvetica", 20))
labelPrep1.grid(row=2,column=0, columnspan=2, sticky=W)

labelPrep2=Label(win,text = "Dette er anden linje",font=("Helvetica", 20))
labelPrep2.grid(row=3,column=0, columnspan=2, sticky=W)

labelPrep3=Label(win,text = "Dette er tredje linje",font=("Helvetica", 20))
labelPrep3.grid(row=4,column=0, columnspan=2, sticky=W)

labelPrep1=Label(win,text = "Dette er fjerde linje",font=("Helvetica", 20))
labelPrep1.grid(row=5,column=0, columnspan=2, sticky=W)

labelPrep2=Label(win,text = "Dette er femte linje",font=("Helvetica", 20))
labelPrep2.grid(row=6,column=0, columnspan=2, sticky=W)

##labelPrep3=Label(win,text = "",height = 11,font=("Helvetica", 20))
##labelPrep3.grid(row=6,column=0, columnspan=2, sticky=W)

##Buttons
BTNChange=Button(win, text = 'SKIFT', font=("Helvetica", 22), height=2, width=11)
BTNChange.grid(row=8,column=0)

BTNSelect=Button(win, text = 'JA TAK!',font=("Helvetica", 22), height=2, width=11)
BTNSelect.grid(row=8,column=1)


## progressbar
progressbar = ttk.Progressbar(win, orient="horizontal", length=400, mode="determinate")
progressbar.grid(row=7, columnspan=2)

progressbar["value"]=0
progressbar.update()
progressbar["maximum"]=1





win.mainloop()
