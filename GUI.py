from _datetime import datetime, timedelta
from tkinter import *
import time
import vlc
import os

os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')
mp3 = vlc.MediaPlayer("C:/Users/Aaron/PycharmProjects/Alarm Clock/Music/Snooze.mp3")


root = Tk()
root.title('Scary Alarm')
root.geometry("600x350")
root.config(bg="black")


# Clock function
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    clock_face.config(text=hour + ":" + minute + ":" + second + "  " + am_pm)
    clock_face.after(1000, clock)


clock_face = Label(root, text="", font=("Helvetica", 48), fg="white", bg="black")

# Date label above clock
def date():
    day = time.strftime("%A")
    month = time.strftime("%B")
    day_of_month = time.strftime("%d")

    date_label.config(text=day + ", " + month + " " + day_of_month)


date_label = Label(root, text="", font=("Helvetica", 18), fg="white", bg="black")

# Alarm Sound Function
def AlarmSound():
    mp3.play()

# Setting Alarm for 06:30. This is the time I always wake up. Alarm will look at today's date and time and if it
# is after 6 AM it will set the alarm to 6:30 the following day. Otherwise, it will set the alarm for 6 AM the
# current day. This calculation was created because while loops and other threading issues happen with Tkinter.
# Using the .after() function allows us to have the function called at exactly the right time to play the alarm.

def setAlarm():
    actual_Time = datetime.now()
    dt6_30 = None
    if actual_Time.hour < 6:
        dt6_30 = datetime(actual_Time.year, actual_Time.month, actual_Time.day, 6, 30, 0, 0)
    else:
        day = timedelta(days=1)
        tomorrow = actual_Time + day
        dt6_30 = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 6, 30, 0, 0)
    seconds = dt6_30 - actual_Time
    time_till_alarm = seconds.seconds * 1000
    root.after(time_till_alarm, AlarmSound)


def setAlarmLabel():
    alarmsetLabel = Label(root, text="Alarm set for 06:30")
    alarmsetLabel.pack()
    alarmsetLabel.after(5000, alarmsetLabel.destroy)



# Function for clicking Yes, I woke up
def yesClick():
    myLabel1 = Label(root, text="Good Morning!")
    myLabel1.pack()
    mp3.stop()


# Function for Snoozing. To be honest there is no function because I need to wake up.
def snoozeClick():
    myLabel1 = Label(root, text="Do you really want to snooze? You know how you are man...")
    snoozeButton = Button(root, text="Yes", padx=30, fg="white", bg="black")
    snoozeButton2 = Button(root, text="Ugh. Maybe I should get up....", padx=30, fg="white", bg="black",
                           command=yesClick)
    myLabel1.pack()
    snoozeButton.pack()
    snoozeButton2.pack()


# Function for further guilt-tripping myself into waking up
def myClick():
    myLabel1 = Label(root, text="Did you actually wake up?")
    myButton2 = Button(root, text="Yes", padx=40, fg="white", bg="black", command=yesClick)
    myButton3 = Button(root, text="No I need to snooze...", padx=40, fg="white", bg="black", command=snoozeClick)
    myLabel1.pack()
    myButton2.pack()
    myButton3.pack()


# Button created to turn off alarm
myButton = Button(root, text="Turn Off Alarm", padx=30, command=myClick, fg="white", bg="black")


# Alarm button
alarmButton = Button(root, text="Set Alarm for 06:30", padx=30, command=lambda:[setAlarm(), setAlarmLabel()], fg="white", bg="black")


# shoving it onto the screen

date_label.pack(pady=10)
clock_face.pack(pady=20)

alarmButton.pack()
myButton.pack()

date()
clock()

root.mainloop()
