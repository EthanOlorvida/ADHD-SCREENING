import pathlib
import cv2
import numpy as np
from gaze_tracking import GazeTracking
from fer import FER
from imagev import store_eye_positionsv
from PIL import Image, ImageTk
import tkinter as tk
import shared
import pygame

overlay_eye_trail_history = []

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

def run_adhd_detection2(canvas, root):
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

    pygame.mixer.init()
    video_1 = cv2.VideoCapture("disney_pixar_piper.mp4")
    video_2 = cv2.VideoCapture("the_cat_came_back.mp4")    
            
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    status_label = tk.Label(root, text="", bg="white", fg="black", font=("Helvetica", 18, "bold"))
    status_label.place(x=canvas_width // 2, y=canvas_height - 50)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    video_writer = cv2.VideoWriter('video_output.avi', fourcc, 1.0, (canvas_width, canvas_height)) 
    
    double_gap = 20
    video_width = (canvas_width - (3 * double_gap)) // 2
    video_height = int(1.25 * 300)

    mini_feed_overlay = np.zeros((150, 200, 3), dtype=np.uint8)

    video_1_maximized = False
    original_video_1_size = (video_width, video_height)
    video_2_visible = True  
    
    video_1_x_position = double_gap
    video_1_y_position = (canvas_height - video_height) // 2
    video_1_area = (video_1_x_position, video_1_y_position, video_1_x_position + video_width, video_1_y_position + video_height)

    def toggle_video_size(event):
            nonlocal video_1_maximized, video_width, video_height, video_2_visible
            if (video_1_area[0] <= event.x <= video_1_area[2] and
                video_1_area[1] <= event.y <= video_1_area[3]):

                if video_1_maximized:  
                    video_width, video_height = original_video_1_size
                    video_2_visible = True
                    pygame.mixer.music.stop()
                else:
                    video_width = canvas_width
                    video_height = canvas_height
                    video_1.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    pygame.mixer.music.load("disney_pixar_piper_audio.mp3")
                    pygame.mixer.music.play(-1, 0.0)
                    
                    video_2_visible = False

                video_1_maximized = not video_1_maximized

    canvas.bind("<Button-1>", lambda e: toggle_video_size(e))
    
    video_2_x_position = canvas_width - double_gap - video_width
    video_2_y_position = (canvas_height - video_height) // 2
    video_2_area = (video_2_x_position, video_2_y_position, video_2_x_position + video_width, video_2_y_position + video_height)

    video_2_maximized = False
    original_video_2_size = (video_width, video_height)
    video_1_visible = True 

    def toggle_video_2_size(event):
        nonlocal video_2_maximized, video_width, video_height, video_1_visible
        if (video_2_area[0] <= event.x <= video_2_area[2] and
            video_2_area[1] <= event.y <= video_2_area[3]):
                
            if video_2_maximized:
                video_width, video_height = original_video_2_size
                video_1_visible = True
                pygame.mixer.music.stop()                
            else:
                video_width = canvas_width
                video_height = canvas_height
                video_2.set(cv2.CAP_PROP_POS_FRAMES, 0)
                pygame.mixer.music.load("the_cat_came_back_audio.mp3")
                pygame.mixer.music.play(-1, 0.0)
                
                video_1_visible = False

            video_2_maximized = not video_2_maximized

    canvas.bind("<Button-1>", lambda e: toggle_video_2_size(e), add=True)

    while True:
        
        if shared.next_button_pressedv:
            break
        
        ret1, frame_1 = video_1.read()
        ret2, frame_2 = video_2.read()

        ret, camera_frame = shared.camera.read()
        frame_resized = cv2.resize(camera_frame, (canvas_width, canvas_height))
        frame_1_resized = cv2.resize(frame_1, (video_width, video_height))
        frame_2_resized = cv2.resize(frame_2, (video_width, video_height))
        top_emotion, _ = detector.top_emotion(camera_frame)

        full_background = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 255))
        x_position_1 = double_gap
        x_position_2 = canvas_width - double_gap - video_width
        
        if video_1_visible:
            full_background.paste(
                Image.fromarray(cv2.cvtColor(frame_1_resized, cv2.COLOR_BGR2RGB)),
            (x_position_1, (canvas_height - video_height) // 2)
            )

        if video_2_visible:
            full_background.paste(
                Image.fromarray(cv2.cvtColor(frame_2_resized, cv2.COLOR_BGR2RGB)),
                (x_position_2, (canvas_height - video_height) // 2)
            )
            
        background_frame = np.array(full_background)

        mini_feed_rgb = cv2.cvtColor(camera_frame, cv2.COLOR_BGR2RGB)
        original_height, original_width, _ = camera_frame.shape
        mini_feed_width = 200
        mini_feed_height = 150
        aspect_ratio = original_width / original_height
        if aspect_ratio > 1:
            new_width = mini_feed_width
            new_height = int(mini_feed_width / aspect_ratio)
        else:
            new_height = mini_feed_height
            new_width = int(mini_feed_height * aspect_ratio)

        resized_camera_frame = cv2.resize(mini_feed_rgb, (new_width, new_height))
        padded_frame = np.zeros((mini_feed_height, mini_feed_width, 3), dtype=np.uint8)
        x_offset = (mini_feed_width - new_width) // 2
        y_offset = (mini_feed_height - new_height) // 2
        padded_frame[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_camera_frame

        gray = cv2.cvtColor(camera_frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

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
            
            blink_count = detect_adhd(gaze_status, top_emotion, blink_count, gaze_directions)

            face_x = int(x * mini_feed_width / original_width)
            face_y = int(y * mini_feed_height / original_height)
            face_w = int(width * mini_feed_width / original_width)
            face_h = int(height * mini_feed_height / original_height)

            cv2.rectangle(padded_frame, (face_x, face_y), (face_x + face_w, face_y + face_h), (0, 255, 255), 2)

        eyes = eye_cascade.detectMultiScale(gray[y:y + height, x:x + width])

        for (ex, ey, ewidth, eheight) in eyes[:2]:
            ex += x
            ey += y

            mini_eye_center_x = int((ex + ewidth // 2) * mini_feed_width / original_width)
            mini_eye_center_y = int((ey + eheight // 2) * mini_feed_height / original_height)

            mini_eye_radius = int(min(ewidth, eheight) * mini_feed_width / original_width / 12)
            cv2.circle(padded_frame, (mini_eye_center_x, mini_eye_center_y), mini_eye_radius, (0, 255, 255), -1)

            full_eye_center_x = int((ex + ewidth // 2) * canvas_width / original_width)
            full_eye_center_y = int((ey + eheight // 2) * canvas_height / original_height)
            overlay = background_frame.copy()
            full_eye_radius = int(ewidth / 3)
            overlay_eye_trail_history.append((full_eye_center_x, full_eye_center_y, full_eye_radius))

            if len(overlay_eye_trail_history) > 5:
                overlay_eye_trail_history.pop(0)

            for i, (trail_x, trail_y, trail_radius) in enumerate(overlay_eye_trail_history):
                trail_color = (255, 255, 0, 32) 
                cv2.circle(overlay, (trail_x, trail_y), trail_radius, trail_color, -1)

            cv2.circle(overlay, (full_eye_center_x, full_eye_center_y), full_eye_radius, (255, 255, 0, 32), -1)

            cv2.addWeighted(overlay, 32 / 255.0, background_frame, 1 - 32 / 255.0, 0, background_frame)

            eye_positions.append((mini_eye_center_x, mini_eye_center_y, ewidth, eheight))

        store_eye_positionsv(eye_positions, filename='eye_positionsv.json')
        status_label.config(text=f'{adhd_status}')
        
        mini_feed_pil = Image.fromarray(padded_frame)
        mini_feed_tk = ImageTk.PhotoImage(mini_feed_pil)

        canvas.delete("all")
        display_frame_pil = Image.fromarray(cv2.cvtColor(background_frame, cv2.COLOR_BGR2RGBA))
        frame_tk = ImageTk.PhotoImage(display_frame_pil)
        canvas.create_image(0, 0, image=frame_tk, anchor='nw')
        
        canvas.create_image(canvas_width - 210, canvas_height - 160, anchor=tk.NW, image=mini_feed_tk)
                
        video_writer.write(frame_resized) 

        root.update_idletasks()
        root.update()
    return video_1.release(), video_2.release(), video_writer.release(), shared.camera.release()