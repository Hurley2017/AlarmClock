from tkinter import *
import datetime
import time
from playsound import playsound
import threading
def new_thread():
    thread = threading.Thread(target=parse_time)
    thread.start()
def alarm(timer):
    banner = False
    time_format=Label(clock, text= "Alarm  Set!", fg="white",bg="red",font="Helevetica").place(x=155,y=150)
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == timer:
            time_format=Label(clock, text= " Wake  UP! ", fg="white",bg="red",font="Helevetica").place(x=150,y=150)
            playsound('alarm_sound.mp3')
            banner = True
            break
    if banner:
        time_format=Label(clock, text= "Alarm Rang!", fg="white",bg="red",font="Helevetica").place(x=145,y=150)
def parse_time():
    timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(timer)
clock = Tk()
clock.title("Tusher's Alarm Clock")
clock.geometry("400x250")
addTime = Label(clock,text = "Hour",fg="Brown", bg="Cyan",relief = "groove", font=120).place(x = 80, y = 75)
addTime = Label(clock,text = "Minute",fg="Brown", bg="Cyan",relief = "groove",font=120).place(x = 172.5, y = 75)
addTime = Label(clock,text = "Second",fg="Brown", bg="Cyan",relief = "groove",font=120).place(x = 270, y =75)
addTime = Label(clock,text = ":",font=120).place(x = 147, y = 100)
addTime = Label(clock,text = ":",font=120).place(x = 247, y = 100)
setYourAlarm = Label(clock,text = "Set Time Here",fg="Black", bg="Magenta",relief = "flat",font=("Ariel",30,"bold")).place(x=38, y=10)
hour = StringVar()
min = StringVar()
sec = StringVar()
hourTime= Entry(clock,textvariable = hour,bg = "White",width = 7).place(x=70,y=100)
minTime= Entry(clock,textvariable = min,bg = "White",width = 7).place(x=170,y=100)
secTime = Entry(clock,textvariable = sec,bg = "White",width = 7).place(x=270,y=100)
submit = Button(clock,text = "Set Alarm",fg="Black", bg="Red",relief = "solid", width = 10,command = new_thread).place(x =145,y=200)
clock.mainloop()
