import customtkinter as ctk
from tkinter import *
from PIL import Image
from helper_functions_new import *
from contact_us import open_contact_us_window
from profile_window import greet_user
from chart_config_window import chart_config
from change_password import open_change_password1
from reset_password import open_reset_password
from about_us_window import open_about_us
from tradingview_ta import TA_Handler , Interval
from register_window import open_register
from chart_maker import plot_advanced_candlestick
import matplotlib.pyplot as plt
import pandas as pd
from color_inverter import invert_color
from images_ui import get_image


fig, (ax_candle, ax_volume) = plt.subplots(2, 1, figsize=(8.5,4), gridspec_kw={'height_ratios': [5, 1]})

def get_stock_analysis(selected_stock): 
    set_stock_detail(selected_stock)
    try :
        handler = TA_Handler(
            symbol=selected_stock,
            screener="america",
            exchange="NASDAQ",
            interval=Interval.INTERVAL_1_DAY
        )
        analysis = handler.get_analysis()
        analysts_analysis = analysis.summary
        if analysts_analysis:
            data = ""
            first = True
            for key, value in analysts_analysis.items():
                if first:
                    analysts_analysis = value
                    first = False
                else:
                    data += f"{key}: {value} | "
            data = f"{analysts_analysis}-> " + data
            if len(data) < 50:
                padding = (50 - len(data)) // 2
                data = ' ' * padding + data + ' ' * padding
            analysis_label.grid(row=0, column=3, pady=3, padx=10)
            temp_lable.grid_remove()
            analysis_label.configure(text=data)
            timeframe_label.grid(row=2, column=2, pady=3 , sticky= "nw")
            time_frame_button.grid(row=2, column=3, pady=3 , sticky= "nw")
        else:
            analysis_label.configure(text=f"⚠️ No data available")
    except Exception as e :
        analysis_label.configure(text=f"⚠️ Error: {str(e)}")

def clear_figures():
    global ax_candle , ax_volume , fig
    ax_candle.clear()
    ax_volume.clear()
    fig, (ax_candle, ax_volume) = plt.subplots(2, 1, figsize=(8.5, 4), gridspec_kw={'height_ratios': [5, 1]})

