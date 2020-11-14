import pyttsx3
import speech_recognition as sr
import os



def myCommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print('Say something...') 
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=1) 
        audio = r.listen(source) 
        try:
            command = r.recognize_google(audio).lower() 
            print('You said: ' + command + '\n') #loop back to continue to listen for commands if unrecognizable speech is received 
        except sr.UnknownValueError: 
            print('....') 
            command = myCommand()
    return command

def sofiaResponse(audio): 
    print(audio)
    for line in audio.splitlines(): 
        os.system("say " + audio)
    
def assistant(cmd):
    if "say hi" in cmd:
        print("Heellooo")
while True: 
    assistant(myCommand())

