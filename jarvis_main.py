import pyttsx3
import speech_recognition

engin = pyttsx3.init("sapi5")
voices = engin.getProperty("voices")
engin.setProperty("voises",voices[0].id)
engin.setProperty("reat",170)

def speak(audio):
    engin.say(audio)
    engin.runAndwait()

def teckcommand():
    r = speech_recognition.reconizer
    with speech_recognition.microphne as source:
        print("Listining....")
        r.pause_threshold = 1
        r.engin.threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanging...")
        query = r.recognize_google(audio,language = ' en-in')
        print(f"you said : {query}\n")

    except Exception as e :
        print("say that again ")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = teckcommand().lower()
        if "wake up" in query :