def open_stock_ui():
    global analysis_label , temp_lable ,  profile_button , chart_edit_button, settings_button, logout_button,\
        time_frame_button , timeframe_label , show_chart_button , main_body_frame
    
    list_of_details = get_user_details()
    stock_window = ctk.CTkToplevel(root)
    stock_window.protocol("WM_DELETE_WINDOW", lambda: None)
    root.withdraw()
    stock_window.title("KairosPredict/StockAnalysis")
    stock_window.geometry("880x765+0+0")

    header = ctk.CTkFrame(stock_window  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=10, sticky="ew")
    switch = ctk.CTkSwitch(stock_window, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=10, column=0, pady=10, padx=20 ,sticky = "se" )
    
    ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold")).grid(row=1, column=0, pady=1, padx=20, sticky="ew")
    header.grid_columnconfigure(0, weight=1)
    
    body_header = ctk.CTkFrame(stock_window, corner_radius=10, border_width=2, border_color="black")
    body_header.grid(row=1, column=0, pady=3 , padx= 10, sticky="ew")

    profile_image_light = make_circle(Image.open(r"static\profiles\{}.png".format(get_profile_letter())).convert("RGBA"))
    profile_image_dark = make_circle(Image.open(r"static\profiles\{}-w.png".format(get_profile_letter())).convert("RGBA"))

    profile_image = ctk.CTkImage(light_image=profile_image_light,
                                    dark_image=profile_image_dark,
                                    size=(35,35))
    ctk.CTkLabel(body_header, text="Stock Analysis",
                 font=("Helvetica", 20, "bold")).grid(row=0, column=1, pady=3 , padx = 200 ,sticky="ew") 
    profile_button = ctk.CTkButton(body_header, image=profile_image, text="",
                 compound="top", fg_color="transparent", command=lambda :greet_user(root,switch_event,switch_var,list_of_details), width=50,
                )
    profile_button.grid(row=0, column=20, pady=5, padx=1, sticky="e")
    logout_button = ctk.CTkButton(body_header, image=get_image("logout_image"), text="Logout", font=("Helvetica", 10, "bold"),
                  hover_color="grey", fg_color="transparent", text_color= "black",
                  compound="top", command=lambda : cancel(stock_window, root , setup_ui), width=50)
    logout_button.grid(row=0, column=21, pady=5, padx=5, sticky="ew")
    settings_button = ctk.CTkButton(body_header, image=get_image("settings_image"), text="changePass", font=("Helvetica", 10, "bold"),
                  hover_color="grey", fg_color="transparent", text_color= "black",
                  compound="top", command=lambda :open_change_password1(root ,cancel ,switch_event , switch_var , setup_ui ), width=50)
    settings_button.grid(row=0, column=22, pady=5, padx=5, sticky="ew")

    element_frame = ctk.CTkFrame(stock_window, corner_radius=10, border_width=2, border_color="black")
    element_frame.grid(row=2, column=0, pady=3 , padx=10, sticky="ew")
    ctk.CTkLabel(element_frame, text="Select Stock Symbol", font=("Helvetica", 14, "bold")).grid(row=0, column=0, pady=3, padx=10)
    stock_symbol = ctk.CTkComboBox(element_frame, values=["AAPL", "GOOGL", "AMZN", "TSLA"] , command = get_stock_analysis)
    stock_symbol.grid(row=0, column=1, pady=3, padx=10 , sticky = "w")
    ctk.CTkLabel(element_frame, text="Analyst's Analysis :", font=("Helvetica", 14, "bold")).grid(row=0, column=2, pady=3, padx=10)
    temp_lable = ctk.CTkLabel(element_frame, text="", font=("Helvetica", 14, "bold"))
    temp_lable.grid(row=0, column=3, pady=3, padx=10)
    analysis_label = ctk.CTkLabel(element_frame, text=" <<<  your Recomendation will display here  >>>", font=("Helvetica", 14, "bold"))
    analysis_label.grid(row=0, column=3, pady=3)
    ctk.CTkLabel(element_frame, text="Plot Style", font=("Helvetica", 14, "bold")).grid(row=2, column=0, pady=3, padx=10)
    plot_style = ctk.CTkComboBox(element_frame, values=["Candlestick chart","Line chart","OHLC chart" ,"Renko Chart" ,"⚠️Point and Figure Chart"] , command= set_chart_style)
    plot_style.grid(row=2, column=1, pady=3, padx=10)
    time_frame_button_var = ctk.StringVar(value=" 1d ")
    timeframe_label = ctk.CTkLabel(element_frame, text="Select TimeFrame :", font=("Helvetica", 14, "bold"))
    timeframe_label.grid(row = 2 , column = 2, pady=3, padx=10 , sticky = "w")
    time_frame_button = ctk.CTkSegmentedButton(element_frame, values=[" 1m ", " 5m ", " 15m ", " 30m ", " 1h ", " 1d "],
                                               command=segmented_button_callback,
                                               variable=time_frame_button_var,
                                               corner_radius=10,
                                               border_width=2,
                                               bg_color="#CFCFCF" if ctk.get_appearance_mode() == "light" else "transparent",
                                               text_color="black" if ctk.get_appearance_mode() == "light" else "white",
                                               text_color_disabled="black" if ctk.get_appearance_mode() == "light" else "white"
                                               )
    time_frame_button.grid(row=2, column=3, pady=10 , padx = 30)
    main_body_frame = ctk.CTkFrame(stock_window, corner_radius=10, border_width=2, border_color="black" , height= 400 , width= 860 )
    main_body_frame.grid(row = 3 , column = 0 , pady = 10 , padx = 10 )
    show_chart_button = ctk.CTkButton(element_frame, text="Plot",height=30 ,  
                                      border_color="black", border_width=2, text_color= "black" ,
                                      corner_radius=30, font=("Arial", 16, "bold"),fg_color="transparent",
                                        hover_color="gray", width=50 , command= lambda : plot_advanced_candlestick(ax_candle ,ax_volume , fig , main_body_frame , clear_figures() , get_chart_style() , get_time_frame() , get_stock_detail()))
    show_chart_button.grid(row=3, column=2, pady=10, padx= 10, sticky="ew")

    chart_edit_button = ctk.CTkButton(body_header, image=get_image("chart_edit_image"), text="Edit chart", font=("Helvetica", 10, "bold"),
                  hover_color="grey", fg_color="transparent", text_color= "black",
                  compound="top", command=lambda: chart_config(root, switch_event, switch_var), width=50)
    chart_edit_button.grid(row=0, column=23, pady=5, padx=5, sticky="ew")

