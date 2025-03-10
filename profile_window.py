from tkinter import *
import customtkinter as ctk 
from PIL import Image

def greet_user(root , switch_event , switch_var , l):
    greet_window = ctk.CTkToplevel(root)
    greet_window.title("KairosPredict/GreetUser")
    length = len(l[2]+l[3])
    greet_window.geometry("{}x375+1500+500".format(440+length))
    header = ctk.CTkFrame(greet_window ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=10, sticky="ew")
    switch = ctk.CTkSwitch(greet_window, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=10, column=0, pady=10, padx=10 , sticky = "w")
    logo = ctk.CTkImage(light_image=Image.open(r"KairosPredict\static\images\logo.png"), 
                        dark_image=Image.open(r"KairosPredict\static\images\logo-w.png"),
                        size=(200, 60))
    ctk.CTkLabel(header, image=logo, text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 , sticky = "ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20 , sticky = "ew")
    header.grid_columnconfigure(0, weight=1)
    main_frame = ctk.CTkFrame(greet_window, corner_radius=20, border_width=2, border_color="black" , height= 300 , width = 300 )
    main_frame.grid(row=1, column=0, pady=3 , padx=10)

    ctk.CTkLabel(main_frame , text="Hello {} ! Here's your profile at a glance:".format(l[2]+" " +l[3]),font=("Helvetica", 15, "bold", "italic")).grid(row =0 , column = 0 , padx = 10 ,pady= 10)
    ctk.CTkLabel(main_frame , text="User_name     : {}".format(l[1]),font=("arial", 16, "bold")).grid(row =1, column = 0 , padx = 100 ,pady= 2)
    ctk.CTkLabel(main_frame , text="First_name    : {}".format(l[2]),font=("arial", 16, "bold")).grid(row =2 , column = 0 , padx = 100 ,pady= 2)
    ctk.CTkLabel(main_frame , text="Last_name     : {}".format(l[3]),font=("arial", 16, "bold")).grid(row =3 , column = 0 , padx = 100 ,pady= 2)
    ctk.CTkLabel(main_frame , text="Email_address : {}".format(l[0]),font=("arial", 16, "bold")).grid(row =4 , column = 0 , padx = 10 ,pady= 2)
    ctk.CTkLabel(main_frame , text="Phone_number  : {}".format(l[4]),font=("arial", 16, "bold")).grid(row =5 , column = 0 , padx = 100 ,pady= 2)