from tkinter import *
import customtkinter as ctk 
from PIL import Image
from images_ui import get_image

def open_about_us(root ,switch_event , switch_var , cancel , setup_ui):
    root.withdraw()
    about_us_window = ctk.CTkToplevel(root)
    about_us_window.protocol("WM_DELETE_WINDOW", lambda: None)
    about_us_window.title("About Us")
    about_us_window.geometry("410x600")
    header = ctk.CTkFrame(about_us_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=10, sticky="ew")
    button_frame = ctk.CTkFrame(about_us_window, corner_radius=10, border_width=2, border_color="black")
    button_frame.grid(row=3, column=0, pady=3 , padx=10)
    switch = ctk.CTkSwitch(button_frame, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=10, padx=42)
    ctk.CTkButton(button_frame, text="Cancel", command=lambda :cancel(about_us_window , root , setup_ui) ,
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 50, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    about_us_frame = ctk.CTkFrame(about_us_window, corner_radius=10, border_width=2, border_color="black")
    about_us_frame.grid(row=1, column=0, pady=3 , padx=10)
    ctk.CTkLabel(about_us_frame, text="About Us", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=3)
    about_us_text = ("🔹 KairosPredict is a platform that provides\n         smart predictions for stock analysis.\n"
                     "🔹 We aim to empower users with data-driven \n         decisions and insights to make informed\n           choices in the stock market.\n"
                     "🔹 Our platform uses machine learning \n             algorithms to analyze historical stock \n                  data and predict future stock prices.\n"
                     "🔹 We believe in simplifying the stock analysis \n      process and providing accurate predictions \n        to help users maximize their returns.\n"
                     "🔹 Join us on this journey of making smarter \n        decisions with KairosPredict.")
    
    about_us_textbox = ctk.CTkTextbox(about_us_frame, height=250, width=350, wrap="word" , font=("Arial", 15 , "bold"),
                                     border_color= "black" , corner_radius= 10, border_width= 2 )
    about_us_textbox.insert("1.0", about_us_text)
    about_us_textbox.configure(state="disabled")
    about_us_textbox.grid(row=1, column=0, pady=10, padx=20)

    team_frame = ctk.CTkFrame(about_us_window, corner_radius=10, border_width=2, border_color="black")
    team_frame.grid(row=2, column=0, pady=3 , padx=10)
    ctk.CTkLabel(team_frame, text="Meet the Team :", 
                 font=("Helvetica", 18, "bold")).grid(row=0, column=0, pady=5 , sticky="w", padx=125)
    ctk.CTkLabel(team_frame, text="👤 Prem Kumar R - CEO & Founder\n👤 Akash S - Lead Data Scientist",
                    font=("Helvetica", 14, "bold")).grid(row=1, column=0, pady=10 , padx =10)