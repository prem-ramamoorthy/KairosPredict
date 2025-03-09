from tkinter import *
from tkinter import messagebox
import customtkinter as ctk 
from PIL import Image
from helper_functions_new import get_user ,verfiy_button
from change_password import open_otp_window

def open_reset_password(root , switch_event , switch_var , cancel ,  setup_ui):
    current_user = get_user()
    reset_password_window = ctk.CTkToplevel(root)
    reset_password_window.protocol("WM_DELETE_WINDOW", lambda: None)
    reset_password_window.title("KairosPredict/ResetPassword")
    reset_password_window.geometry("345x430")
    root.withdraw()
    footer = ctk.CTkFrame(reset_password_window, corner_radius=10, border_width=2, border_color="black")
    footer.grid(row=2, column=0, pady=3)
    ctk.CTkButton(footer, text="Cancel", command=lambda :cancel(reset_password_window, root , setup_ui) ,
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    switch = ctk.CTkSwitch(footer, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=20, padx= 15 ,sticky = "se")
    header = ctk.CTkFrame(reset_password_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    logo = ctk.CTkImage(light_image=Image.open(r"KairosPredict\static\images\logo.png"), 
                        dark_image=Image.open(r"KairosPredict\static\images\logo-w.png"),
                        size=(200, 60))
    ctk.CTkLabel(header, image=logo, text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    
    entry_frame = ctk.CTkFrame(reset_password_window, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row=1, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Reset Password", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Enter your username to reset password ", 
                 font=("Helvetica", 12, "bold")).grid(row=1, column=0, pady=10, padx=50)
    
    reset_user_entry = ctk.CTkEntry(entry_frame, placeholder_text="Username")
    reset_user_entry.bind("<Enter>", lambda e: reset_user_entry.configure(border_color="blue"))
    reset_user_entry.bind("<Leave>", lambda e: reset_user_entry.configure(border_color="grey"))
    reset_user_entry.grid(row=3, column=0, pady=15, padx=50) 

    ctk.CTkButton(entry_frame, text="Verify", command=lambda : verfiy_button(reset_user_entry.get() , open_otp_window , reset_password_window , root , setup_ui , switch_event , switch_var),
                  fg_color= "blue",hover_color= "#59BACC").grid(row=4, column=0, pady=10 , padx=40)