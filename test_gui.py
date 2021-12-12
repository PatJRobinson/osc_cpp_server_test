from tkinter import *
from tkinter import ttk
root = Tk()

# Initialize a database of oscillator waveshapes
waveshapes = ('Sine', 'Square', 'Triangle', 'Saw', 'AllPartials')
wshapes = StringVar(value=waveshapes)

statusmsg = StringVar()

# Called when the selection in the listbox changes; figure out
# which waveshape is currently selected. Update the status message
# with the new waveshape.  As well, clear the message about the
# gift being sent, so it doesn't stick around after we start doing
# other things.
def wshape_info(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        name = waveshapes[idx]
        statusmsg.set("You have selected the %s oscillator" % (name))



# Create and grid the outer content frame
c = Frame(root)
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to.
# We're using the StringVar() 'wshapes', constructed from 'waveshapes'
lbox = Listbox(c, listvariable=wshapes, height=5)
lbl = Label(c, text="Select waveshape for oscillator:")
status = Label(c, textvariable=statusmsg, anchor=W)

# label tied to the same variable as the scale, so auto-updates
pitch = StringVar()
volume = StringVar()
Label(root, textvariable=pitch).grid(column=1, row=10, sticky='we')
Label(root, textvariable=volume).grid(column=2, row=10, sticky='we')

# label that we'll manually update via the scale's command callback
manual1 = Label(root)
manual1.grid(column=1, row=10, sticky='we')
manual2 = Label(root)
manual2.grid(column=2, row=10, sticky='we')
#
def update_pitch(val):
    manual1['text'] = "Pitch: " + val
#
def update_vol(val):
   manual2['text'] = "Volume: " + val
#

pitch_slider = Scale(orient=VERTICAL, length=100, from_=100.0, to=1.0, command=update_pitch)
amplitude_slider = Scale(orient=VERTICAL, length=100, from_=100.0, to=1.0, command=update_vol)
# Grid all the widgets
lbl.grid(column=0, row=0, padx=10, pady=5)
lbox.grid(column=0, row=2, rowspan=6, sticky=(N,S,E,W))
status.grid(column=0, row=7, columnspan=2, sticky=(W,E))
pitch_slider.grid(column=1, row=0, columnspan=1, padx=10, pady=5, sticky='we')
amplitude_slider.grid(column=2, row=0, columnspan=1, padx=10, pady=5, sticky='ns')

pitch_slider.set(20)
amplitude_slider.set(20)

c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', wshape_info)

# Colorize alternating lines of the listbox
for i in range(0,len(waveshapes),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# fired when users makes a change, we explicitly call showPopulation.
#gift.set('card')
statusmsg.set('')
lbox.selection_set(0)
wshape_info()

# We then put a few finishing touches on our user interface.
for child in c.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


root.mainloop()