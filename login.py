import tkinter as tk
from tkinter import messagebox
from auth import login
import shared

def create_login_page(root, show_page2, show_main_page):
    page3 = tk.Frame(root, bg="#526b5c")
    page3.pack_propagate(False)

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        if login(username, password):
            shared.logged_in_username = username
            show_page2()
        else:
            messagebox.showerror("Login", "Invalid username or password. Please try again.")

    frame_page3 = tk.Label(page3, bg="white", width=2560, height=5, highlightthickness=4, highlightbackground="white")
    frame_page3.place(relx=0.5, rely=0.0, anchor='n')
    
    back_button_page1 = tk.Button(page3, text="←", bg="white", fg="black", font=("Helvetica", 24, "bold"), command=show_main_page, bd=0, highlightthickness=0, relief="flat")
    back_button_page1.place(relx=0.05, rely=0.020, anchor='nw')

    login_title = tk.Label(page3, text="ADHD Cognitive Function Screening", bg="white", fg="black", font=("Helvetica", 18, "bold"))
    login_title.place(relx=0.95, rely=0.035, anchor='ne')
    
    frame2_page3 = tk.Frame(page3, bg="white", bd=2, relief="solid")
    frame2_page3.place(relx=0.49, rely=0.53, width=400, height=260, anchor='center')

    login_label = tk.Label(page3, text="Sign In", bg="white", fg="black", font=("Helvetica", 36, "bold"))
    login_label.place(relx=0.5, rely=0.4, anchor='center')

    username_label = tk.Label(page3, text="Username:", bg="white", fg="black")
    username_label.place(relx=0.4, rely=0.5, anchor='e')

    username_entry = tk.Entry(page3, width=36, bg="black", fg="white")
    username_entry.place(relx=0.45, rely=0.5, anchor='w')

    password_label = tk.Label(page3, text="Password:", bg="white", fg="black")
    password_label.place(relx=0.4, rely=0.55, anchor='e')

    password_entry = tk.Entry(page3, show="*", width=36, bg="black", fg="white")
    password_entry.place(relx=0.45, rely=0.55, anchor='w')

    signin_button = tk.Button(page3, text="Log In", command=handle_login, width=10, height=1, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    signin_button.place(relx=0.5, rely=0.65, anchor='center')


    return page3
