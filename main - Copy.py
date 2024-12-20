import tkinter as tk
from tkinter import messagebox
from login import create_login_page
from signup import create_signup_page
from prevideo import run_adhd_detection1
from video import run_adhd_detection2
from PIL import Image, ImageTk
from quiz import create_quiz_page
from results import display_results 
from auth import login, sign_up, save_quiz, create_table
import shared

create_table()

current_user = None

def load_resized_image(path, size):
    image = Image.open(path)
    resized_image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

def create_main_page(root):
    def show_page2():        
        page3.pack_forget()
        canvas.pack_forget()
        quiz_frame.pack_forget()
        next_button.place_forget()
        quiz_button.place_forget()
        page2.pack(fill="both", expand=True)
        image_detection_button.place(relx=0.18, rely=0.75, anchor='n')
        video_detection_button.place(relx=0.5, rely=0.75, anchor='n')
        quizzes_button.place(relx=0.82, rely=0.75, anchor='n')
        submit_samples_button.place(relx=0.5, rely=0.88, anchor='n')     

        frame_page2.place(relx=0.5, rely=0.0, anchor='n')
        img_label4.place(relx=0.05, rely=0.028, anchor='nw')
        page2_title.place(relx=0.1, rely=0.035, anchor='nw')
        main_label.place(relx=0.95, rely=0.034, anchor='ne')
        selectanoption_label.place(relx=0.5, rely=0.24, anchor='center')
        selectanoptiontitle_label.place(relx=0.5, rely=0.31, anchor='center')
        logout_button.place(relx=0.95, rely=0.175, anchor='ne')
        left_frame.place(relx=0.18, rely=0.55, anchor='center')
        middle_frame.place(relx=0.5, rely=0.55, anchor='center')
        right_frame.place(relx=0.82, rely=0.55, anchor='center')
        img_label5.place(relx=0.5, rely=0.5, anchor='center')
        img_label6.place(relx=0.5, rely=0.5, anchor='center')
        img_label7.place(relx=0.5, rely=0.5, anchor='center')

    def go_back_to_page1():   
        page2.pack_forget()
        page3.pack_forget()
        page4.pack_forget()
        page1.pack(fill="both", expand=True)

    def show_login_page():
        page4.pack_forget()
        page3.pack(fill="both", expand=True)

    def show_quiz_page():         
        for var_name in ['frame_prevideo', 'label_prevideo', 'main_labelpv', 'frame_video', 'label_video', 'main_labelv', 'img_prevideo', 'img_video']:
            if var_name in globals() and globals()[var_name] is not None:
                try:
                    globals()[var_name].place_forget()
                except AttributeError:
                    pass  
        
        shared.next_button_pressedv = True    
        frame_quiz = tk.Label(quiz_frame, bg="#526b5c", width=2560, height=5, highlightthickness=4, highlightbackground="white")
        frame_quiz.place(relx=0.5, rely=0.0, anchor='n')

        img4 = load_resized_image("5.png", (50, 50))
        img_quiz = tk.Label(quiz_frame, image=img4, bg="white")
        img_quiz.place(relx=0.05, rely=0.028, anchor='nw')
    
        label_quiz = tk.Label(quiz_frame, text="ADHD Cognitive Function Screening", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
        label_quiz.place(relx=0.1, rely=0.035, anchor='nw')
    
        main_labelpv = tk.Label(quiz_frame, text="Main", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
        main_labelpv.place(relx=0.95, rely=0.034, anchor='ne')
        
        img_quiz.image = img4
            
        page2.pack_forget()
        quiz_frame.pack(fill="both", expand=True)

    def show_canvas():
        canvas.pack(fill="both", expand=True)

    def open_results_page():
        display_results(canvas, root, show_page2, page2,frame_page2,img_label4,page2_title,main_label,selectanoption_label, selectanoptiontitle_label,logout_button,left_frame,middle_frame,right_frame,img_label5,img_label6,img_label7,image_detection_button,video_detection_button,quizzes_button,submit_samples_button)

    def hideu():     
        global frame_prevideo, imgpv, img_prevideo, label_prevideo, main_labelpv
        frame_prevideo = tk.Label(root, bg="#526b5c", width=2560, height=5, highlightthickness=4, highlightbackground="white")
        imgpv = load_resized_image("5.png", (50, 50))
        img_prevideo = tk.Label(root, image=imgpv, bg="white")
        label_prevideo = tk.Label(root, text="ADHD Cognitive Function Screening", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
        main_labelpv = tk.Label(root, text="Main", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
                       
        frame_prevideo.place(relx=0.5, rely=0.0, anchor='n')
        img_prevideo.place(relx=0.05, rely=0.028, anchor='nw')
        label_prevideo.place(relx=0.1, rely=0.035, anchor='nw')
        main_labelpv.place(relx=0.95, rely=0.034, anchor='ne')
            
        shared.next_button_pressedpv = False
        image_detection_button.place_forget()
        video_detection_button.place_forget()
        quizzes_button.place_forget()
        submit_samples_button.place_forget()
        next_button.place(relx=0.05, rely=0.95, anchor='sw')
        run_adhd_detection1(canvas, root)

    def hided():	
        global frame_video, imgv, img_video, label_video, main_labelv        
        frame_video = tk.Label(root, bg="#526b5c", width=2560, height=5, highlightthickness=4, highlightbackground="white")
        imgv = load_resized_image("5.png", (50, 50))
        img_video = tk.Label(root, image=imgv, bg="white")
        label_video = tk.Label(root, text="ADHD Cognitive Function Screening", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
        main_labelv = tk.Label(root, text="Main", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))    
      
        frame_video.place(relx=0.5, rely=0.0, anchor='n')
        img_video.place(relx=0.05, rely=0.028, anchor='nw')
        label_video.place(relx=0.1, rely=0.035, anchor='nw')
        main_labelv.place(relx=0.95, rely=0.034, anchor='ne')
                
        shared.next_button_pressedpv = True
        shared.next_button_pressedv = False
        image_detection_button.place_forget()
        video_detection_button.place_forget()
        quizzes_button.place_forget()
        submit_samples_button.place_forget()
        quiz_button.place(relx=0.05, rely=0.95, anchor='sw')
        run_adhd_detection2(canvas, root)
       
    page1 = tk.Frame(root, bg="white")
    page1.pack(fill="both", expand=True)
    page2 = tk.Frame(root, bg="white")
    page3 = create_login_page(root, show_page2, go_back_to_page1)
    page4 = create_signup_page(root, show_login_page, go_back_to_page1)

    title_label_page1 = tk.Label(page1, text="ADHD Cognitive Function Screening", bg="white", fg="black", font=("Helvetica", 18, "bold"))
    title_label_page1.place(relx=0.1, rely=0.035, anchor='nw')
    img1 = load_resized_image("3.png", (50, 50))
    img_label1 = tk.Label(page1, image=img1, bg="white")
    img_label1.place(relx=0.05, rely=0.028, anchor='nw')
    img2 = load_resized_image("classroom.png", (1125, 300))
    img_label2 = tk.Label(page1, image=img2, bg="white")
    img_label2.place(relx=0.5, rely=0.32, anchor='center')
    img3 = load_resized_image("combined.png", (806, 260))
    img_label3 = tk.Label(page1, image=img3, bg="white")
    img_label3.place(relx=0.65, rely=0.73, anchor='center')

    signin_button = tk.Button(page1, text="Sign In", command=lambda: [page1.pack_forget(), page3.pack(fill="both", expand=True)], width=10, height=1, bg="#4E9F3D", fg="white", font=("Arial", 16, "bold"), relief="flat")
    signin_button.place(relx=0.05, rely=0.9, anchor='sw')

    signup_button = tk.Button(page1, text="Sign Up", command=lambda: [page1.pack_forget(), page4.pack(fill="both", expand=True)], width=10, height=1, bg="#4E9F3D", fg="white", font=("Arial", 14, "bold"), relief="flat")
    signup_button.place(relx=0.94, rely=0.035, anchor='ne')
    
    about_label_page1 = tk.Label(page1, text="About", bg="white", fg="black", font=("Helvetica", 24, "bold"))
    about_label_page1.place(relx=0.060, rely=0.63, anchor='sw')
    about_description_page1 = tk.Label(page1, text="Our system tracks children's eye gaze on videos and\nimages while analyzing their facial emotions in\nreal-time. It provides valuable insights for early detection\nof ADHD symptoms, supporting parents and professionals\nin understanding cognitive and emotional behaviors.", bg="white", justify="left", fg="black", font=("Helvetica", 10, "bold"))
    about_description_page1.place(relx=0.055, rely=0.77, anchor='sw')

    frame_page2 = tk.Label(page2, bg="#526b5c", width=2560, height=5)
    frame_page2.place(relx=0.5, rely=0.0, anchor='n')
    img4 = load_resized_image("5.png", (50, 50))
    img_label4 = tk.Label(page2, image=img4, bg="white")
    img_label4.place(relx=0.05, rely=0.028, anchor='nw')
    page2_title = tk.Label(page2, text="ADHD Cognitive Function Screening", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
    page2_title.place(relx=0.1, rely=0.035, anchor='nw')
    main_label = tk.Label(page2, text="Main", bg="#526b5c", fg="white", font=("Helvetica", 18, "bold"))
    main_label.place(relx=0.95, rely=0.034, anchor='ne')
    
    selectanoption_label = tk.Label(page2, text="SELECT AN OPTION", bg="white", fg="black", font=("Arial", 24, "bold"))
    selectanoption_label.place(relx=0.5, rely=0.24, anchor='center')
    selectanoptiontitle_label = tk.Label(page2, text="It is recommended to start testing images, videos, and lastly quiz. Quiz is designated for the parent/guardian of the child.", bg="white", fg="black", font=("Arial", 12, "normal"), wraplength=600)
    selectanoptiontitle_label.place(relx=0.5, rely=0.31, anchor='center')

    logout_button = tk.Button(page2, text="LOG OUT", command=go_back_to_page1, width=14, height=1, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    logout_button.place(relx=0.95, rely=0.175, anchor='ne')

    left_frame = tk.Frame(page2, bg="white", width=374, height=300)
    left_frame.place(relx=0.18, rely=0.55, anchor='center')
    middle_frame = tk.Frame(page2, bg="white", width=374, height=300)
    middle_frame.place(relx=0.5, rely=0.55, anchor='center')
    right_frame = tk.Frame(page2, bg="white", width=374, height=300)
    right_frame.place(relx=0.82, rely=0.55, anchor='center')
    canvas = tk.Canvas(page2, width=640, height=480, bg="white")

    img5 = load_resized_image("IMAGES.png", (300, 275))
    img_label5 = tk.Label(left_frame, image=img5, bg="white")
    img_label5.place(relx=0.5, rely=0.5, anchor='center')
    img6 = load_resized_image("VIDEOS.png", (300, 275))
    img_label6 = tk.Label(middle_frame, image=img6, bg="white")
    img_label6.place(relx=0.5, rely=0.5, anchor='center')
    img7 = load_resized_image("QUIZ.png", (300, 275))
    img_label7 = tk.Label(right_frame, image=img7, bg="white")
    img_label7.place(relx=0.5, rely=0.5, anchor='center')
    quiz_frame = tk.Frame(root, bg="white")

    def get_current_user():
        global current_user
        if current_user:
            return current_user
        else:
            return None
    
    current_user = get_current_user()

    create_quiz_page(root, quiz_frame, current_user, show_page2)

    image_detection_button = tk.Button(page2, text="IMAGE", command=lambda: [show_canvas(), root.after(15000, hideu), run_adhd_detection1(canvas, root)], width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")   
    image_detection_button.place(relx=0.18, rely=0.75, anchor='n')
    video_detection_button = tk.Button(page2, text="VIDEO", command=lambda: [show_canvas(), root.after(15000, hided), run_adhd_detection2(canvas, root)], width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    video_detection_button.place(relx=0.5, rely=0.75, anchor='n')

    quizzes_button = tk.Button(page2, text="QUIZ", command=show_quiz_page, width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    quizzes_button.place(relx=0.82, rely=0.75, anchor='n')
    
    submit_samples_button = tk.Button(page2, text="SUBMIT", command=open_results_page, width=14, height=1, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
    submit_samples_button.place(relx=0.5, rely=0.88, anchor='n')
    
    next_button = tk.Button(page2, text="NEXT", command=lambda: [show_canvas(), root.after(6000, hided), run_adhd_detection2(canvas, root)], width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")

    quiz_button = tk.Button(page2, text="NEXT", command=show_quiz_page, width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ADHD Cognitive Function Screening")
    root.geometry("1280x720")
    create_main_page(root)
