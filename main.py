import webbrowser

from tkinter import *

root = Tk()

root.title("WebBrowser")

root.geometry("300x200")

def github():
    webbrowser.open("https://github.com/MicheleCorradi")

def google():
    webbrowser.open("www.google.com")

github = Button(root, text="visit my github", command=github).pack(pady=20)

mygoogle = Button(root, text="open Google",command=google).pack(pady=20)

root.mainloop()