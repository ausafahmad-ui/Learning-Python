
import speech_recognition as sr
import webbrowser
import pyttsx3

#initialize both here or stasrt
recogniser=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.setProperty("rate", 10)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Listening...")
    

    while True:
        try:
            with sr.Microphone() as source:  # Open microphone
                print("Say something!")
                audio = recogniser.listen(source,timeout=2,phrase_time_limit=5)     # Record your voice
            # if audio == "stop":
            #     break
            print("Analysing...")    
            text = recogniser.recognize_google(audio) # Convert speech to text
            engine.say(text)
            engine.runAndWait()  
            print(text)

        except sr.UnknownValueError:
            print("Sorry did not catch")  