from tkinter import *
from PIL import Image,ImageTk
from numpy import imag

window_btn = Tk()
window_btn.geometry("500x500")

image_test = ImageTk.PhotoImage(Image.open('../images/Group 1.png'))
Button(window_btn,image= image_test,border=0).place(x = 100, y =100)

window_btn.mainloop()