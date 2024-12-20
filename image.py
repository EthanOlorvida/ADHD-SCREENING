import json
import cv2
import tkinter as tk
from PIL import Image, ImageTk, ImageGrab

def store_eye_positions(eye_positions, filename='eye_positions.json'):
    serializable_positions = [(int(x), int(y), int(ewidth), int(eheight)) for (x, y, ewidth, eheight) in eye_positions]
    with open(filename, 'w') as file:
        json.dump(serializable_positions, file)

def load_eye_positions(filename='eye_positions.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def open_eye_position_window(canvas, back):
    
    def hideall(canvas):
        canvas.pack_forget()
    
    back_button_results = tk.Button(canvas, text="←", bg="white", fg="black", font=("Helvetica", 24, "bold"), command=lambda: [hideall(canvas), canvas.after(1000,back)], bd=0, highlightthickness=0, relief="flat")
    back_button_results.place(relx=0.05, rely=0.020, anchor='nw')
    
    eye_positions = load_eye_positions()

    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    scale_x = canvas_width / 200
    scale_y = canvas_height / 150

    for (x, y, ewidth, eheight) in eye_positions:

        scaled_x = int(x * scale_x)
        scaled_y = int(y * scale_y)

        reduced_ewidth = int((ewidth * scale_x) / 4)
        reduced_eheight = int((eheight * scale_y) / 4)

        canvas.create_oval(scaled_x, scaled_y, scaled_x + reduced_ewidth, scaled_y + reduced_eheight, outline="cyan", fill="cyan")
        
    canvas.update()
    
    def take_screenshot():
        screenshot = ImageGrab.grab()
        
        screenshot.save('eye_positions.png')

    canvas.after(2000, take_screenshot)