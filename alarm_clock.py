#import and global variabels
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
alarm_time = None
window = tk.Tk()
window.title("alarm clock app")
window.resizable(width= False , height=False)
window.geometry("400x300")
window.configure(bg = "black")
#function for getting time
def set_alarm():
     global alarm_time
     current_time = datetime.now()
     alarm_time = current_time.replace(hour = int(hour_entry.get()) , minute = int(minute_entry.get()) , second=0 , microsecond=0)
     latest_alarm_label.configure(text = alarm_time.strftime("%H:%M:%S"))


#function to set alarm timer
def get_current_time():
    current_time = datetime.now()
    compare_current_time_wuth_alarm_time(current_time)
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    window.after(1000 , get_current_time)

#function for comparing time with alarm time
def compare_current_time_wuth_alarm_time(current_time):
     global alarm_time
     if alarm_time is not  None and current_time >= alarm_time:
          print("alarm reached")
          messagebox.showinfo("alarm info" , "your alarm has gone off")
          latest_alarm_label.configure(text = "No alarms has been set")
          alarm_time = None


#UI design
tk.Label(window , text="Alarm application built with tkinter" ,bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=1 , ).pack(pady=5)
#text time
time_label = tk.Label(window , text="12:30:30" , font = ("Tahoma" , 32) , bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=3)

time_label.pack()

#text input hour
#hour entry
tk.Label(window , text= "Hour",bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=1 , ).pack(pady=5)
#text time
hour_entry = tk.Entry(window)
hour_entry.pack()

#text input minute
#entry minute
tk.Label(window , text= "Minute",bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=1 , ).pack(pady=5)
#text time
minute_entry = tk.Entry(window)
minute_entry.pack(pady=3 )

#button set alarm
tk.Button(text="Set Alarm",bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=1 , command=set_alarm ).pack(pady=5)
#text time

#show last alarm
latest_alarm_label = tk.Label(window , text= "No alarms has been set",bg="#242424" , fg="white" , highlightbackground="red" , highlightthickness=1 , )
latest_alarm_label.pack(pady=5)
#text time
#running the Papplication
get_current_time()
window.mainloop()









