import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import datetime

# Initialize the text-to-speech engine for pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Set speech rate

# Function to set the voice (male or female) for pyttsx3
def set_voice_(gender="male"):
    voices = engine.getProperty('voices')
    if gender == "female":
        engine.setProperty('voice', voices[1].id)  # Female voice (typically at index 1)
    else:
        engine.setProperty('voice', voices[0].id)  # Male voice (typically at index 0)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand your command.")
        except sr.RequestError:
            speak("Sorry, there was an issue with the recognition service.")
    return ""

# Function to handle user commands
def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {today}")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "search for" in command:
        search_term = command.replace("search for", "").strip()
        speak(f"Searching for {search_term} on Google")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    elif "play music" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "search youtube for" in command:
        search_term = command.replace("search youtube for", "").strip()
        speak(f"Searching for {search_term} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
    elif "news" in command:
        speak("Opening news website")
        webbrowser.open("https://www.google.com/news")
    elif "open email" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    # Education Section
    elif "UG Course " in command:
        speak("Which degree are you interested in? I can help with B-Tech, BBA, BCA, BCS")
        degree_type = listen()

        if "B-Tech" in degree_type:
            speak("Opening the best colleges for B-Tech")
            webbrowser.open("https://academics.iitd.ac.in/")
            webbrowser.open("https://admissions.mitwpu.edu.in/")
            webbrowser.open("https://b-tech.sycet.org/")
            webbrowser.open("https://dypatiluniversitypune.edu.in/")
            webbrowser.open("https://metbhujbalknowledgecity.ac.in/")
        elif "BBA" in degree_type:
            speak("Opening the best colleges for BBA.")
            webbrowser.open("https://admissions.mitwpu.edu.in/")
            webbrowser.open("https://b-tech.sycet.org/")
            webbrowser.open("https://ditms.org/")
            webbrowser.open("https://www.mgmmumbai.ac.in/")
        elif "BCA" in degree_type:
            speak("Opening the best colleges for BCA.")
            webbrowser.open("https://ditms.org/")
            webbrowser.open("https://www.mgmmumbai.ac.in/")
            webbrowser.open("https://metbhujbalknowledgecity.ac.in/")
        elif "BCS" in degree_type:
            speak("Opening the best colleges for BCS.")
            webbrowser.open("https://ditms.org/")
            webbrowser.open("https://www.mgmmumbai.ac.in/")
            webbrowser.open("https://b-tech.sycet.org/")
            webbrowser.open("https://metbhujbalknowledgecity.ac.in/")
        else:
            speak("Sorry, I couldn't find specific colleges for that degree. Please try again.")

    elif "PG Course" in command:
        speak("Which degree are you interested in? I can help with MCA, MBA, M-Tech.")
        degree_type = listen()

        if "MCA" in degree_type:
            speak("Opening the best colleges for MCA.")
            webbrowser.open("https://ifeel.edu.in/")
            webbrowser.open("https://www.mgmmumbai.ac.in/")
            webbrowser.open("https://b-tech.sycet.org/")
            webbrowser.open("https://metbhujbalknowledgecity.ac.in/")
        elif "MBA" in degree_type:
            speak("Opening the best colleges for MBA")
            webbrowser.open("https://ifeel.edu.in/")
            webbrowser.open("https://www.mgmmumbai.ac.in/")
            webbrowser.open("https://metbhujbalknowledgecity.ac.in/")
        elif "M-Tech" in degree_type:
            speak("Opening the best colleges for M-Tech")
            webbrowser.open("https://christuniversity.in/")
            webbrowser.open("https://admissions.mitwpu.edu.in/")

    #  Professional Course larning
    elif "learn cyber security" in command:
        speak("Opening websites for learning cyber security.")
        webbrowser.open("https://www.connectinwhizttech.com/")

    # Coding Courses
    elif "coding courses" in command:
        speak("Online courses learning platforms")
        Course_type = listen()

        if "python" in Course_type:
            speak("Opening the Python online learning sites.")
            webbrowser.open("https://swayam.gov.in/")
            webbrowser.open("https://www.coursera.org/")
            webbrowser.open("https://www.udemy.com/")
            webbrowser.open("https://www.khanacademy.org/")
        elif "Java" in Course_type:
            speak("Opening the Java online learning sites.")
            webbrowser.open("https://swayam.gov.in/")
            webbrowser.open("https://www.khanacademy.org/")
            webbrowser.open("https://onlinecourses.nptel.ac.in/")
        elif "C Language" in Course_type:
            speak("Opening the C online learning sites.")
            webbrowser.open("https://www.mygreatlearning.com/")
            webbrowser.open("https://www.learnvern.com/")
            webbrowser.open("https://www.coursera.org/")
        elif "c++" in Course_type:
            speak("Opening the C++ online learning sites.")
            webbrowser.open("https://www.mygreatlearning.com/")
            webbrowser.open("https://www.coursera.org/")
        elif "html" in Course_type:
            speak("Opening the HTML online learning sites.")
            webbrowser.open("https://onlinecourses.nptel.ac.in/")
            webbrowser.open("https://www.coursera.org/")
            webbrowser.open("https://www.khanacademy.org/")
        elif "css" in Course_type:
            speak("Opening the CSS online learning sites.")
            webbrowser.open("https://www.khanacademy.org/")
            webbrowser.open("https://www.learnvern.com/")
            webbrowser.open("https://www.mygreatlearning.com/")
        elif "javascript" in Course_type:
            speak("Opening the JavaScript online learning sites.")
            webbrowser.open("https://onlinecourses.nptel.ac.in/")
            webbrowser.open("https://www.learnvern.com/")

    # Translation
    elif "translate" in command:
        speak("Please say the text you want to translate to Hindi or Marathi.")
        translate = listen()
        if translate:
            speak(f"Translating {translate} to Hindi and Marathi.")
            pyautogui.open(f"https://translate.google.com/?sl=en&tl=hi&text={translate}")
        else:
            speak("I didn't understand the text. Please try again.")

    # UPSC and MPSC Exams
    elif "upsc" in command:
        speak("Opening the UPSC exam website")
        webbrowser.open("https://www.upsc.gov.in/")
    elif "mpsc" in command:
        speak("Opening the MPSC exam website")
        webbrowser.open("https://www.mpsc.gov.in/")

    # Exit condition
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I am not sure how to help with that.")

# Main loop
def main():
    speak("Hello, I am your personal assistant. Would you like a male or female voice?")

    # Ask the user to select voice
    gender = listen()

    # Set voice based on user choice
    if "female" in gender:
        set_voice_("female")
        speak("You have selected a female voice.")
    else:
        set_voice_("male")
        speak("You have selected a male voice.")

    # Start listening and handling commands
    while True:
        command = listen()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
