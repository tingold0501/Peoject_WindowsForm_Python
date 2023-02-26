from tkinter import ttk, font
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import Image, ImageTk

mainForm = Tk()
mainForm.geometry("1040x740")
mainForm.config(background='#DFEBE9')



width_of_window = 1040
height_of_window = 740
screen_width = mainForm.winfo_screenwidth()
screen_height = mainForm.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
mainForm.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

image_btn_register = ImageTk.PhotoImage(Image.open('../images/Group 591.png'))



s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(mainForm, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=1070, mode='determinate', )

def bar():
    l4 = Label(mainForm, text='Loading...', fg='#207198', bg='#DFEBE9')
    lst4 = ('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=18, y=690)
    import time
    r = 0
    for i in range(100):
        progress['value'] = r
        mainForm.update_idletasks()
        time.sleep(0.01)
        r = r + 1
    mainForm.destroy()

progress.place(x=-10, y=722)

b1 = Button(mainForm, width=35, height=3,foreground='#207198', text='Get Started', command=bar, border=0, bg='#E3F1FE')
b1.place(x=30, y=370)
lst5 = ('Calibri (Body)', 10)
b1.config(font=lst5)

l1=Label(mainForm,text='THE SHOES',fg='#749BAE',bg='#DFEBE9')
lst1= font.Font(family='Shantell Sans , cursive',size=40)
l1.config(font=lst1)
l1.place(x=30,y=80)

l3=Label(mainForm,text='GROUP 7',fg='#207198',bg='#DFEBE9')
lst3=('Calibri (Body)',20)
l3.config(font=lst3)
l3.place(x=30,y=150)

mainForm.mainloop()


