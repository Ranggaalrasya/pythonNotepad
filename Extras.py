#################################################
# gasukaa dengan notepadny? kembangkan sendiri! #
#################################################

# You can make a 'Settings' sub-menu and try this:

from tkinter import *

def read_only():
    pad.config(state='disabled')

def editable():
    pad.config(state='normal')

settings = Menu(options)
options.add_cascade(label='Settings', menu=settings)
settings.add_command(label='Make Read Only', command=read_only)
settings.add_command(label='Editable', command=editable)


root.mainloop()
