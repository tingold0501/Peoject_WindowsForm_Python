from tkinter import *
from PIL import Image,ImageTk
window_dashboard = Tk()
bg_color = '#DFEBE9'

window_dashboard.geometry("1040x740")
window_dashboard.config(background= bg_color)

image_frame_left = ImageTk.PhotoImage(Image.open('../images/Group 1000001543.png'))
image_frame_total = ImageTk.PhotoImage(Image.open('../images/Group 1000001545.png'))
image_frame_over = ImageTk.PhotoImage(Image.open('../images/Group 1000001546.png'))
image_graph = ImageTk.PhotoImage(Image.open('../images/Group 1000001547.png'))
image_contact = ImageTk.PhotoImage(Image.open('../images/Group 1000001549.png'))


frame_main = Frame(window_dashboard,width=1040, height=740, background=bg_color)
frame_main.place(x=0,y=0)

frame_left = Frame(frame_main, width= 300, height= 740, background=bg_color)
frame_left.pack(side=LEFT)

lable_bg_left = Label(frame_left, image= image_frame_left, background= bg_color)
lable_bg_left.place(x=0,y=0)

frame_right = Frame(frame_main, width= 740, height= 740, background=bg_color)
frame_right.pack(side=RIGHT)

lable_total = Label(frame_right, image= image_frame_total, background=bg_color)
lable_total.place(x=0,y=20)

frame_left_bottom = Frame(frame_right, width= 740, height= 600, background=bg_color)
frame_left_bottom.place(x = 0,y =140)

label_over = Label(frame_left_bottom, image= image_frame_over, background= bg_color)
label_over.place(x=6,y=10)

lable_graph = Label(frame_left_bottom,image= image_graph, background=bg_color)
lable_graph.place(x= 0, y = 260)



window_dashboard.mainloop()