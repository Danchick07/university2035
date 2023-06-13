import pyaudio # pip install pyaudio
import speech_recognition as sr #pip install speechRecognition
import pyttsx3 #pip install pyttsx3
import random
import webbrowser

rec = sr.Recognizer() # Распознаватель

# print(sr.Microphone.list_microphone_names())

voice = pyttsx3.init()
voice.say('Привет! Я голосовой помощник!')
voice.runAndWait()

list_hi = ['привет', "хай", "здравствуй", "хэллоу"]

while True:
    with sr.Microphone(device_index=1) as source:
        rec.adjust_for_ambient_noise(source, duration=3) # Команда, если выдаёт ошибку.
        print('Скажите что-нибудь...')
        audio = rec.listen(source)
    text = rec.recognize_google(audio, language='ru_RU')

    # voice.say(text + "бууээээ")
    # voice.runAndWait()
    if 'привет' in text.lower():
        voice.say(random.choice(list_hi))
        voice.runAndWait()
    elif 'как дела' in text.lower():
        voice.say("пока не родила")
        voice.runAndWait()
    elif 'youtube' in text.lower():
        webbrowser.open_new('https://www.youtube.com/')
        voice.say("ютуб запущен")
        voice.runAndWait()
    elif 'элжур' in text.lower():
        webbrowser.open_new('https://sch56.eljur.ru/journal-user-prefs-action')
        voice.say("дневник запущен")
        voice.runAndWait()
    elif 'анекдот' in text.lower():
        voice.say(" Молодой мужчина просит гадалку рассказать, что ждет его в будущем , Гадалка раскинула карты и говорит:— Предупреждаю, на вашем пути встанет один человек. — Вы лучше предупредите его, потому что я гонщик. ХАХАХАХАХАХАХАХХАХАХАХ")
        voice.runAndWait()
