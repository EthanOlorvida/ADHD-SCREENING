import tkinter as tk
from tkinter import messagebox
from auth import save_quiz
import shared

def create_quiz_page(root, parent_frame, current_user, show_page2):
    def clear_page():
        for widget in parent_frame.winfo_children():
            widget.pack_forget()

    parent_frame.config(bg="white")

    intro_text = ("Instructions: This questionnaire is designed to determine whether your child demonstrates symptoms similar to those "
                  "of children with Attention Deficit Hyperactivity Disorder (ADHD) and is intended to be used as a screening tool.")

    questions_group1 = [
        "Often fails to give close attention to details or makes careless mistakes in school or at home.",
        "Often has trouble holding attention on tasks or play activities (easily distracted).",
        "Often does not seem to listen when spoken to directly (not holding eye contact, looking elsewhere).",
        "Often does not follow through on instructions and fails to finish schoolwork or chores, because of getting distracted.",
        "Often has trouble organizing tasks and activities (a huge problem with organization and with prioritization).",
        "Often avoids, dislikes, or is reluctant to do tasks that require mental effort over a long period of time (e.g., schoolwork or homework; instead functions by hyper-focused energy followed by very low energy times).",
        "Often loses things necessary for tasks and activities (misplaces things all the time).",
        "Often easily distracted by extraneous stimuli.",
        "Often forgetful in daily activities."
    ]

    questions_group2 = [
        "Often fidgets or taps hands or feet (di mapakali).",
        "Often leaves the seat in situations where remaining seated is expected (e.g., one of those people who needs to get up 17 times while watching a movie).",
        "Often runs about or climbs in situations where it’s not appropriate.",
        "Often unable to play or take part in a leisure activity quietly (hyper all the time).",
        "Often on the go, acting as if driven by a motor.",
        "Often talks excessively (talks too much)."
    ]

    questions_group3 = [
        "Often blurts out an answer before a question has been completed (impulsive).",
        "Often has trouble waiting for their turn.",
        "Often interrupts or intrudes on others (unable to keep things to themselves, butting in)."
    ]

    all_questions = questions_group1 + questions_group2 + questions_group3
    questions_per_page = 3
    num_pages = (len(all_questions) + questions_per_page - 1) // questions_per_page

    user_answers = {}
    current_page = 0

    def save_quiz_responses():
        responses = {q_number: answer.get() for q_number, answer in user_answers.items()}
        if responses:
            score_map = {"Not at all": 0, "Just a little": 1, "Often": 2, "Very Often": 3}
            scored_responses = {q_number: score_map[answer] for q_number, answer in responses.items() if answer}
            
            formatted_responses = ','.join(f"{q_number}:{score}" for q_number, score in scored_responses.items())

            inattentive_count = sum(1 for q_number in range(9) if scored_responses.get(q_number, 0) >= 2)
            hyperactive_count = sum(1 for q_number in range(9, 15) if scored_responses.get(q_number, 0) >= 2)
            impulsive_count = sum(1 for q_number in range(15, 18) if scored_responses.get(q_number, 0) >= 2)

            if inattentive_count >= 6 and hyperactive_count >= 6:
                message = ("Based on your responses to this child ADHD screening test, your child shows similarities with children who have symptoms of a Combined Type of Attention Deficit Hyperactivity Disorder (ADHD).")
                message2 = ("While this is not a formal diagnosis or treatment recommendation, it may be helpful to seek further evaluation from a qualified mental health professional.")
                message3 = ("Recommendations:\n"

                             "To support children with ADHD, it’s important to limit or avoid the following:\n"
                             "- Artificial additives: Food dyes, artificial flavors, and preservatives like Red 40, Yellow 5, and sodium benzoate.\n"
                             "- Refined sugars: Found in candies, sodas, and sweet snacks, which can trigger hyperactivity.\n"
                             "- Caffeine: Found in sodas, energy drinks, and chocolate, as it may overstimulate.\n"
                             "- Processed and fast foods: High in unhealthy fats, salt, and additives.\n"
                             "- Potential allergens: Dairy, gluten, soy, and other allergens if sensitivities are present.\n"

                             "Focus on a balanced diet rich in whole foods, lean proteins, vegetables, and healthy fats to help manage symptoms. Consult a healthcare professional for tailored advice.")
            elif inattentive_count >= 6:
                message = ("Based on your responses to this child ADHD screening test, your child shows similarities with children who have symptoms of an Inattentive Type of Attention Deficit Hyperactivity Disorder (ADHD).")
                message2 = ("While this is not a formal diagnosis or treatment recommendation, it may be helpful to seek further evaluation from a qualified mental health professional.")
                message3 = ("Recommendations:\n"

                             "To support children with ADHD, it’s important to limit or avoid the following:\n"
                             "- Artificial additives: Food dyes, artificial flavors, and preservatives like Red 40, Yellow 5, and sodium benzoate.\n"
                             "- Refined sugars: Found in candies, sodas, and sweet snacks, which can trigger hyperactivity.\n"
                             "- Caffeine: Found in sodas, energy drinks, and chocolate, as it may overstimulate.\n"
                             "- Processed and fast foods: High in unhealthy fats, salt, and additives.\n"
                             "- Potential allergens: Dairy, gluten, soy, and other allergens if sensitivities are present.\n"

                             "Focus on a balanced diet rich in whole foods, lean proteins, vegetables, and healthy fats to help manage symptoms. Consult a healthcare professional for tailored advice.")
            elif hyperactive_count >= 6:
                message = ("Based on your responses to this child ADHD screening test, your child shows similarities with children who have symptoms of a Hyperactive-Impulsive Type of Attention Deficit Hyperactivity Disorder (ADHD).")
                message2 = ("While this is not a formal diagnosis or treatment recommendation, it may be helpful to seek further evaluation from a qualified mental health professional.")
                message3 = ("Recommendations:\n"

                             "To support children with ADHD, it’s important to limit or avoid the following:\n"
                             "- Artificial additives: Food dyes, artificial flavors, and preservatives like Red 40, Yellow 5, and sodium benzoate.\n"
                             "- Refined sugars: Found in candies, sodas, and sweet snacks, which can trigger hyperactivity.\n"
                             "- Caffeine: Found in sodas, energy drinks, and chocolate, as it may overstimulate.\n"
                             "- Processed and fast foods: High in unhealthy fats, salt, and additives.\n"
                             "- Potential allergens: Dairy, gluten, soy, and other allergens if sensitivities are present.\n"

                             "Focus on a balanced diet rich in whole foods, lean proteins, vegetables, and healthy fats to help manage symptoms. Consult a healthcare professional for tailored advice.")
            else:
                message = ("Based on your responses to this child ADHD screening test, your child does not seem to exhibit characteristics typically associated with Attention Deficit Hyperactivity Disorder (ADHD).")
                message2 = ("However, please note that this is not a definitive diagnosis. If you wish to explore the results further, we encourage you to consult a specialist.")
                message3 = ("Recommendations:\n"

                             "To support children with ADHD, it’s important to limit or avoid the following:\n"
                             "- Artificial additives: Food dyes, artificial flavors, and preservatives like Red 40, Yellow 5, and sodium benzoate.\n"
                             "- Refined sugars: Found in candies, sodas, and sweet snacks, which can trigger hyperactivity.\n"
                             "- Caffeine: Found in sodas, energy drinks, and chocolate, as it may overstimulate.\n"
                             "- Processed and fast foods: High in unhealthy fats, salt, and additives.\n"
                             "- Potential allergens: Dairy, gluten, soy, and other allergens if sensitivities are present.\n"  

                             "Focus on a balanced diet rich in whole foods, lean proteins, vegetables, and healthy fats to help manage symptoms. Consult a healthcare professional for tailored advice.")

            shared.message = message
            shared.message2 = message2
            shared.message3 = message3
            if save_quiz(current_user, formatted_responses):
                print(f"Quiz responses saved for {current_user}")

            parent_frame.pack_forget()
            show_page2()

    def create_question_page(page):
        clear_page()

        def on_back():
            if page == 0:
                parent_frame.pack_forget()
                show_page2() 
            else:
                navigate_to_page(page - 1)
                
        back_button = tk.Button(parent_frame, text="←", command=on_back, bg="white", font=("Arial", 14, "bold"), bd=0,highlightthickness=0, relief="flat")
        back_button.pack(padx=20, pady=(100,0), anchor="w")

        if page == 0:
            intro_label = tk.Label(parent_frame, text=intro_text, bg="white", justify="left", fg="black", font=("Helvetica", 12), wraplength=600)
            intro_label.pack(anchor="w", padx=20, pady=(20,0))

        start_index = page * questions_per_page
        end_index = min(start_index + questions_per_page, len(all_questions))

        for i in range(start_index, end_index):
            
            question_text = all_questions[i]
            question_label = tk.Label(parent_frame, text=question_text, bg="white", justify="left", fg="black", font=("Helvetica", 14), wraplength=1240)

            if i == start_index and page != 0:
                question_label.pack(anchor="w", padx=20, pady=(100, 20)) 
            else:
                question_label.pack(anchor="w", padx=20, pady=20)

            options = ["Not at all", "Just a little", "Often", "Very Often"]
            var = tk.StringVar(value="") 
            option_menu = tk.OptionMenu(parent_frame, var, *options)
            option_menu.pack(anchor="w", padx=40, pady=5)
            user_answers[i] = var

        if page < num_pages - 1:
            next_button = tk.Button(parent_frame, text="Next", command=lambda: navigate_to_page(page + 1), 
            width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
            next_button.pack(padx=40, pady=(50,20), anchor="w")
        else:
            save_button = tk.Button(parent_frame, text="Save", command=save_quiz_responses,
            width=28, height=2, bg="#526b5c", fg="white", font=("Arial", 16, "bold"), relief="flat")
            save_button.pack(padx=40, pady=(50,20), anchor="w")

    def navigate_to_page(page):
        nonlocal current_page
        current_page = page
        create_question_page(page)

    navigate_to_page(current_page)
