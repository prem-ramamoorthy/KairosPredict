from tkinter import *
from tkinter import messagebox
import customtkinter as ctk 
from PIL import Image
from helper_functions_new import get_user , change_password , verify_otp ,send_otp , cancel1
from images_ui import get_image

def open_change_password(root , cancel ,switch_event , switch_var , setup_ui):
    current_user = get_user()
    change_password_window = ctk.CTkToplevel(root)
    change_password_window.protocol("WM_DELETE_WINDOW", lambda: None)
    change_password_window.title("KairosPredict/ChangePassword")
    change_password_window.geometry("345x480+1500+500")
    root.withdraw()
    footer = ctk.CTkFrame(change_password_window, corner_radius=10, border_width=2, border_color="black")
    footer.grid(row=2, column=0, pady=3)
    ctk.CTkButton(footer, text="Cancel", command=lambda :cancel(change_password_window, root , setup_ui),
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    switch = ctk.CTkSwitch(footer, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=20, padx= 15 ,sticky = "se")
    header = ctk.CTkFrame(change_password_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 50, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    
    entry_frame = ctk.CTkFrame(change_password_window, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row=1, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Change Password", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=10 , padx=30)
    ctk.CTkLabel(entry_frame, text="Enter your new password :" ,
                 font=("Helvetica", 14, "bold")).grid(row=1, column=0, pady=10, padx=50 , sticky = "w")
    
    new_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="New Password", show="*")
    new_pass_entry.bind("<Enter>", lambda e: new_pass_entry.configure(border_color="blue"))
    new_pass_entry.bind("<Leave>", lambda e: new_pass_entry.configure(border_color="grey"))
    new_pass_entry.bind("<Return>" ,lambda e : confirm_new_pass_entry.focus() )
    new_pass_entry.grid(row=3, column=0, pady=15, padx= 70)

    confirm_new_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="Confirm New Password", show="*")
    confirm_new_pass_entry.bind("<Enter>", lambda e: confirm_new_pass_entry.configure(border_color="blue"))
    confirm_new_pass_entry.bind("<Leave>", lambda e: confirm_new_pass_entry.configure(border_color="grey"))
    confirm_new_pass_entry.bind("<Return>", lambda e: change_password(root , change_password_window ,setup_ui,current_user,new_pass_entry.get(),confirm_new_pass_entry.get()))
    confirm_new_pass_entry.grid(row=4, column=0, pady=15, padx=95)

    ctk.CTkButton(entry_frame, text="Change Password", command=lambda : change_password(root , change_password_window ,setup_ui,current_user,new_pass_entry.get(),confirm_new_pass_entry.get()),
                    fg_color= "blue",hover_color= "#59BACC").grid(row=5, column=0, pady=10 , padx=40)
    
def open_otp_window(root , cancel , setup_ui , switch_event , switch_var ,username):
    global otp_window, otp_entry 
    otp_window = ctk.CTkToplevel(root)
    otp_window.protocol("WM_DELETE_WINDOW", lambda: None)
    otp_window.title("KairosPredict/OTP")
    otp_window.geometry("345x430")
    root.withdraw()
    footer = ctk.CTkFrame(otp_window, corner_radius=10, border_width=2, border_color="black")
    footer.grid(row=2, column=0, pady=3)
    ctk.CTkButton(footer, text="Cancel", command=lambda :cancel(otp_window, root , setup_ui) ,
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    switch = ctk.CTkSwitch(footer, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=20, padx= 15 ,sticky = "se")
    header = ctk.CTkFrame(otp_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 40, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    
    entry_frame = ctk.CTkFrame(otp_window, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row=1, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Enter OTP", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Enter the OTP sent to your email" , 
                 font=("Helvetica", 14, "bold")).grid(row=1, column=0, pady=10, padx=55 , sticky="w")
    given_otp = send_otp(username)
    otp_entry = ctk.CTkEntry(entry_frame, placeholder_text="OTP")
    otp_entry.bind("<Enter>", lambda e: otp_entry.configure(border_color="blue"))
    otp_entry.bind("<Leave>", lambda e: otp_entry.configure(border_color="grey"))
    otp_entry.grid(row=2, column=0, pady=15, padx=50)
    ctk.CTkButton(entry_frame, text="Verify", command= lambda:verify_otp(given_otp , otp_entry.get() , otp_window , open_change_password , root ,switch_event , switch_var , setup_ui),
                  fg_color= "blue",hover_color= "#59BACC").grid(row=3, column=0, pady=10 , padx=40)
    
def open_change_password1(root , cancel ,switch_event , switch_var , setup_ui):
    current_user = get_user()
    change_password_window = ctk.CTkToplevel(root)
    change_password_window.protocol("WM_DELETE_WINDOW", lambda: None)
    change_password_window.title("KairosPredict/ChangePassword")
    change_password_window.geometry("345x480+1500+500")
    root.withdraw()
    footer = ctk.CTkFrame(change_password_window, corner_radius=10, border_width=2, border_color="black")
    footer.grid(row=2, column=0, pady=3)
    ctk.CTkButton(footer, text="Cancel", command=lambda :cancel1(change_password_window),
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    switch = ctk.CTkSwitch(footer, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=20, padx= 15 ,sticky = "se")
    header = ctk.CTkFrame(change_password_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 30, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    
    entry_frame = ctk.CTkFrame(change_password_window, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row=1, column=0, pady=10)
    ctk.CTkLabel(entry_frame, text="Change Password", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=10 , padx=30)
    ctk.CTkLabel(entry_frame, text="Enter your new password :" ,
                 font=("Helvetica", 14, "bold")).grid(row=1, column=0, pady=10, padx=50 , sticky = "w")
    
    new_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="New Password", show="*")
    new_pass_entry.bind("<Enter>", lambda e: new_pass_entry.configure(border_color="blue"))
    new_pass_entry.bind("<Leave>", lambda e: new_pass_entry.configure(border_color="grey"))
    new_pass_entry.bind("<Return>" ,lambda e : confirm_new_pass_entry.focus() )
    new_pass_entry.grid(row=3, column=0, pady=15, padx= 70)

    confirm_new_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="Confirm New Password", show="*")
    confirm_new_pass_entry.bind("<Enter>", lambda e: confirm_new_pass_entry.configure(border_color="blue"))
    confirm_new_pass_entry.bind("<Leave>", lambda e: confirm_new_pass_entry.configure(border_color="grey"))
    confirm_new_pass_entry.bind("<Return>", lambda e: change_password(root , change_password_window ,setup_ui,current_user,new_pass_entry.get(),confirm_new_pass_entry.get()))
    confirm_new_pass_entry.grid(row=4, column=0, pady=15, padx=95)

    ctk.CTkButton(entry_frame, text="Change Password", command=lambda : change_password(root , change_password_window ,setup_ui,current_user,new_pass_entry.get(),confirm_new_pass_entry.get()),
                    fg_color= "blue",hover_color= "#59BACC").grid(row=5, column=0, pady=10 , padx=40)