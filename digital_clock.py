#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from time import strftime

# Create window
root = Tk()
root.title('Digital Clock')

# Styling the clock label
label = Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Time function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()


# In[ ]:




