import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Say Hi!")
    audio = r.listen(source)

query = r.recognize_google(audio, language = "ru-RU")
print("Вот, что вы сказали", query.lower())
