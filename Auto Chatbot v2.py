
def pick_option():
    global options, choice
    options = ["My background", "My journey into tech", "Projects I'm proud of", "Skills & certifications"]

    print("What would you like to know?")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")
    try:
        choice = int(input("Enter option here (1-4): "))
        if choice == 1:
            my_background()
        elif choice == 2:
            my_journey()
        elif choice == 3:
            projects_()
        elif choice == 4:
            skill_cert()
        else:
            print("Invalid option. Try again.")
            pick_option()
    except ValueError:
        print("Please enter a number from 1 to 4.")
        pick_option()

def my_background():
    print("""
Kelwyn graduated from George Mason University with a B.S. in Rehabilitation Science. 
Though his degree was in a different field, he pursued a career in Safety & Health, starting as a Coordinator. 
Driven to grow, Kelwyn quickly established a strong reputation for his commitment to learning, compliance, and problem-solving. 
He created new policies and safety measures that significantly reduced incidents and near-miss events across work sites. 
Eventually, he advanced to Safety & Health Specialist at the Pentagon – DoD. 
During this time, he discovered a passion for technology and began exploring the world of computer science.
Click option 2 to learn more about his journey into tech!""")
    pick_option()

def my_journey():
    print("""
Kelwyn’s interest in coding began when he hired freelance developers to create automated stock trading scripts. 
Although the code initially looked like a foreign language, he was determined to understand it. 
He began teaching himself Python and quickly realized how much more he could learn with structured education. 
Kelwyn soon enrolled in Merrimack College’s Master’s in Computer Science program, where he continues building his skills. 
Expected to graduate in Fall 2026, Kelwyn now focuses on hands-on projects that apply what he’s learning to real-world challenges.
Click option 3 to explore some of the projects he’s developed!""")
    pick_option()

def projects_():
    print("""
To date, Kelwyn has created both an automated chatbot and a file integrity verifier. 
The chatbot allowed him to practice core Python skills, while the file integrity verifier introduced him to cybersecurity principles. 
By coding a tool that detects file tampering through hashing, he gained a deeper understanding of how companies ensure digital safety. 
These projects reflect Kelwyn’s growing ability to build purposeful software — and his passion for learning through creation.
Click option 4 to learn more about his education and certifications!""")
    pick_option()

def skill_cert():
    print("""
CompTIA Security + (In progress)
M.S. Computer Science - University of Merrimack (In progress)
B.S. Rehabilitation Science
DoD Cyberawareness training
Public Trust clearance

Skills: Python, critical thinking, organization, adaptability""")
    pick_option()

def opening_greet():
    print("Welcome to my autochatbot! This program is here to tell you a bit about myself. - Kelwyn")
    print("I am K.AI, I am happy to tell you more about Kelwyn.")
    visitor_name = input("What is your name? ")
    print(f"Hello, {visitor_name}.")
    pick_option()

opening_greet()
