from tkinter import *
from tkinter import messagebox
import customtkinter as ctk 
from PIL import Image
from helper_functions_new import register_user
from images_ui import get_image

def open_register(root , switch_event , switch_var , cancel , setup_ui ):
    reg_window = ctk.CTkToplevel(root)
    reg_window.resizable(False, False)
    reg_window.protocol("WM_DELETE_WINDOW", lambda: None)
    root.withdraw()
    reg_window.title("KairosPredict/register")
    reg_window.geometry("345x580")
    
    header = ctk.CTkFrame(reg_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    switch = ctk.CTkSwitch(root, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=10, column=0, pady=30, padx=20 ,sticky = "se")
    
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 30, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=10 , padx=20)
    
    entry_frame = ctk.CTkFrame(reg_window, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row = 1 , column = 0 , pady=10)
    ctk.CTkLabel(entry_frame, text="Hello new user !!!", 
                 font=("Helvetica", 24, "bold")).grid(row = 0 , column = 0 , pady=3)
    
    reg_fname_entry = ctk.CTkEntry(entry_frame, placeholder_text="First Name")
    reg_fname_entry.bind("<Enter>", lambda e: reg_fname_entry.configure(border_color="blue"))
    reg_fname_entry.bind("<Leave>", lambda e: reg_fname_entry.configure(border_color="grey"))
    reg_fname_entry.grid(row=1, column=0, pady=3, padx=50)
    reg_fname_entry.bind("<Return>", lambda e: reg_lname_entry.focus_set())
    
    reg_lname_entry = ctk.CTkEntry(entry_frame, placeholder_text="Last Name")
    reg_lname_entry.bind("<Enter>", lambda e: reg_lname_entry.configure(border_color="blue"))
    reg_lname_entry.bind("<Leave>", lambda e: reg_lname_entry.configure(border_color="grey"))
    reg_lname_entry.grid(row=2, column=0, pady=3, padx=50)
    reg_lname_entry.bind("<Return>", lambda e: reg_email_entry.focus_set())
    
    reg_email_entry = ctk.CTkEntry(entry_frame, placeholder_text="Email")
    reg_email_entry.bind("<Enter>", lambda e: reg_email_entry.configure(border_color="blue"))
    reg_email_entry.bind("<Leave>", lambda e: reg_email_entry.configure(border_color="grey"))
    reg_email_entry.grid(row=3, column=0, pady=3, padx=50)
    reg_email_entry.bind("<Return>", lambda e: reg_phone_entry.focus_set())
    
    reg_phone_entry = ctk.CTkEntry(entry_frame, placeholder_text="Phone")
    reg_phone_entry.bind("<Enter>", lambda e: reg_phone_entry.configure(border_color="blue"))
    reg_phone_entry.bind("<Leave>", lambda e: reg_phone_entry.configure(border_color="grey"))
    reg_phone_entry.grid(row=4, column=0, pady=3, padx=50)
    reg_phone_entry.bind("<Return>", lambda e: reg_user_entry.focus_set())
    
    reg_user_entry = ctk.CTkEntry(entry_frame, placeholder_text="Username")
    reg_user_entry.bind("<Enter>", lambda e: reg_user_entry.configure(border_color="blue"))
    reg_user_entry.bind("<Leave>", lambda e: reg_user_entry.configure(border_color="grey"))
    reg_user_entry.grid(row=5, column=0, pady=3, padx=50)
    reg_user_entry.bind("<Return>", lambda e: reg_pass_entry.focus_set())
    
    reg_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="Password", show="*")
    reg_pass_entry.bind("<Enter>", lambda e: reg_pass_entry.configure(border_color="blue"))
    reg_pass_entry.bind("<Leave>", lambda e: reg_pass_entry.configure(border_color="grey"))
    reg_pass_entry.grid(row=6, column=0, pady=3, padx=90)
    reg_pass_entry.bind("<Return>", lambda e: reg_confirm_pass_entry.focus_set())
    
    reg_confirm_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="Confirm Password", show="*")
    reg_confirm_pass_entry.bind("<Enter>", lambda e: reg_confirm_pass_entry.configure(border_color="blue"))
    reg_confirm_pass_entry.bind("<Leave>", lambda e: reg_confirm_pass_entry.configure(border_color="grey"))
    reg_confirm_pass_entry.grid(row=7, column=0, pady=3, padx=50)
    reg_confirm_pass_entry.bind("<Return>", lambda e: register_user(root , reg_window , setup_ui ,\
            reg_user_entry.get(),reg_pass_entry.get() , reg_phone_entry.get() , reg_email_entry.get(),\
                  reg_fname_entry.get() , reg_lname_entry.get() ,  reg_confirm_pass_entry.get()))
    
    button_frame = ctk.CTkFrame(reg_window, corner_radius=10, border_width=2, border_color="black")
    button_frame.grid(row=2, column=0, pady=3 )
    ctk.CTkButton(button_frame, text="Create Account", command=lambda :register_user(root , reg_window , setup_ui \
        ,reg_user_entry.get(),reg_pass_entry.get() , reg_phone_entry.get() , reg_email_entry.get(),
          reg_fname_entry.get() , reg_lname_entry.get() ,  reg_confirm_pass_entry.get() ) ,
                  hover_color= "#59BACC").grid(row=0, column=0, pady=10, padx=10)
    ctk.CTkButton(button_frame, text="Cancel", command=lambda :cancel(reg_window, root , setup_ui) ,
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=1, pady=10, padx=10)

    switch = ctk.CTkSwitch(reg_window, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=3, column=0, pady=20, padx=20 ,sticky = "se")
