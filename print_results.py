import tkinter as tk
import sqlite3
import shared
import tempfile
import webbrowser
from reportlab.pdfgen import canvas

logged_in_username = None

def connect_db():
    return sqlite3.connect('users.db')

def get_user_details(logged_in_username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT firstname, lastname, age FROM users WHERE username = ?", (logged_in_username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result
    return None

def open_print_dialog(content):
    root = tk.Tk()
    root.withdraw()
    
    message = shared.message 
    message2 = shared.message2
    message3 = shared.message3
    summary_text = shared.summary_text
    
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf_path = temp_pdf.name
    temp_pdf.close()

    pdf_canvas = canvas.Canvas(pdf_path)

    page_height = 800
    margin = 100
    y_position = page_height - margin

    def add_wrapped_text(canvas, text, x, y, max_width):
        paragraphs = text.split('\n')
        for para in paragraphs:
            lines = []
            words = para.split()
            line = ""
            for word in words:
                if canvas.stringWidth(line + word, "Helvetica", 12) < max_width:
                    line += (word + " ")
                else:
                    lines.append(line)
                    line = word + " "
            lines.append(line)  
            for i, line in enumerate(lines):
                canvas.drawString(x, y - i * 14, line)  
            y -= (len(lines) * 14 + 10)  
        return y  

    def check_page_space(y_position, content_height):
        if y_position - content_height < margin:
            pdf_canvas.showPage() 
            return page_height - margin  
        return y_position

    firstname, lastname, age = get_user_details(shared.logged_in_username)
    if firstname and lastname and age:
        y_position = add_wrapped_text(pdf_canvas, f"Name: {firstname} {lastname}", 100, y_position, 400)
        y_position = add_wrapped_text(pdf_canvas, f"Age: {age}", 100, y_position, 400)

    y_position = add_wrapped_text(pdf_canvas, message, 100, y_position, 400)
    y_position = add_wrapped_text(pdf_canvas, message2, 100, y_position, 400)

    images = [
        'eye_positions.png',
        'eye_positions1.png',
        'eye_positions2.png',
        'eye_positions3.png',
        'eye_positions4.png',
        'eye_positionsv.png'
    ]
    
    for image in images:
        y_position = check_page_space(y_position, 310)  # Check if there is space for the next image
        y_position -= 300
        pdf_canvas.drawImage(image, 100, y_position, width=400, height=300)  # Adjust size and position

    y_position = add_wrapped_text(pdf_canvas, summary_text, 100, y_position - 50, 400)
    y_position = add_wrapped_text(pdf_canvas, message3, 100, y_position, 400)

    pdf_canvas.save()

    webbrowser.open(pdf_path)
