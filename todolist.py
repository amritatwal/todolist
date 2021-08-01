#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:31:25 2020

@author: amritatwal
"""

import tkinter
import tkFont 
import tkinter.messagebox
import pickle

def add_task():
    task = entry_task.get()
    if task != "":        
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")
        

def completed_task():
    selection = listbox_tasks.curselection()
    current_selection = listbox_tasks.get(selection[0])
    new_current_selection = ""
    for i in current_selection:
        if i != " ":
            new_current_selection = new_current_selection + i + '\u0336'
    listbox_tasks.insert(selection, new_current_selection)
    old_selection = listbox_tasks.curselection()
    listbox_tasks.delete(old_selection)

   
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
          tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")  
    
def save_tasks():
    tasks = listbox_tasks.get(0,listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

root = tkinter.Tk()
root.title("To-Do List by Amrit")

# Create GUI

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=50, background="gray15")
listbox_tasks.config(foreground="thistle1", font=("Arial", 14))
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_completed_task = tkinter.Button(root, text="Mark complete", width=48, command=completed_task)
button_completed_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()

