import customtkinter as ctk
from PIL import Image

logo = ctk.CTkImage(light_image=Image.open(r"static\images\logo.png"), 
                        dark_image=Image.open(r"static\images\logo-w.png"),
                        size=(200, 60))
logout_image = ctk.CTkImage(light_image=Image.open(r"static\images\logout-w.png"),
                                dark_image=Image.open(r"static\images\logout.png"),
                                size=(20,20))
settings_image = ctk.CTkImage(light_image=Image.open(r"static\images\settings.png"),
                                dark_image=Image.open(r"static\images\settings-w.png"),
                                size=(20,20))
chart_edit_image = ctk.CTkImage(light_image=Image.open(r"static\images\edit_chart.png"),
                                dark_image=Image.open(r"static\images\edit_chart-w.png"),
                                size=(18,18))
instagram = ctk.CTkImage(light_image=Image.open(r"static\images\instagram.png"), 
                        dark_image=Image.open(r"static\images\instagram-w.png"),
                        size=(30,30))
facebook = ctk.CTkImage(light_image=Image.open(r"static\images\facebook.png"),
                            dark_image=Image.open(r"static\images\facebook-w.png"),
                            size=(30,30))
github = ctk.CTkImage(light_image=Image.open(r"static\images\github.png"),
                          dark_image=Image.open(r"static\images\github-w.png"),
                          size=(30,30))
linkedin = ctk.CTkImage(light_image=Image.open(r"static\images\linkedin.png"),
                            dark_image=Image.open(r"static\images\linkedin-w.png"),
                            size=(30,30))

def get_image(image) :
    if image == "logo":
        return logo
    elif image == "chart_edit_image":
        return chart_edit_image
    elif image == "instagram":
        return instagram
    elif image== "logout_image":
        return logout_image
    elif image == "github":
        return github
    elif image == "facebook":
        return facebook
    elif image == "linkedin":
        return linkedin
    elif image == "settings_image":
        return settings_image
    else :
        return None