import pathlib
import cv2
import numpy as np
from gaze_tracking import GazeTracking
from fer import FER
from image import store_eye_positions
from image1 import store_eye_positions1
from image2 import store_eye_positions2
from image3 import store_eye_positions3
from image4 import store_eye_positions4
from PIL import Image, ImageTk
import tkinter as tk
import shared

images = []
eye_trail_history = []
image_clicked_state = [False, False, False, False]
active_image_index = None

def clear_adhd_log():
    with open("adhd_detection_log.json", "w") as log_file:
        log_file.truncate(0)

def log_adhd_event(event):
    with open("adhd_detection_log.json", "a") as log_file:
        log_file.write(f"{event}\n")

def detect_adhd(gaze_status, emotion, blink_count, gaze_directions):
    global adhd_status 
    attention_span_threshold = 15  
    fidgeting_blink_threshold = 12  
    
    adhd_status = ""
      
    gaze_changes = len(gaze_directions) - 1
    if gaze_changes > attention_span_threshold:
        adhd_status = "Short attention span"
        log_adhd_event("Short attention span") #Short attention span detected: Frequent gaze direction changes.
        gaze_directions.clear()

    if blink_count > fidgeting_blink_threshold:
        adhd_status = "Fidgeting"
        log_adhd_event("Fidgeting") #Fidgeting detected: High blink count.
        blink_count = 0

    gaze_variation = len(set(gaze_directions))  
    if gaze_variation > 3: 
        adhd_status = "Fidgeting"
        log_adhd_event("Fidgeting") #Fidgeting detected: Frequent shifts in gaze direction.
        gaze_directions.clear()

    if emotion in ["angry", "disgust"]:
        adhd_status = "Stress"
        log_adhd_event(f"Stress") #May indicate stress or restlessness linked to ADHD.
        
    return blink_count
    
