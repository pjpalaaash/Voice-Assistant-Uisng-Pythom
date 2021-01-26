import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello,Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon!")   

    else:
        speak("Hello,Good Evening!")  

    speak("Hello sir i am Jofraa. Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
         

    except Exception:    
        print("Say that again please...")  
        return "None"
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('idnum50@gmail.com', 'Youtube50')
    server.sendmail('idnum50@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    Greeting()
    while True:
    
        query = takeCommand().lower()

    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'F:\\Songs1'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\PALASH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pjpallu55@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Palash bhai. I am not able to send this email")    

        elif 'exit' in query:
            speak("Exiting sir, Thankyou for using")
            exit()
 
        elif 'your name' in query:
            speak("my name is jofraa sir") 

        elif 'who are you' in query:
            speak("im a voice assistant sir")      

        elif 'message' in query:
            speak("Whats the message sir")
            mess = takeCommand()
            speak(mess)
        elif 'good' in query:
            speak("Thankyou sirr.") 

        elif 'my college website' in query:
            webbrowser.open("sistec.ac.in")       
            
   
 