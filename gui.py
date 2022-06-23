import os
from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
  gui = Tk()
else:
  gui = Tk()
gui.title('NFM Restarter')
gui.resizable(False, False)
gui.geometry('400x400')
gui.grid_propagate(False)
for x in range(11):
  Grid.columnconfigure(gui, x, weight=1, uniform='row')
for y in range(11):
  Grid.rowconfigure(gui, y, weight=1, uniform='row')
for x in range(11):
  for y in range(11):
    Label(gui, width = 1, bg = '#C6C6C6').grid(row = y, column = x, sticky = N+S+E+W)
init = True
gui.label = Label(gui, text = "NFM Path:", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#c6c6c6')
gui.label.grid(row = 2, column = 3, columnspan = 5, rowspan = 1, sticky = N+S+E+W)
gui.success1 = Label(gui, text = "", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#c6c6c6')
gui.success1.grid(row = 8, column = 2, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
gui.success2 = Label(gui, text = "", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', bg = '#c6c6c6')
gui.success2.grid(row = 8, column = 6, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
gui.path = Entry(gui, width = 1, bg = '#FFFFFF', justify = 'center')
gui.path.grid(row = 3, column = 3, columnspan = 3, rowspan = 1, sticky = N+S+E+W)
gui.path.insert(0, "")
def runrestart_game(argument):
  global init
  if not(__name__ == '__main__'):
    init = True
    from main import restart_game
    if argument == "nfm1go":
      restart_game(1, gui.path.get())
      gui.success1.config(text = "Done!")
    else:
      restart_game(2, gui.path.get())
      gui.success2.config(text = "Done!")
def runopenfile(argument):
  global init
  if not(__name__ == '__main__'):
    init = True
    from main import openfile
    folder = openfile()
    gui.path.delete(0,END)
    gui.path.insert(0,folder)
gui.nfm1go = Button(gui, text = "Restart NFM1", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', command = lambda: runrestart_game("nfm1go"), bg = '#00FFFF')
gui.nfm1go.grid(row = 6, column = 2, columnspan = 3, rowspan = 2, sticky = N+S+E+W)
gui.nfm2go = Button(gui, text = "Restart NFM2", font = ('Arial', 16), width = 1, height = 1, fg = '#000000', command = lambda: runrestart_game("nfm2go"), bg = '#00FFFF')
gui.nfm2go.grid(row = 6, column = 6, columnspan = 3, rowspan = 2, sticky = N+S+E+W)
gui.browse = Button(gui, text = "Browse", font = ('Arial', 14), width = 1, height = 1, fg = '#000000', command = lambda: runopenfile("browse"), bg = '#00FFFF')
gui.browse.grid(row = 3, column = 6, columnspan = 2, rowspan = 1, sticky = N+S+E+W)
def initModules():
  from main import restart_game
  from main import openfile
gui.initModules = initModules
def hide():
  gui.withdraw()
def show():
  gui.deiconify()
def hideAllWidgets():
    gui.label.grid_remove()
    gui.success1.grid_remove()
    gui.success2.grid_remove()
    gui.path.grid_remove()
    gui.nfm1go.grid_remove()
    gui.nfm2go.grid_remove()
    gui.browse.grid_remove()
gui.hideAllWidgets = hideAllWidgets
def showAllWidgets():
    gui.label.grid()
    gui.success1.grid()
    gui.success2.grid()
    gui.path.grid()
    gui.nfm1go.grid()
    gui.nfm2go.grid()
    gui.browse.grid()
gui.showAllWidgets = showAllWidgets
running = True
def isRunning():
    global running
    return running
def quit():
    global running
    running = False
    gui.hide()
gui.protocol("WM_DELETE_WINDOW", quit)
gui.isRunning = isRunning
def run():
  global init
  gui.update()
  gui.update_idletasks()
  if init:
    gui.label.config(wraplength = gui.label.winfo_width() + 2)
    gui.success1.config(wraplength = gui.success1.winfo_width() + 2)
    gui.success2.config(wraplength = gui.success2.winfo_width() + 2)
    gui.nfm1go.config(wraplength = gui.nfm1go.winfo_width() + 2)
    gui.nfm2go.config(wraplength = gui.nfm2go.winfo_width() + 2)
    gui.browse.config(wraplength = gui.browse.winfo_width() + 2)
    if (gui.label.cget("wraplength") > 3):
        init = False
gui.run = run
gui.hide = hide
gui.show = show

if __name__ == "__main__":
  while isRunning():
    gui.run()
