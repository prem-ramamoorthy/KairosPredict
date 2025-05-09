from tkinter import *
from tkinter import messagebox, colorchooser
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk, ImageDraw
import hashlib
import sqlite3
import webbrowser
import customtkinter as ctk
import json
import smtplib
import ssl
from email.message import EmailMessage
import re
from clustering import main

def set_visualization(value):
    global visualization
    visualization = value

def get_visualization():
    global visualization
    return visualization

def set_chart_style(value):
    global chart_style 
    candle_styles = {
        "Candlestick chart": "candle",
        "Line chart": "line",
        "OHLC chart": "ohlc",
        "Renko Chart": "renko",
        "⚠️Point and Figure Chart" : "pnf"
    }
    selected_candle_style = candle_styles.get(value,"candle")
    chart_style = selected_candle_style

def get_chart_style():
    global chart_style
    return chart_style

def submit_feedback(feedback_entry):
        feedback = feedback_entry.get("1.0", END).strip()
        if feedback:
            send_email("kairospredict@gmail.com" , feedback)
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
            feedback_entry.delete("1.0", END)
        else:
            messagebox.showwarning("Empty Feedback", "Please enter your feedback before submitting ")

def segmented_button_callback(value):
    global timeframe
    timeframe = value

def get_time_frame():
    global timeframe
    return timeframe

def cancel(windowname , root , setup_ui):
    global is_stock_window_opened
    windowname.destroy()
    root.deiconify()
    setup_ui()

def cancel1(windowname):
    windowname.destroy()

def update_profile_letter(l):
    global profile_letter 
    profile_letter = l

def get_profile_letter():
    global profile_letter 
    return profile_letter

def update_user_details(username_detail , first_name_detail , last_name_detail , email_detail , phone_detail):
    global username , first_name , last_name , email , phone 
    username = username_detail 
    first_name = first_name_detail
    last_name = last_name_detail 
    email = email_detail 
    phone = phone_detail

def get_user_details():
    global username , first_name , last_name , email , phone 
    return [email,username,first_name,last_name,phone]

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True, "Valid email address."
    else:
        return False, "Invalid email address."

def is_valid_phone_number(phone):
    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{4}$"
    if re.match(pattern, phone):
        return True, "Valid phone number."
    else:
        return False, "Invalid phone number."