def run_adhd_detection1(canvas, root):
    from main import load_resized_image
    
    clear_adhd_log()
    
    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
    eye_cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_eye.xml"
    clf = cv2.CascadeClassifier(str(cascade_path))
    eye_cascade = cv2.CascadeClassifier(str(eye_cascade_path))

    gaze = GazeTracking()
    detector = FER()
    shared.camera = cv2.VideoCapture(0)

    eye_positions = []
    gaze_directions = []
    blink_count = 0

    root.update_idletasks()  
    canvas_width = max(1, canvas.winfo_width())
    canvas_height = max(1, canvas.winfo_height())
    
    status_label = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 18, "bold"))
    status_label.place(x=canvas_width // 2, y=canvas_height - 50)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    video_writer = cv2.VideoWriter('image_output.avi', fourcc, 1.0, (canvas_width, canvas_height)) 

    total_images = 4
    double_gap = 20  
    image_space = canvas_width - (total_images + 1) * double_gap
    square_size = image_space // total_images

    background_image = Image.open("image1.png").resize((square_size, square_size))
    background_image2 = Image.open("image2.png").resize((square_size, square_size))
    background_image3 = Image.open("image3.png").resize((square_size, square_size))
    background_image4 = Image.open("image4.png").resize((square_size, square_size))
    full_background = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))

    x_position_1 = double_gap
    label_1 = tk.Label(root)
    label_1.bind("<Button-1>", lambda event: toggle_image(0))
    images.append(label_1)
    background_image_resized_1 = background_image.resize((square_size, square_size))
    img_1 = ImageTk.PhotoImage(background_image_resized_1)
    label_1.config(image=img_1)
    label_1.image = img_1
    
    x_position_2 = double_gap + (square_size + double_gap)
    label_2 = tk.Label(root)
    label_2.bind("<Button-1>", lambda event: toggle_image(1))
    images.append(label_2)
    background_image_resized_2 = background_image2.resize((square_size, square_size))
    img_2 = ImageTk.PhotoImage(background_image_resized_2)
    label_2.config(image=img_2)
    label_2.image = img_2

    x_position_3 = double_gap + 2 * (square_size + double_gap)
    label_3 = tk.Label(root)
    label_3.bind("<Button-1>", lambda event: toggle_image(2))
    images.append(label_3)
    background_image_resized_3 = background_image3.resize((square_size, square_size))
    img_3 = ImageTk.PhotoImage(background_image_resized_3)
    label_3.config(image=img_3)
    label_3.image = img_3

    x_position_4 = double_gap + 3 * (square_size + double_gap)
    label_4 = tk.Label(root)
    label_4.bind("<Button-1>", lambda event: toggle_image(3))
    images.append(label_4)
    background_image_resized_4 = background_image4.resize((square_size, square_size))
    img_4 = ImageTk.PhotoImage(background_image_resized_4)
    label_4.config(image=img_4)
    label_4.image = img_4

    background_frame = np.array(full_background)
    
    label_1.place(x=x_position_1, y=(canvas_height - square_size) // 2)
    label_2.place(x=x_position_2, y=(canvas_height - square_size) // 2)
    label_3.place(x=x_position_3, y=(canvas_height - square_size) // 2)
    label_4.place(x=x_position_4, y=(canvas_height - square_size) // 2)
    
    bgframe_rgb = cv2.cvtColor(background_frame, cv2.COLOR_BGR2RGB)
    bgframe_pil = Image.fromarray(bgframe_rgb)
    bgframe_tk = ImageTk.PhotoImage(bgframe_pil)
    canvas.create_image(0, 0, anchor=tk.NW, image=bgframe_tk)
    canvas.image = bgframe_tk

    while True: 

        if shared.next_button_pressedpv:
            break
        
        _, frame = shared.camera.read() 
        frame_resized = cv2.resize(frame, (canvas_width, canvas_height))
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        display_frame = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
        display_frame_np = np.array(display_frame)
        faces = clf.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
        )

        mini_feed_overlay = np.zeros((150, 200, 3), dtype=np.uint8) 

        def toggle_image(index):
            global active_image_index
            active_image_index = index           
            image_clicked_state[index] = True
            
            for label in images:
                label.place_forget()

            #new_frame_image = Image.open("image.png").resize((canvas_width, canvas_height))
            new_frame_image = [Image.open(f"image{i}.png").resize((canvas_width, canvas_height))
            for i in range(1, 5)
            ]
            
            new_frame_rgbs = [cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) for img in new_frame_image]
            new_frame_pils = [Image.fromarray(rgb) for rgb in new_frame_rgbs]
            new_frame_tks = [ImageTk.PhotoImage(pil) for pil in new_frame_pils]
            
            #new_frame_rgb = cv2.cvtColor(np.array(new_frame_image), cv2.COLOR_RGB2BGR)
            #new_frame_pil = Image.fromarray(new_frame_rgb)
            #new_frame_tk = ImageTk.PhotoImage(new_frame_pil)
    
            canvas.create_image(0, 0, anchor=tk.NW, image=new_frame_tks[active_image_index], tags="new_frame")
            canvas.image = new_frame_tks[active_image_index]
            canvas.tag_lower(new_frame)
        
            root.update_idletasks()
            root.update()
        
        def on_image_click(event):
            colored_image = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))
            colored_image_tk = ImageTk.PhotoImage(colored_image)
        
            canvas.create_image(0, 0, anchor=tk.NW, image=colored_image_tk)
            canvas.image = colored_image_tk 
                
            for i, label in enumerate(images):
                if not image_clicked_state[i]: 
                    x_position = double_gap + i * (square_size + double_gap)
                    label.place(x=x_position, y=(canvas_height - square_size) // 2)        
                  

        if len(faces) > 0:
            faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
            (x, y, width, height) = faces[0]

            face_frame = frame_resized[y:y + height, x:x + width]
            gaze.refresh(face_frame)
            horizontal_ratio = gaze.horizontal_ratio()

            gaze_status = ""
            if horizontal_ratio is not None:
                if gaze.is_blinking():
                    gaze_status = "Blinking"
                    blink_count += 1
                elif horizontal_ratio > 0.80:
                    gaze_status = "Looking Left"
                    gaze_directions.append("Looking Left")
                elif horizontal_ratio < 0.60:
                    gaze_status = "Looking Right"
                    gaze_directions.append("Looking Right")
                else:
                    gaze_status = "Looking Center"
                    gaze_directions.append("Looking Center")
            else:
                gaze_directions.append("Looking Away")

            emotions = detector.detect_emotions(face_frame)
            top_emotion, _ = detector.top_emotion(face_frame)
            
            blink_count = detect_adhd(gaze_status, top_emotion, blink_count, gaze_directions)

            mini_feed_overlay = cv2.resize(frame.copy(), (200, 150))
            mini_face_x, mini_face_y = int(x * 200 / canvas_width), int(y * 150 / canvas_height)
            mini_face_w, mini_face_h = int(width * 200 / canvas_width), int(height * 150 / canvas_height)

            cv2.rectangle(mini_feed_overlay, (mini_face_x, mini_face_y),
                          (mini_face_x + mini_face_w, mini_face_y + mini_face_h), (255, 255, 0), 2)

            eyes = eye_cascade.detectMultiScale(gray[y:y + height, x:x + width])
            for (ex, ey, ewidth, eheight) in eyes[:2]:
                eye_center_x = mini_face_x + int((ex + ewidth / 2) * 200 / canvas_width)
                eye_center_y = mini_face_y + int((ey + eheight / 2) * 150 / canvas_height)
                eye_radius = int((ewidth / 2) * 200 / canvas_width / 4)
                cv2.circle(mini_feed_overlay, (eye_center_x, eye_center_y), eye_radius, (255, 255, 0), -1)
                
                full_eye_center_x = x + ex + ewidth // 2
                full_eye_center_y = y + ey + eheight // 2
                full_eye_radius = int(ewidth / 5)
                    
                eye_trail_history.append((full_eye_center_x, full_eye_center_y, full_eye_radius))
    
                if len(eye_trail_history) > 5:
                    eye_trail_history.pop(0)
    
                for i, (trail_x, trail_y, trail_radius) in enumerate(eye_trail_history):
                    trail_color = (0, 255, 255, 32)
                    cv2.circle(display_frame_np, (trail_x, trail_y), trail_radius, trail_color, -1)
        
                cv2.circle(display_frame_np, (full_eye_center_x, full_eye_center_y), full_eye_radius, (0, 255, 255, 32), -1)
                
                eye_positions.append((eye_center_x, eye_center_y, ewidth, eheight))
                            
            if active_image_index == 0:
                store_eye_positions1(eye_positions, filename="eye_positions1.json")
                eye_positions.clear()
            elif active_image_index == 1:
                store_eye_positions2(eye_positions, filename="eye_positions2.json")
                eye_positions.clear()
            elif active_image_index == 2:
                store_eye_positions3(eye_positions, filename="eye_positions3.json")
                eye_positions.clear()
            elif active_image_index == 3:
                store_eye_positions4(eye_positions, filename="eye_positions4.json")
                eye_positions.clear()
            else:
                store_eye_positions(eye_positions, filename='eye_positions.json')
                
            status_label.config(text=f'{adhd_status}')

        mini_feed_rgb = cv2.cvtColor(mini_feed_overlay, cv2.COLOR_BGR2RGB)
        mini_feed_pil = Image.fromarray(mini_feed_rgb)
        mini_feed_tk = ImageTk.PhotoImage(mini_feed_pil)

        frame_pil = Image.fromarray(display_frame_np)
        frame_tk = ImageTk.PhotoImage(frame_pil)
        canvas.create_image(0, 0, anchor=tk.NW, image=frame_tk)
        canvas.image = frame_tk

        canvas.tag_bind(canvas.create_image(0, 0, anchor=tk.NW, image=frame_tk), '<Button-1>', on_image_click)
        canvas.create_image(canvas_width - 210, canvas_height - 160, anchor=tk.NW, image=mini_feed_tk)
        canvas.mini_image = mini_feed_tk
                      
        video_writer.write(frame_resized) 

        root.update_idletasks()
        root.update()
    return video_writer.release(), shared.camera.release()
