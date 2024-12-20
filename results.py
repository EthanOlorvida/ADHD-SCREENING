import tkinter as tk
from image import open_eye_position_window
from image1 import open_eye_position_window1
from image2 import open_eye_position_window2
from image3 import open_eye_position_window3
from image4 import open_eye_position_window4
from imagev import open_eye_position_windowv
from print_results import open_print_dialog
import cv2
from PIL import Image, ImageTk
import shared 

def show_canvas(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_window(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))

def show_canvas1(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_window1(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))
  
def show_canvas2(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_window2(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))
  
def show_canvas3(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_window3(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))
  
def show_canvas4(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_window4(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))
  
def show_canvasv(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame):
    results_frame.pack_forget()

    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(fill="both", expand=True)
    
    root.after(1000, open_eye_position_windowv(canvas, lambda: display_results(canvas, root, show_page2, page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button)))
    
def again(show_page2, results_frame, frame_results, img_results, label_results, main_label, dropdown_menu, facial_results_button):      
    results_frame.pack_forget()
    frame_results.place_forget()
    img_results.place_forget()
    label_results.place_forget()
    main_label.place_forget()
    dropdown_menu.place_forget()
    facial_results_button.place_forget()
    
    show_page2()

def display_results(canvas, root, show_page2, page2,frame_page2,img_label4,page2_title,main_label,selectanoption_label, selectanoptiontitle_label,logout_button,left_frame,middle_frame,right_frame,img_label5,img_label6,img_label7,image_detection_button,video_detection_button,quizzes_button,submit_samples_button):
    page2.pack_forget()
    frame_page2.place_forget()
    img_label4.place_forget()
    page2_title.place_forget()
    main_label.place_forget()
    selectanoption_label.place_forget()
    selectanoptiontitle_label.place_forget()
    logout_button.place_forget()
    left_frame.place_forget()
    middle_frame.place_forget()
    right_frame.place_forget()
    img_label5.place_forget()
    img_label6.place_forget()
    img_label7.place_forget()
    image_detection_button.place_forget()
    video_detection_button.place_forget()
    quizzes_button.place_forget()
    submit_samples_button.place_forget()
 
    results_frame = tk.Canvas(root, bg="#526b5c")
    results_frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(results_frame, orient="vertical", command=results_frame.yview)
    scrollbar.pack(side="right", fill="y")

    results_frame.configure(yscrollcommand=scrollbar.set)

    def on_frame_configure(event):
        results_frame.configure(scrollregion=results_frame.bbox("all"))
        
    results_frame.bind("<Configure>", on_frame_configure)
    
    #for i in range(50):
    #    results_frame.create_text(10, (i + 1) * 30, text=f"Item {i+1}", anchor="nw")
    
    from main import load_resized_image

    frame_results = tk.Label(results_frame, bg="#526b5c", width=2560, height=5)
    frame_results.place(relx=0.5, rely=0.0, anchor='n')
    
    img4 = load_resized_image("5.png", (50, 50))
    img_results = tk.Label(results_frame, image=img4, bg="white")
    img_results.place(relx=0.05, rely=0.028, anchor='nw')
    
    label_results = tk.Label(results_frame, text="ADHD Cognitive Function Screening", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
    label_results.place(relx=0.1, rely=0.035, anchor='nw')
    
    main_label = tk.Button(results_frame, text="Main", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"), command=lambda: [again(show_page2, results_frame, frame_results, img_results, label_results, main_label, dropdown_menu, facial_results_button)], bd=0, highlightthickness=0, relief="flat")
    main_label.place(relx=0.95, rely=0.034, anchor='ne')
    
    img_results.image = img4
    
    facial_results_button = tk.Button(results_frame, text="VIEW VIDEO EYE RESULTS", command=lambda: [show_canvasv(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)], width=28, height=2, bg="white", fg="black", font=("Arial", 16, "bold"), relief="flat")
    results_frame.create_window(320 + 315, 480 + 900, window=facial_results_button, anchor='s')
    
    print_results_button = tk.Button(results_frame, text="PRINT RESULTS", command=lambda: [open_print_dialog("Test")], width=28, height=2, bg="white", fg="black", font=("Arial", 16, "bold"), relief="flat")
    results_frame.create_window(630 + 600, 480 + 900, window=print_results_button, anchor='se')
    
    def on_select(option):
        if option == "ALL":
            show_canvas(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)
        if option == "1ST IMAGE":
            show_canvas1(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)
        if option == "2ND IMAGE":
            show_canvas2(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)
        if option == "3RD IMAGE":
            show_canvas3(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)
        if option == "4TH IMAGE":
            show_canvas4(canvas, root, page2, show_page2, frame_page2, img_label4, page2_title, main_label, selectanoption_label, selectanoptiontitle_label, logout_button, left_frame, middle_frame, right_frame, img_label5, img_label6, img_label7, image_detection_button, video_detection_button, quizzes_button, submit_samples_button, results_frame)        
                
    selected_option = tk.StringVar()
    selected_option.set("VIEW EYE RESULTS")

    dropdown_menu = tk.OptionMenu(results_frame, selected_option, "ALL", "1ST IMAGE", "2ND IMAGE", "3RD IMAGE", "4TH IMAGE")
    dropdown_menu.config(width=28, height=2, font=("Arial", 16, "bold"), bg="white", fg="black")
    results_frame.create_window(35, 480 + 900, window=dropdown_menu, anchor='sw')

    selected_option.trace("w", lambda *args: on_select(selected_option.get()))
    
    try:
        message = shared.message 
        message2 = shared.message2
        message3 = shared.message3

        if message:
            label = tk.Label(results_frame, text=message, bg="#526b5c", fg="white", font=("Helvetica", 14), wraplength=900, justify="left")
            results_frame.create_window(10 + 100*2, 510, window=label, anchor='nw')
            label2 = tk.Label(results_frame, text=message2, bg="#526b5c", fg="white", font=("Helvetica", 14), wraplength=900, justify="left")
            results_frame.create_window(10 + 100*2, 570, window=label2, anchor='nw')
            label3 = tk.Label(results_frame, text=message3, bg="#526b5c", fg="white", font=("Helvetica", 14), wraplength=900, justify="left")
            results_frame.create_window(10 + 100*2, 630, window=label3, anchor='nw')

        try:
            with open('adhd_detection_log.json', 'r') as f:
                detections = f.read().splitlines() 

            if detections:
                detection_counts = {}
                for detection in detections:
                    detection_counts[detection] = detection_counts.get(detection, 0) + 1

                summary_text = "The screening process detected "
                detection_list = []

                for detection, count in detection_counts.items():
                    detection_list.append(f"{count} {detection.lower()}")

                summary_text += ", ".join(detection_list) + "."

                padding = tk.Label(results_frame, text="", bg="#526b5c", font=("Helvetica", 14), wraplength=600, justify="left")
                results_frame.create_window(10 + 100*2, 220 + 100*2, window=padding, anchor='nw')
                summary_label = tk.Label(results_frame, text=summary_text, bg="#526b5c", fg="white", font=("Helvetica", 14), wraplength=600, justify="left")
                results_frame.create_window(10 + 100*2, 730 + 100*2, window=summary_label, anchor='nw')
                
                shared.summary_text = summary_text

            else:
                no_detections_label = tk.Label(results_frame, text="No ADHD detection results available.", bg="#526b5c", fg="white", font=("Helvetica", 14), wraplength=600, justify="left")
                results_frame.create_window(10 + 100*2, 260 + 100*2, window=no_detections_label, anchor='nw')

        except FileNotFoundError:
            error_label = tk.Label(results_frame, text="Error: ADHD detection log not found.", bg="#526b5c", fg="red", font=("Helvetica", 14), wraplength=600, justify="left")
            results_frame.create_window(10 + 100*2, 300 + 100*2, window=error_label, anchor='nw')

    except Exception as e:
        error_label = tk.Label(results_frame, text=f"Error: {str(e)}", bg="#526b5c", fg="red", font=("Helvetica", 14), wraplength=600, justify="left")
        results_frame.create_window(10 + 100*2, 300 + 100*2, window=error_label, anchor='nw')
        


    class VideoPlayer:
        def __init__(self, parent_frame, video_source, x, y, width, height):
            self.parent_frame = parent_frame
            self.video_source = video_source
            self.x = x
            self.y = y
            self.width = width  
            self.height = height  
            self.vid = cv2.VideoCapture(self.video_source)

            self.canvas = tk.Canvas(parent_frame, width=self.width, height=self.height)
            results_frame.create_window(self.x + 100*2, self.y + 815, window=self.canvas)

        def update(self):
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)

                self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
                self.canvas.img = imgtk 

            else:
                self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)

        def __del__(self):
            if self.vid.isOpened():
                self.vid.release()
    
    def play_videos(results_frame, video1_path, video2_path):
        
        video_width = 400
        video_height = 300
        
        video_player1 = VideoPlayer(results_frame, video1_path, x=230, y=320, width=video_width, height=video_height)
        video_player2 = VideoPlayer(results_frame, video2_path, x=650, y=320, width=video_width, height=video_height)

        while True:
            video_player1.update()
            video_player2.update()
            results_frame.update_idletasks()
            results_frame.update()

    video1_path = "image_output.avi"  
    video2_path = "video_output.avi"

    play_videos(results_frame, video1_path, video2_path)

    root.mainloop()
        
    return results_frame
