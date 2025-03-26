from tkinter import *
from tkinter import messagebox
import customtkinter as ctk 
from PIL import Image, ImageTk, ImageDraw
from helper_functions_new import save_colors,chart_style1 , pick_color , reset , get_list
from images_ui import get_image

def chart_config(root, switch_event , switch_var):
    global chart_edit_window
    list_of_select_colors = get_list()
    chart_edit_window = ctk.CTkToplevel(root)
    chart_edit_window.title("KairosPredict/char-configuration")
    chart_edit_window.resizable(False, False)
    chart_edit_window.protocol("WM_DELETE_WINDOW", lambda: None)
    chart_edit_window.geometry("620x465+1500+500")
    header = ctk.CTkFrame(chart_edit_window ,corner_radius= 20, border_width= 2, border_color= "black")
    header.grid(row=0, column=0, pady=3, padx=10, sticky="ew")
    switch = ctk.CTkSwitch(chart_edit_window, text="Theme", command=switch_event,
                           variable=switch_var, onvalue="on", 
                           offvalue="off", height= 10, width = 20)
    switch.grid(row=10, column=0, pady=10, padx=10 , sticky = "w")
    try :
        ctk.CTkLabel(header, image=get_image("logo"), text="" , compound= "left").grid(row=0, column=0 , pady=10 , padx=5 )
    except Exception as e :
        ctk.CTkLabel(header,text="KairosPredict", font=("Times New Roman", 50, "bold"), compound= "left").grid(row=0, column=0, pady=3, padx=50, sticky="ew")
    ctk.CTkLabel(header, text="Empowering Decisions with Smart Predictions.",
                 font=("Helvetica", 13, "bold") ).grid(row=1, column=0, pady=5 , padx=20 , sticky = "ew")
    header.grid_columnconfigure(0, weight=1)
    main_frame = ctk.CTkFrame(chart_edit_window, corner_radius=20, border_width=2, border_color="black" , height= 300 , width = 300 )
    main_frame.grid(row=1, column=0, pady=3 , padx=10)

    ctk.CTkLabel(main_frame , text = "Bullish color").grid(row = 0 , column= 0 , padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Bearish color").grid(row = 0 , column= 2, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Wick up color").grid(row = 1 , column= 0, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Wick down color").grid(row = 1 , column= 2, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Bearish edge color").grid(row = 2 , column= 0, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Bullish edge color").grid(row = 2 , column= 2, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Volume Up color").grid(row = 3 , column= 0, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Moving Avg Line").grid(row = 3 , column= 2, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Background color ").grid(row = 4 , column= 0, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Edge color").grid(row = 4 , column= 2, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Grid color").grid(row = 5 , column= 0, padx = 5 , pady= 5)
    ctk.CTkLabel(main_frame , text = "Select the grid Style").grid(row = 5 , column= 2, padx = 5 , pady= 5)
    grid_style = ctk.CTkComboBox(main_frame , values= ["Solid line", "Dashed line" , "Dash-dot line" , "Dotted line" , "No grid"] , command= chart_style1)
    grid_style.set(list_of_select_colors[11])
    grid_style.grid(row = 5 , column = 3 , padx = 10 , pady = 10 , sticky = "w")
    up_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[0], command=lambda :pick_color(up_color_button , 0))
    up_color_button.grid(row = 0 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    down_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black", corner_radius=60,width=20, height=20, fg_color=list_of_select_colors[1], command=lambda :pick_color(down_color_button, 1))
    down_color_button.grid(row = 0 , column = 3, padx = 10 , pady = 10 , sticky = "w")
    wick_up_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black", corner_radius=60,width=20, height=20, fg_color=list_of_select_colors[2], command=lambda :pick_color( wick_up_color_button , 2))
    wick_up_color_button.grid(row = 1 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    wick_down_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[3], command=lambda :pick_color(wick_down_color_button , 3))
    wick_down_color_button.grid(row = 1 , column = 3 , padx = 10 , pady = 10 , sticky = "w")
    up_edge_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[4], command=lambda :pick_color(up_edge_color_button , 4))
    up_edge_color_button.grid(row = 2 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    down_edge_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[5], command=lambda :pick_color(down_edge_color_button , 5))
    down_edge_color_button.grid(row = 2 , column = 3 , padx = 10 , pady = 10 , sticky = "w")
    up_volume_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[6], command=lambda :pick_color(up_volume_color_button , 6))
    up_volume_color_button.grid(row = 3 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    mvg_avg_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[7], command=lambda :pick_color(mvg_avg_color_button , 7))
    mvg_avg_color_button.grid(row = 3 , column = 3 , padx = 10 , pady = 10 , sticky = "w")
    background_color_button = ctk.CTkButton(main_frame, text="" ,corner_radius=60,border_width=1,border_color="black", width=20, height=20, fg_color=list_of_select_colors[8], command=lambda :pick_color(background_color_button , 8))
    background_color_button.grid(row = 4 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    edge_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black", corner_radius=60,width=20, height=20, fg_color=list_of_select_colors[9], command=lambda :pick_color(edge_color_button , 9))
    edge_color_button.grid(row = 4 , column = 3 , padx = 10 , pady = 10 , sticky = "w")
    grid_color_button = ctk.CTkButton(main_frame, text="" ,border_width=1,border_color="black",corner_radius=60, width=20, height=20, fg_color=list_of_select_colors[10], command=lambda :pick_color(grid_color_button , 10))
    grid_color_button.grid(row = 5 , column = 1 , padx = 10 , pady = 10 , sticky = "w")
    submit_button = ctk.CTkButton(main_frame, text="Submit/Exit" ,text_color="white",fg_color="gray",border_color="black",border_width= 1 , hover_color= "gray" , command=lambda :save_colors("chart_configuration" , list_of_select_colors, chart_edit_window))
    submit_button.grid(row = 6 , column = 1 , padx = 10 , pady = 10 , sticky = "ew")
    reset_button = ctk.CTkButton(main_frame, text="Reset" ,text_color="white",fg_color="gray",border_color="black",border_width= 1 , hover_color= "gray" , command=lambda :reset(chart_edit_window))
    reset_button.grid(row = 6 , column = 2, padx = 10 , pady = 10 , sticky = "ew")
    