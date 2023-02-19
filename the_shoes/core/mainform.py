from struct import pack
from tkinter import ttk, font
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import Image, ImageTk

mainForm = Tk()

fram_bg = Frame(mainForm, width=1040, height=740, background='#DFEBE9')
fram_bg.pack(side=TOP)


width_of_window = 1040
height_of_window = 740
screen_width = mainForm.winfo_screenwidth()
screen_height = mainForm.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
mainForm.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

#mainForm.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress = Progressbar(mainForm, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=1070, mode='determinate', )


def login_window():
    window_login = Tk()
    window_login.title('Login window')
    window_login.geometry('1040x740')
    window_login.config(background='#DFEBE9')
#//////////////////////////////////////WinDow Login Right
    frame_left_window = Frame(window_login, width=520,height=740,background='#DFEBE9')


    frame_left_window.pack(side=LEFT)
#///////////////////////////////////// WinDow Login LEFT
    frame_right_window = Frame(window_login,width=520,height=740,background='#DFEBE9')
    lable_login = Label(frame_right_window, text='Login',background='#DFEBE9',foreground='#749BAE')
    style1 = ('Calibri (Body)', 10)
    lable_login.config(font=style1)
    lable_login.place(x=150, y=200)
    frame_right_window.pack(side=RIGHT)

    window_login.mainloop()
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
        time.sleep(0.001)
        r = r + 1
    mainForm.destroy()
    login_window()

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


