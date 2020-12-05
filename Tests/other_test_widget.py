from tkinter import *


class MainWindow:
  def __init__(self, root):
    self.root = root
    self.tasks = ['text1', 'text2', 'text3']
    self.list_tasks()

  def list_tasks(self):
    self.tasks_frame = Frame(self.root)
    for task in self.tasks:
      task_label = Label(self.tasks_frame, text=task)
      task_label.bind('<Button>', self.replace_with_entry)
      task_label.pack()
    print(self.tasks_frame)
    self.tasks_frame.pack()

  def replace_with_entry(self, event):
    print("replace")
    widget = event.widget
    entry_widget = Entry(widget)
    entry_widget.place(x=0, y=0, anchor="nw", relwidth=1.0, relheight=1.0)
    entry_widget.bind("<Return>", self.remove_entry)
    entry_widget.focus_set()

  def remove_entry(self, event):
    entry = event.widget
    label = entry.place_info()["in"]
    label.configure(text=entry.get())
    entry.destroy()
