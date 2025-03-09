import customtkinter as ctk 
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def open_contact_us_window(root , switch_event , switch_var , cancel ,setup_ui):
    def submit_feedback():
        feedback = feedback_entry.get("1.0", END).strip()
        if feedback:
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
            feedback_entry.delete("1.0", END)
        else:
            messagebox.showwarning("Empty Feedback", "Please enter your feedback before submitting ")
    contact_us_window = ctk.CTkToplevel(root)
    contact_us_window.protocol("WM_DELETE_WINDOW", lambda: None)
    button_frame = ctk.CTkFrame(contact_us_window, corner_radius=10, border_width=2, border_color="black")
    button_frame.grid(row=3, column=0, pady=3 , padx=10)
    switch = ctk.CTkSwitch(button_frame, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=0, column=1, pady=10, padx=10)
    contact_us_window.title("KairosPredict/Contact Us")
    root.withdraw()
    contact_us_window.geometry("370x650")
    ctk.CTkButton(button_frame, text="Cancel", command=lambda :cancel(contact_us_window , root , setup_ui) ,
                  fg_color= "red",hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=40)
    contact_us_frame_header = ctk.CTkFrame(contact_us_window, corner_radius=10, border_width=2, border_color="black")
    contact_us_frame_header.grid(row=0, column=0, pady=10 , padx=10)
    logo = ctk.CTkImage(light_image=Image.open(r"static\images\logo.png"), 
                        dark_image=Image.open(r"static\images\logo-w.png"),
                        size=(200, 60))
    ctk.CTkLabel(contact_us_frame_header, image=logo, text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    ctk.CTkLabel(contact_us_frame_header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)
    feed_back_body = ctk.CTkFrame(contact_us_window, corner_radius=10, border_width=2, border_color="black")
    feed_back_body.grid(row=1, column=0, pady=10 , padx = 20)
    contact_us_frame_body = ctk.CTkFrame(contact_us_window, corner_radius=10, border_width=2, border_color="black")
    contact_us_frame_body.grid(row=2, column=0, pady=10 , padx = 20)
    ctk.CTkLabel(feed_back_body, text="Feedback", font=("Arial", 18, "bold") ).grid(row=0, column=0, pady=10 , padx=10)
    feedback_entry = ctk.CTkTextbox(feed_back_body, height= 150, width=250 ,
                                     border_color= "black" , corner_radius= 10, border_width= 2 )
    feedback_entry.grid(row=2, column=0, pady=10 , padx= 40)
    feedback_entry.bind("<Return>" , lambda e : submit_feedback())
    ctk.CTkButton(feed_back_body, text="Submit Feedback", command=submit_feedback, corner_radius= 20,
                  fg_color="blue",hover_color= "grey" ).grid(row=3, column=0, pady=10, padx=10)
    ctk.CTkLabel(contact_us_frame_body, text="Contact Info", font=("Arial", 18, "bold")).grid(row=4, column=0, pady= 3, padx=10)
    email_heading = ctk.CTkLabel(contact_us_frame_body, text="Email :", font=("Arial", 14, "bold"))
    email_heading.grid(row=5, column=0, pady=3, padx=10 , sticky="w")
    email = ctk.CTkLabel(contact_us_frame_body, text="Kairospredict@gmail.com", font=("Arial", 13, "bold"))
    email.grid(row=5, column=1, pady= 3, padx=10 , sticky="w")
    phone_heading = ctk.CTkLabel(contact_us_frame_body, text="Phone :", font=("Arial", 14, "bold"))
    phone_heading.grid(row=7, column=0, pady=3, padx=10 , sticky="w")
    phone = ctk.CTkLabel(contact_us_frame_body, text="+91-6380498136", font=("Arial", 13, "bold"))
    phone.grid(row=7, column=1, pady=3, padx=10)
    address_heading = ctk.CTkLabel(contact_us_frame_body, text="Address :", font=("Arial", 14, "bold"))
    address_heading.grid(row=9, column=0, pady=3, padx=10 , sticky="w")
    address = ctk.CTkLabel(contact_us_frame_body, text="VIT Bhopal , Sehore ,\n MadhyaPradesh .", font=("Arial", 13, "bold"))
    address.grid(row=9, column=1, pady=3, padx= 30 , sticky="sw")