def switch_event():
    try : 
        chart_config = load_colors("chart_configuration")
        inverted= invert_color(chart_config)
        save_colors("chart_configuration", inverted ,None)
        if ctk.get_appearance_mode() == "Dark":
            show_chart_button.configure(text_color = "black" , border_color = "black")
            logout_button.configure(text_color = "black")
            settings_button.configure(text_color = "black")
            chart_edit_button.configure(text_color = "black")
            profile_button.configure(hover_color ="#335878")
        else :
            show_chart_button.configure(text_color = "white" , border_color = "white")
            chart_edit_button.configure(text_color = "white")
            logout_button.configure(text_color = "white")
            settings_button.configure(text_color = "white")
            profile_button.configure(hover_color = "#CCA787")
    except Exception as e:
            pass
    try:
        plot_advanced_candlestick(ax_candle ,ax_volume , fig , main_body_frame , clear_figures() , get_chart_style() , get_time_frame() , get_stock_detail())
    except Exception as e:
        pass
    ctk.set_appearance_mode("light") if switch_var.get() == "on" else ctk.set_appearance_mode("dark")

def setup_ui():
    global switch_var
    header = ctk.CTkFrame(root  ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=5, sticky="ew")
    switch_var = ctk.StringVar(value="on")
    switch = ctk.CTkSwitch(root, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=10, column=0, pady=20, padx=20 ,sticky = "se")
    
    ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20)

    entry_frame = ctk.CTkFrame(root, corner_radius=10, border_width=2, border_color="black")
    entry_frame.grid(row=1, column=0, pady=3)
    ctk.CTkLabel(entry_frame, text="Hello User !!!", 
                 font=("Helvetica", 24, "bold")).grid(row=0, column=0, pady=3)

    login_user_entry = ctk.CTkEntry(entry_frame, placeholder_text="Username")
    login_user_entry.bind("<Enter>", lambda e: login_user_entry.configure(border_color="blue"))
    login_user_entry.bind("<Leave>", lambda e: login_user_entry.configure(border_color="grey"))
    login_user_entry.grid(row=1, column=0, pady=10, padx=90)
    try :
        login_user_entry.bind("<Return>", lambda e: login_pass_entry.focus_set())
    except IndexError as e :
        messagebox.showwarning("Entry Warning !" , "Values required for Entry fields !")

    login_pass_entry = ctk.CTkEntry(entry_frame, placeholder_text="Password", show="*")
    login_pass_entry.bind("<Enter>", lambda e: login_pass_entry.configure(border_color="blue"))
    login_pass_entry.bind("<Leave>", lambda e: login_pass_entry.configure(border_color="grey"))
    login_pass_entry.grid(row=2, column=0, pady=10, padx=50)

    button_frame = ctk.CTkFrame(root, corner_radius=10, border_width=2, border_color="black")
    button_frame.grid(row=4, column=0, pady=3)
    login_pass_entry.bind("<Return>", lambda e: login_user(login_user_entry.get() , login_pass_entry.get() , open_stock_ui))

    ctk.CTkButton(button_frame, text="Login", command=lambda :login_user(login_user_entry.get() , login_pass_entry.get() , open_stock_ui)
                  ,hover_color= "#59BACC").grid(row=0, column=0, pady=10 , padx=10)
    ctk.CTkButton(button_frame, text="Register", command=lambda :open_register(root , switch_event , switch_var , cancel , setup_ui ) ,
                   fg_color= "#58AD69" , hover_color="#59BACC" ).grid(row=0, 
                                                                      column=1, pady=10   , padx=10)

    extra_frame = ctk.CTkFrame(root, corner_radius=10, border_width=2, border_color="black")
    extra_frame.grid(row=5, column=0, pady=3)
    ctk.CTkLabel(extra_frame, text="Forgot Password?", 
                 font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=5, padx=35)
    ctk.CTkButton(extra_frame, text="Reset Password" , 
                  text_color= "blue",fg_color= "transparent", 
                  hover_color="#d4f1f4" , command=lambda :open_reset_password(root , switch_event , switch_var , cancel ,  setup_ui)\
                  ).grid(row=0, column=1, pady= 5 , padx = 5 )
    ctk.CTkButton(extra_frame, text="Contact Support",
                   text_color= "blue", fg_color= "transparent",
                     hover_color="#d4f1f4" , command=lambda :open_contact_us_window(root , switch_event , switch_var , cancel, setup_ui)).grid(row=1,column=0, pady=5 ,padx = 5)
    ctk.CTkButton(extra_frame, text="About Us", text_color= "blue",
                   fg_color= "transparent" , hover_color="#d4f1f4" , command=lambda : open_about_us(root ,switch_event , switch_var , cancel , setup_ui)\
                   ).grid(row=1, column=1, pady=5 , padx = 5 )
    
    sign_in_frame = ctk.CTkFrame(root, corner_radius=10, border_width=2, border_color="black")
    sign_in_frame.grid(row=6, column=0, pady=3)
    ctk.CTkLabel(sign_in_frame, text="Follow us on  :", 
                 font=("Helvetica", 12, "bold")).grid(row=0, column=0, pady=3, padx=50)
    ctk.CTkButton(sign_in_frame, image=get_image("github" ), 
                  fg_color= "transparent" , hover_color= "grey", 
                  text= "" ,command= open_github).grid(row=1, column=0, pady=3, padx=10)
    ctk.CTkButton(sign_in_frame, image=get_image("facebook"),
                  fg_color= "transparent", hover_color= "grey", 
                  text= "" , command= open_facebook).grid(row=1, column=1, pady=3,padx =3 )
    ctk.CTkButton(sign_in_frame, image=get_image("linkedin"),
                  fg_color= "transparent", hover_color= "grey", 
                  text= "" , command= open_linkedin).grid(row=2, column=0, pady=3, padx=10)
    ctk.CTkButton(sign_in_frame, image=get_image("instagram"),
                  fg_color= "transparent", hover_color= "grey", 
                  text= "" , command= open_insta).grid(row=2, column=1, pady=3, padx=3)

def get_back_to_light_mode():
    if ctk.get_appearance_mode() == "Dark":
        switch_event()
    else :
        None

def fade_out_close(alpha=1.0):
    if alpha > 0:
        root.attributes("-alpha", alpha)
        root.after(50, fade_out_close, alpha - 0.05)
    else:
        get_back_to_light_mode()
        root.destroy()

if __name__ == "__main__" :
    root = ctk.CTk()
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")
    root.title("KairosPredict/login")
    root.geometry("345x580")
    root.protocol("WM_DELETE_WINDOW", lambda: fade_out_close())   
    root.iconbitmap(r"static\images\icon.ico")
    setup_ui()
    current_user = get_user()
    root.mainloop()