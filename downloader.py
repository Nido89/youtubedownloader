import tkinter as tk
from tkinter import *
root = Tk()
root.geometry('500x150')
def runit():
    os.startfile('link.bat')
def downloadytv():
    with open('link.bat', 'w') as down_load:
        down_load.write(f'youtube-dl{link.get()}')
        down_load.close()
    runit()
f = Frame(root)
f.grid()
Label(f,text='-------Download your favorite youtubevideos using my Downloader by Jalal-------',font=15,padx=6).pack()


f1= Frame(root)
f1.grid()
Label(f1,text='Paste Video Link Here.',font=5).grid(row=1)

link = StringVar()

Entry(f1,font=5,textvariable=link).grid(row=1,column=1,pady=5,padx=10)

Button=tk.Button(f1,text='Download',padx=50,relief=RAISED,font=10,borderwidth=5,command=downloadytv)
Button.grid(column=2,pady=10)
root.mainloop()