def register_user(root , reg_window , setup_ui ,username , password , phone , email , first_name , last_name , confirm_password ):
    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror("Error", "All fields are required")
        return
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return
    value3 = is_valid_phone_number(phone)
    if not value3[0]:
        messagebox.showwarning("Error" , value3[1])
        return
    value1 = is_valid_email(email)
    if not value1[0]:
        messagebox.showwarning("Error" , value1[1])
        return
    value = is_valid_password(password)
    if not value[0]:
        messagebox.showwarning("Error" , value[1])
        return
    hashed_password = hash_password(password)
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        cursor.execute("INSERT INTO users_data (username, first_name, last_name, email, phone) VALUES (?, ?, ?, ?, ?)", (username, first_name, last_name, email, phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration Successful")
        root.deiconify()
        setup_ui()
        reg_window.destroy()
    except sqlite3.IntegrityError :
        messagebox.showerror("Error", "Username already exists")

def save_colors(filename, colors , chart_edit_window):
    with open(filename, 'w') as file:
        json.dump(colors, file, indent=4)
    try : 
        chart_edit_window.destroy()
    except Exception as e :
        pass

def get_list():
    global list_of_select_colors
    return list_of_select_colors

def load_colors(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] 

def open_insta():
    url = "https://www.instagram.com/"
    webbrowser.open(url)

def open_twitter():
    url = "https://twitter.com/"
    webbrowser.open(url)

def open_website():
    url = "https://www.kairospredict.com/"
    webbrowser.open(url)

def open_linkedin():
    url = "https://www.linkedin.com/in/premramamoorthy/"
    webbrowser.open(url)

def open_facebook():
    url = "https://www.facebook.com/"
    webbrowser.open(url)

def open_github():
    url = "https://github.com/prem-ramamoorthy/"
    webbrowser.open(url)

def resizer(path,size):
    image_resized = Image.open(path)
    image_resized = image_resized.resize(size)
    return ImageTk.PhotoImage(image_resized)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      username TEXT UNIQUE NOT NULL PRIMARY KEY,
                      password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_data (
                      username TEXT UNIQUE NOT NULL PRIMARY KEY,
                      first_name TEXT NOT NULL,
                      last_name TEXT NOT NULL,
                      email TEXT NOT NULL,
                      phone TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def check_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def send_email(receiver_email, otp):
    SMTP_SERVER = "smtp.gmail.com"  
    SMTP_PORT = 465 
    sender_email = "kairospredict@gmail.com"  
    sender_password = "jxrs asoe pjfe abxm" 
    if type(otp) == type(1) :
        subject = "Your Password Reset OTP for Kairos Predict"
        body = f"""
        Dear User,

        Your One-Time Password (OTP) for secure access is: *{otp}*

        Please use this OTP within the next 10 minutes. Do not share it with anyone.

        If you didn't request this OTP, please ignore this email or contact support.

        Best regards,  
        Kairos Predict
        """
    else:
        subject = "New User Feedback Received"
        body = f"""
        Dear Team,

        You have received new feedback from a user:

        "{otp}"

        Please review and take necessary actions.

        Best regards,  
        Kairos Predict
        """
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")

def generate_otp():
    import random
    otp = random.randint(100000, 999999)
    return otp

def send_otp(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users_data WHERE username = ?", (username,))
    user_email = cursor.fetchone()
    conn.close()
    otp = generate_otp()    
    send_email(user_email, otp)
    return otp

def make_circle(image):
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)
        result = Image.new("RGBA", image.size)
        result.paste(image, (0, 0), mask)
        return result

def predict_stock():
    pass

def plot_stock_analysis():
    pass

def get_stock_analysis(s):
    print(s)

def change_password(root , change_password_window ,setup_ui, username , new_password , confirm_password ):
    value = is_valid_password(new_password)
    if not value[0]:
        messagebox.showwarning("Error" , value[1])
        return
    if new_password == "" or confirm_password == "":
        messagebox.showerror("Error", "All fields are required")
        return
    if new_password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return
    hashed_password = hash_password(new_password)
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Password changed successfully")
        change_password_window.destroy()
        b = get_is_stock_window_opened()
        if not b :
            root.deiconify()
            setup_ui()
    except sqlite3.Error:
        messagebox.showerror("Error", "An error occurred while changing the password")

def reset(chart_edit_window):
    global list_of_select_colors
    list_of_select_colors = [ 'green','red', 'lime','red','green',\
                         'red', 'green','blue',"white","black",'gray' , "Solid line"]
    save_colors("chart_configuration" , list_of_select_colors , None )
    chart_edit_window.destroy()

def chart_style1(selected_style):
    global list_of_select_colors
    list_of_select_colors[11] = selected_style 

def pick_color(color_button , no):
    global list_of_select_colors
    color_code = colorchooser.askcolor(title="Pick a Color")[1]
    if color_code:
        color_button.configure(fg_color=color_code) 
        list_of_select_colors[no] = color_code

def verify_otp(given_otp , otp , otp_window , open_change_password , root ,switch_event , switch_var , setup_ui):
    if otp == "":
        messagebox.showerror("Error", "OTP is required")
        return
    if otp == str(given_otp):
        open_change_password(root , cancel ,switch_event , switch_var , setup_ui)
        otp_window.destroy()
    else:
        messagebox.showerror("Error", "Invalid OTP")

def verfiy_button(username , open_otp_window , reset_password_window , root , setup_ui , switch_event , switch_var ):
    global current_user
    try :
        if username == "":
            messagebox.showerror("Error", "Username is required")
            return 
        user = check_user(username)
        if user:
            open_otp_window(root , cancel , setup_ui , switch_event , switch_var ,username)
            reset_password_window.destroy()
            current_user = username
        else:
            messagebox.showerror("Error", "Invalid username")
    except Exception as e:
        print(e)
    return current_user

def get_user():
    global current_user
    return current_user

def change_user(username ):
    global current_user 
    current_user = username

def login_user(user_entry , pass_entry , open_stock_ui):
    global is_stock_window_opened
    if user_entry == "" and pass_entry == "":
            messagebox.showwarning("Entry Warning !" , "Values required for Entry fields !")
            return
    username = user_entry
    change_user(username)
    update_profile_letter(username[0].lower())
    password = pass_entry
    hashed_password = hash_password(password)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    result = cursor.fetchone()
    conn.close()
    if result:
        conn1 = sqlite3.connect("users.db")
        cur = conn1.cursor()
        cur.execute("SELECT * FROM users_data WHERE username = ?", (username,))
        r = cur.fetchmany(1)
        username_detail  = r[0][0]
        first_name_detail = r[0][1]
        last_name_detail = r[0][2]
        email_detail = r[0][3]
        phone_detail = r[0][4]
        update_user_details(username_detail , first_name_detail , last_name_detail , email_detail , phone_detail)
        is_stock_window_opened = True
        open_stock_ui()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def get_is_stock_window_opened():
    global is_stock_window_opened
    return is_stock_window_opened

def set_stock_detail(value):
    global stock_detail
    stock_detail = value

def get_stock_detail():
    global stock_detail
    return stock_detail

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, "Password is valid."

def predict_stock(l, distance_metric, cluster_entry, visualize_on_off_var , sname , t_frame , clear): 
    if l == "" or distance_metric == "" or cluster_entry == "":
        messagebox.showerror("Error", "All fields are required")
        return
    try:
        cluster_entry = int(cluster_entry)
    except Exception as e :
        messagebox.showerror("Error", "Cluster entry should be an integer")
        return
    if len(l) <= 0 :
        messagebox.showerror("Error", "Select at least a Model")
        return
    if cluster_entry <= 0 and cluster_entry >= 20:
        messagebox.showerror("Error", "Cluster entry should be between 0 and 20")
    if distance_metric == "":
        return
    if cluster_entry == 0:
        messagebox.showerror("Error", "Cluster entry should be greater than 0")
        return
    if visualize_on_off_var == "off" :
        visualize_on_off_var = False
    else:
        visualize_on_off_var = True
    loading_window = Toplevel()
    loading_window.title("Loading")
    loading_window.geometry("350x120")  # Set window size

    Label(loading_window, text="Processing, please wait...").pack(pady=10, padx=20)

    progress_bar = Progressbar(loading_window, orient="horizontal", length=300, mode='determinate', maximum=100)
    progress_bar.pack(pady=10)
    
    def update_progress(progress):
        progress_bar['value'] = progress
        loading_window.update_idletasks()

    def process_task(progress=0):
        if progress != 100:
            update_progress(progress)
            loading_window.after(200, lambda: process_task(progress + 10))  # Recursive updates
        else:
            try:
                main(l, distance_metric, visualize_on_off_var, cluster_entry , sname , t_frame )
                update_progress(100)
                messagebox.showinfo("Success", "Plot Again to see the Prediction...")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                loading_window.destroy()

    process_task()

is_stock_window_opened = False
username = ""
first_name = ""
last_name = ""
email = ""
phone = ""
profile_letter = "a"
list_of_select_colors = load_colors("chart_configuration")
current_user = None
timeframe = " 1d "
chart_style = "candle"
stock_detail = "AAPL"
visualization = "off"
data_path = None
setup_db()