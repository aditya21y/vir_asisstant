from cgitb import text
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia

ts = pyttsx3.init()
rec = sr.Recognizer()
mic = sr.Microphone()

text2 = "hallo im jarvis your virtual assistant, what can i do for you"
ts.say(text2)
ts.runAndWait()

x = True
while x:
    with mic as source:
        print("listening...")
        audio=rec.listen(source)
        text1 = rec.recognize_google(audio)
        text1 = text1.lower()
        if "who" in text1:
            text1_answer = "im jarvis your virtual assistant, yes what can i do for you sir!"
            ts.say(text1_answer)
            ts.runAndWait()
        elif "play"in text1:
            text1=text1.replace("play","")
            play_text = "playing",text1
            pywhatkit.playonyt(text1)
            ts.say(play_text)
            ts.runAndWait()
        elif "search" in text1:
            text1=text1.replace("search","")
            serach_text = "searcing.",text1
            pywhatkit.search(text1)
            ts.say(serach_text)
            ts.runAndWait()
        elif "what" in text1:
            text1=text1.replace("what","")
            what_text = wikipedia.summary(text1)
            ts.say(what_text)
            ts.runAndWait()
        elif "stop" in text1:
            stop_text="stoping my program. have a good day sir!"
            ts.say(stop_text)
            ts.runAndWait()
            x=False
    #print(text1)