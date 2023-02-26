from tkinter import *
from tkinter import ttk, font
from PIL import Image,ImageTk

bg_color = '#DFEBE9'


window_login = Tk()
window_login.title('Login window')
window_login.geometry('1040x740')
window_login.config(background='#DFEBE9')
#////////////////////////////////////////////////////////////////////////
image_framLeft = ImageTk.PhotoImage(Image.open('../images/Group 743.png'))
image_lable_login = ImageTk.PhotoImage(Image.open('../images/Group 744.png'))
image_text_username = ImageTk.PhotoImage(Image.open('../images/Group 745.png'))
image_text_password = ImageTk.PhotoImage(Image.open('../images/Group 746.png'))
image_btn_login = ImageTk.PhotoImage(Image.open('../images/Component 17.png'))
image_text_forgot_pass = ImageTk.PhotoImage(Image.open('../images/Group 747.png'))

frame_main = Frame(window_login,width=1040,height=740,background=bg_color)
frame_main.place(x = 0,y = 0)

fram_left = Frame(frame_main,width=500, height=740,background=bg_color)
fram_left.pack(side=LEFT)
lable_image_left = Label(fram_left,width=500,height=740,background=bg_color,image=image_framLeft)
lable_image_left.place(x=0,y=0)
#////////////////////////////////////////////FRAME LEFT

fram_right = Frame(frame_main,width=540,height=740,background=bg_color)
fram_right.pack(side=RIGHT)

fram_right_login = Frame(fram_right,width=540,height=500,background=bg_color)
fram_right_login.pack(side=TOP)

lable_text_login = Label(fram_right_login,image=image_lable_login,background=bg_color)
lable_text_login.place(x = 100 , y = 0)

lable_text_createnow = Label(fram_right_login, activebackground='#37677E', text= "Don't have account ?", background=bg_color)
lable_text_createnow.place(x = 100, y = 50)

lable_text_username = Label(fram_right_login,image=image_text_username, background=bg_color)
lable_text_username.place(x=100, y = 80)

username = StringVar()
usernameEntry = Entry(lable_text_username, textvariable=username,width=60,border=0)
usernameEntry.place(x=10,y=52)

lable_text_password = Label(fram_right_login,image=image_text_password, background=bg_color)
lable_text_password.place(x=100, y = 170)

password = StringVar()
passwordEntry = Entry(lable_text_password, textvariable=password,show='*',width=55,border=0)
passwordEntry.place(x=10,y=52)


btn_login = Button(fram_right_login,image=image_btn_login,border=0, background=bg_color)
btn_login.place(x=100, y= 290)


lable_text_forgotPass = Label(fram_right_login, image=image_text_forgot_pass, background=bg_color)
lable_text_forgotPass.place(x=100, y = 350)

#///////////////////////////////////////////////////FRAME RIGHT

window_login.mainloop()