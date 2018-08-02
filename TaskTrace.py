from tkinter import *
from tkinter import ttk
import datetime


# ///////////////////////// MODEL /////////////////////////

currentTask = ""        # Name of the current task

def logTask(*args):
    if (currentTask == ""):
        createNewTask()
    else:
        endCurrentTask()

def createNewTask():
    global currentTask
    currentTask = newTask.get()
    taskLabel["text"] = "CURRENT TASK : " + currentTask
    with open("log.txt", "a") as myfile:
        myfile.write(">>>>> Task Begun: " + str(datetime.datetime.now()) + "\n")
        myfile.write("Task Name: " + str(currentTask) + "\n")
        print(datetime.datetime.now())
        print(currentTask)

def endCurrentTask():
    global currentTask
    currentTask = ""
    taskLabel["text"] = "CURRENT TASK : None"
    with open("log.txt", "a") as myfile:
        myfile.write(">>>>> Task Ended: " + str(datetime.datetime.now()) + "\n\n")
        print(datetime.datetime.now())


# ///////////////////////// VIEW /////////////////////////

root = Tk()
root.title("TaskTrace")
root.geometry("400x400+200+200")
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=3)
root.columnconfigure(0, weight=1)

taskLabel = ttk.Label(root, text=currentTask)
taskLabel.grid(row=0, column=0, sticky=(N,S,E,W))

newTask = StringVar()
taskEntry = ttk.Entry(root, textvariable=newTask)
taskEntry.grid(row=1, column=0, sticky=(N,S,E,W))
taskEntry.focus()

button = ttk.Button(root, text="Log", command=logTask)
button.grid(row=2, column=0, sticky=(N,S,E,W))
root.bind("<Return>", logTask)

root.mainloop()
