from Tkinter import *
import ttk
import datetime


# ///////////////////////// MODEL ///////////////////////// 
currentTask = ""   # Name of the current task
newTask = ""       # The task we want to enter next

def logTask():
    if (currentTask == ""):
        createNewTask()
    else:
        endCurrentTask()

def createNewTask():
    global currentTask
    currentTask = newTask
    with open("log.txt", "a") as myfile:
        myfile.write(">>>>> Task Begun: " + str(datetime.datetime.now()) + "\n")
        myfile.write("Task Name: " + str(currentTask) + "\n")
        print(datetime.datetime.now())
        print(currentTask)

def endCurrentTask():
    global currentTask
    currentTask = ""
    with open("log.txt", "a") as myfile:
        myfile.write(">>>>> Task Ended: " + str(datetime.datetime.now()) + "\n")
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

newTask = ttk.Entry(root, textvariable=newTask)
newTask.grid(row=1, column=0, sticky=(N,S,E,W))

button = ttk.Button(root, text="Log", command=logTask)
button.grid(row=2, column=0, sticky=(N,S,E,W))

root.mainloop()
