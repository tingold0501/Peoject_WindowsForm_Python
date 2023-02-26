from tkinter import *
from tkinter import ttk, font
from PIL import Image,ImageTk

bg_color = '#DFEBE9'


window_login = Tk()
window_login.title('Register window')
window_login.geometry('1040x740')
window_login.config(background='#DFEBE9')
#////////////////////////////////////////////////////////////////////////
image_framLeft = ImageTk.PhotoImage(Image.open('../images/Group 743.png'))
image_framRight = ImageTk.PhotoImage(Image.open('../images/Group 585.png'))
image_text_firstname = ImageTk.PhotoImage(Image.open('../images/Group 586.png'))
image_text_lastname = ImageTk.PhotoImage(Image.open('../images/Group 587.png'))
image_text_email = ImageTk.PhotoImage(Image.open('../images/Group 588.png'))
image_text_password = ImageTk.PhotoImage(Image.open('../images/Group 589.png'))
image_text_confirmpassword = ImageTk.PhotoImage(Image.open('../images/Group 590.png'))
image_btn_register = ImageTk.PhotoImage(Image.open('../images/Group 591.png'))


frame_main = Frame(window_login,width=1040,height=740,background=bg_color)
frame_main.place(x = 0,y = 0)

fram_left = Frame(frame_main,width=500, height=740,background=bg_color)
fram_left.pack(side=LEFT)
lable_image_left = Label(fram_left,width=500,height=740,background=bg_color,image=image_framLeft)
lable_image_left.place(x=0,y=0)
#////////////////////////////////////////////FRAME LEFT


frame_right_register = Frame(frame_main,width=540, height=740, background=bg_color)
frame_right_register.pack(side=RIGHT)

lable_Create = Label(frame_right_register, background= bg_color, image= image_framRight)
lable_Create.place(x=20 ,y =100)

lable_text_firstname = Label(frame_right_register, image= image_text_firstname, background=bg_color)
lable_text_firstname.place(x =  20, y  = 160)
firstname = StringVar()
firstnameEntry = Entry(lable_text_firstname, textvariable=firstname,width=50,border=0)
firstnameEntry.place(x= 10, y = 48)

lable_text_lastname = Label(frame_right_register, image= image_text_lastname, background=bg_color)
lable_text_lastname.place(x =  20, y  = 240)
lastname = StringVar()
lastnameEntry = Entry(lable_text_lastname, textvariable=lastname,width=50,border=0)
lastnameEntry.place(x= 10, y = 48)

lable_text_email = Label(frame_right_register, image= image_text_lastname, background=bg_color)
lable_text_email.place(x =  20, y  = 320)
email = StringVar()
emailEntry = Entry(lable_text_email, textvariable=email,width=50,border=0)
emailEntry.place(x= 10, y = 48)

lable_text_password = Label(frame_right_register, image= image_text_password, background=bg_color)
lable_text_password.place(x =  20, y  = 400)
password = StringVar()
passwordEntry = Entry(lable_text_password,show="*", textvariable=password,width=50,border=0)
passwordEntry.place(x= 10, y = 48)

lable_text_confirmpassword = Label(frame_right_register, image= image_text_confirmpassword, background=bg_color)
lable_text_confirmpassword.place(x =  20, y  = 480)
confirmpassword = StringVar()
confirmpasswordEntry = Entry(lable_text_confirmpassword, show="*" ,textvariable=confirmpassword,width=50,border=0)
confirmpasswordEntry.place(x= 10, y = 48)

btn_register = Button(frame_right_register, image= image_btn_register, border= 0, background=bg_color)
btn_register.place(x = 20, y = 580)
lastname = StringVar()
lastnameEntry = Entry(lable_text_lastname, textvariable=lastname,width=50,border=0)
lastnameEntry.place(x= 10, y = 48)

window_login.mainloop()