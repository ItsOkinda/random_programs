import pyttsx3
#pip install pyttsx3


def speak_text(text):
    
    engine = pyttsx3.init()

   
    engine.setProperty('rate', 130)  
    engine.setProperty('volume', 1.0)  
    engine.say(text)
    engine.runAndWait()


text = "hello there,,! you are a champ ! don't give up."
speak_text(text)
