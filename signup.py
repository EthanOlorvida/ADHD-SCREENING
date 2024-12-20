import tkinter as tk
from captcha.image import ImageCaptcha
from tkinter import ttk
from tkinter import messagebox
from auth import sign_up
from PIL import Image, ImageTk
import random
import string

def create_signup_page(root, show_login_page, show_main_page):
    page4 = tk.Frame(root, bg="#526b5c")
    page4.pack_propagate(False)
    
    def generate_captcha_text():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        
    def generate_captcha_image(captcha_text, filename="captcha.png"):
        image = ImageCaptcha()
        image.write(captcha_text, filename)
    
    captcha_text = generate_captcha_text()
    generate_captcha_image(captcha_text)
    
    def generate_new_captcha():
        nonlocal captcha_text
        captcha_text = generate_captcha_text()
        generate_captcha_image(captcha_text)
        
        captcha_image = Image.open("captcha.png")
        captcha_photo = ImageTk.PhotoImage(captcha_image)
        captcha_image_label = tk.Label(page4, image=captcha_photo)
        captcha_image_label.place(relx=0.58, rely=0.67, anchor='e')
        captcha_image_label.image = captcha_photo
        
    def handle_sign_up():
        firstname = signup_firstname_entry.get()
        lastname = signup_lastname_entry.get()
        age = signup_age_entry.get()
        
        username = signup_username_entry.get()
        password = signup_password_entry.get()
        captcha = captcha_entry.get()
                
        confirmpassword = signup_confirmpassword_entry.get()
        
        if captcha != captcha_text:
            messagebox.showerror("Sign Up", "Incorrect CAPTCHA. Please try again.")
            return
            
        if len(password) < 7:
            messagebox.showerror("Sign Up", "Password must be at least 7 characters long.")
            return
        
        if password != confirmpassword:
            messagebox.showerror("Sign Up", "Passwords do not match. Please try again.")
            return

        if sign_up(username, password, firstname, lastname, age):
            show_login_page()
        else:
            messagebox.showerror("Sign Up", "Please fill in all the fields, and try again.")

    frame_page4 = tk.Label(page4, bg="white", width=2560, height=5, highlightthickness=4, highlightbackground="white")
    frame_page4.place(relx=0.5, rely=0.0, anchor='n')

    back_button_page1 = tk.Button(page4, text="←", bg="white", fg="black", font=("Helvetica", 24, "bold"), command=show_main_page, bd=0, highlightthickness=0, relief="flat")
    back_button_page1.place(relx=0.05, rely=0.020, anchor='nw')

    signup_title = tk.Label(page4, text="ADHD Cognitive Function Screening", bg="white", fg="black", font=("Helvetica", 18, "bold"))
    signup_title.place(relx=0.95, rely=0.035, anchor='ne')
    
    frame2_page3 = tk.Frame(page4, bg="white", bd=2, relief="solid")
    frame2_page3.place(relx=0.50, rely=0.53, width=510, height=480, anchor='center')

    signup_label = tk.Label(page4, text="Create New Account", bg="white", fg="black", font=("Helvetica", 36, "bold"))
    signup_label.place(relx=0.5, rely=0.25, anchor='center')

    signup_firstname_label = tk.Label(page4, text="First Name:", bg="white", fg="black")
    signup_firstname_label.place(relx=0.4, rely=0.35, anchor='e')

    signup_firstname_entry = tk.Entry(page4, width=36, bg="black", fg="white")
    signup_firstname_entry.place(relx=0.45, rely=0.35, anchor='w')

    signup_lastname_label = tk.Label(page4, text="Last Name:", bg="white", fg="black")
    signup_lastname_label.place(relx=0.4, rely=0.4, anchor='e')

    signup_lastname_entry = tk.Entry(page4, width=36, bg="black", fg="white")
    signup_lastname_entry.place(relx=0.45, rely=0.4, anchor='w')

    signup_age_label = tk.Label(page4, text="Age:", bg="white", fg="black")
    signup_age_label.place(relx=0.4, rely=0.45, anchor='e')

    signup_age_entry = tk.Entry(page4, width=36, bg="black", fg="white")
    signup_age_entry.place(relx=0.45, rely=0.45, anchor='w')

    signup_username_label = tk.Label(page4, text="Username:", bg="white", fg="black")
    signup_username_label.place(relx=0.4, rely=0.5, anchor='e')

    signup_username_entry = tk.Entry(page4, width=36, bg="black", fg="white")
    signup_username_entry.place(relx=0.45, rely=0.5, anchor='w')

    signup_password_label = tk.Label(page4, text="Password:", bg="white", fg="black")
    signup_password_label.place(relx=0.4, rely=0.55, anchor='e')

    signup_password_entry = tk.Entry(page4, show="*", width=36, bg="black", fg="white")
    signup_password_entry.place(relx=0.45, rely=0.55, anchor='w')

    signup_confirmpassword_label = tk.Label(page4, text="Confirm Password:", bg="white", fg="black")
    signup_confirmpassword_label.place(relx=0.4, rely=0.6, anchor='e')

    signup_confirmpassword_entry = tk.Entry(page4, show="*", width=36, bg="black", fg="white")
    signup_confirmpassword_entry.place(relx=0.45, rely=0.6, anchor='w')

    signup_captcha_label = tk.Label(page4, text="Enter CAPTCHA:", bg="white", fg="black")
    signup_captcha_label.place(relx=0.4, rely=0.65, anchor='e')

    signup_button = tk.Button(page4, text="Register", command=handle_sign_up, width=10, height=1, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    signup_button.place(relx=0.5, rely=0.80, anchor='center')

    captcha_image = Image.open("captcha.png")
    captcha_photo = ImageTk.PhotoImage(captcha_image)
    captcha_image_label = tk.Label(page4, image=captcha_photo)
    captcha_image_label.place(relx=0.58, rely=0.67, anchor='e')
    captcha_image_label.image = captcha_photo

    captcha_entry = tk.Entry(page4, width=36, bg="black", fg="white")
    captcha_entry.place(relx=0.62, rely=0.74, anchor='e')

    generate_new_captcha_button = tk.Button(page4, text="Another", command=generate_new_captcha, bg="#526b5c", fg="white")
    generate_new_captcha_button.place(relx=0.63, rely=0.65, anchor='e')

    return page4
