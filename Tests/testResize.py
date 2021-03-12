from tkinter import *


class TkExample(Frame):
   def __init__(self, parent):
      Frame.__init__(self, parent)
      self.init_ui()

   def init_ui(self):
      self.pack()
      text_box = Text(self)
      text_box.pack()
      text_box.bind("<Key>", self.update_size)

   def update_size(self, event):
      widget_width = 0
      widget_height = float(event.widget.index(END))
      for line in event.widget.get("1.0", END).split("\n"):
         if len(line) > widget_width:
            widget_width = len(line)+1
      event.widget.config(width=widget_width, height=widget_height)
