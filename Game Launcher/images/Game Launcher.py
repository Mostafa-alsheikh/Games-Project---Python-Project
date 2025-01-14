from tkinter import*
from tkinter import filedialog
import tkinter as tk 
from tkinter import messagebox
import tkinter
import os
import customtkinter
from PIL import Image,ImageTk


root = customtkinter.CTk()
root.title("Games launcher")
root.geometry("600x400")

photo = tk.PhotoImage(file = "app logo2.png")
root.wm_iconphoto(False, photo)

bkg = PhotoImage(file="app background.png")

label_1= Label(root, image=bkg)
label_1.place(x=0, y=0, relwidth=1, relheight=1)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
 
''''
def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system('"%s"' % my_program)
'''
#this define function to start game and you call it in button command   
# photo button icon

xo_image= PhotoImage(file = r"xo0.png")
tetris_image=PhotoImage(file = r"tetris22.png")
pingpong_image=PhotoImage(file = r"pingpong.png")
exit_image=PhotoImage(file=r"exit3.png")
def open_pingpong():
    messagebox.showinfo("Games launcher", "running PingPong ")
    os.startfile("c:\\Users\\kareem\\Desktop\\university data\\cs 102\\final project\\laucncher\\pingpong\\pingpong.exe")

def open_xo():
    messagebox.showinfo("Games launcher", "running XO ")
    os.startfile("c:\\Users\\kareem\\Desktop\\university data\\cs 102\\final project\\laucncher\\xo\\xo.exe")
def open_tetris():
    messagebox.showinfo("Games launcher", "running Tetris")
    os.startfile("c:\\Users\\kareem\\Desktop\\university data\\cs 102\\final project\\laucncher\\tetris\\T1.exe")
#this is the buttons            
XO_BUTTON= Button(root, text="XO", command=open_xo, image=xo_image)
XO_BUTTON.pack(pady=20,padx=20)
XO_BUTTON.place(x=50,y=150)
Ttetris_button = Button(root, text="Tetris", command=open_tetris,image=tetris_image)
Ttetris_button.pack(pady=20,padx=20)
Ttetris_button.place(x=375,y=150)
pingpong_button = Button(root, text="Tetris", command=open_pingpong,image=pingpong_image)
pingpong_button.pack(pady=20,padx=20)
pingpong_button.place(x=200,y=150)
exit_button = Button(root, text="exit", command=root.destroy,image=exit_image)
exit_button.pack(pady=20,padx=20)
exit_button.place(x=230,y=250)
root.mainloop()
