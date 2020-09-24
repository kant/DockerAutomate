import speech_recognition as sr
import webbrowser
import pyttsx3
print()
print("Here is the Program which launch or stop Docker for You")
print()
pyttsx3.speak("Hello I am john")
pyttsx3.speak("I am here to help you to launch and stop your docker container")
pyttsx3.speak("Tell me your requirement") 
r=sr.Recognizer()
with sr.Microphone() as source:
 print("I am Listening to You....")
 audio=r.listen(source)
 print("Done...")
text=r.recognize_google(audio)
print(text)

if ("run" in text) or ("launch" in text) and ("docker" in text) or ("container" in text):
 webbrowser.open("http://192.168.43.107/index.html")
 pyttsx3.speak("Opening a Page launch Docker")
elif ("stop" in text) and ("docker" in text) or ("container" in text):
 webbrowser.open("http://192.168.43.107/stop.html")
 pyttsx3.speak("Opening a Page to stop Docker")
else:
 print("Sorry")
