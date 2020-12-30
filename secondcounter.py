# secondcounter
from tkinter import *
import threading
import time
r=Tk()
r.geometry("400x400")
r.minsize(200,200)
r.maxsize(500,500)
speed=0
count=0
counting=None
counting=IntVar()
def counter():
    global speed,count
    print(count)
    while True:
        time.sleep(1)
        count+=speed
        counting.set(count)
timer=threading.Thread(target=counter)
timer.start()
def starttimer():
    global speed
    speed=1
def stoptimer():
    global speed
    speed=0
def resettimer():
    global count,speed
    count=0
    speed=0
background=Label(bg="yellow",padx=400,pady=400)
background.place(x=0,y=0)
heading=Label(text="COUNTER",font="arial 30 bold",bg="red")
heading.place(x=0,y=10)
start=Button(text="START",command=starttimer,padx=40)
start.place(x=20,y=300)
stop=Button(text="STOP",command=stoptimer,padx=40)
stop.place(x=130,y=300)
reset=Button(text="RESET",command=resettimer,padx=37)
reset.place(x=245,y=300)
label=Label(textvariable=counting,font="arial 30 bold",bg="white")
label.place(x=230,y=100)
r.mainloop()
