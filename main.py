# Python program to create a simple GUI Remainder Application Notification
import time
from plyer import notification
# import everything from tkinter module
from tkinter import *


print("app is running")
def noti():
    if __name__ =="__main__":
        
        root.iconify()
        
        t=int(time1_entry.get())
        time.sleep(t)
        notification.notify(
            title=title1_entry.get(),
            message=message1_entry.get(),
            
            #app_name="Devotional",
            app_name='war',
            app_icon="G:\CHROME DOWN\Oxygen-Icons.org-Oxygen-Actions-document-edit.ico",
             #message is shown for 10 seconds
            timeout=10
            
        )
        print("execution completed")
        root.destroy()
def destroy_window():
    print("execution completed")
    root.destroy()
# Driver code
root=Tk()
root.title("INFORMER")
root.geometry("300x200")
root.minsize(300,200)
root.maxsize(300,200)
ts=Label(text="WELCOME TO YOUR INFORMER")
ts.grid(row=0,columnspan=2)
title1_label = Label(root, text= "Title:",pady=7)
# grid method is used for placing the widgets at respective positions in table like structure .
title1_label.grid(row=1,column=0)
# create the text entry box for showing the expression.
title1_entry = Entry(root)
title1_entry.grid(row=1,column=1)
message1_label = Label(root, text= "Message:",pady=7)
message1_label.grid(row=2,column=0)
message1_entry = Entry(root)
message1_entry.grid(row=2,column=1)
time1_label = Label(root, text= "Time:",pady=7)
time1_label.grid(row=3,column=0)
time1_entry = Entry(root)
time1_entry.grid(row=3,column=1)
text_label = Label(root, text= "click yes to get notification otherwise click no :",pady=5)
text_label.grid(row=5,columnspan=2)
# create a Buttons and place at a particular location inside the root window .when user press the button, the command or function affiliated to that button is executed 
b1=Button(text="yes",width=10,command=noti)
b1.grid(row=6,column=0)
b2=Button(text="no",width=10,command=destroy_window)
b2.grid(row=6,column=1)
# start the GUI
root.mainloop()
