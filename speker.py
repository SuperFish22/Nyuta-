# *Нужно добавить смену голоса
# https://gb.ru/posts/tts_python

import pyttsx3

tts = pyttsx3.init() # Инициализировать голосовой движок.

def speak(text):
    tts.say(text)
    tts.runAndWait()

def speakOption(speed,volume):
    tts.setProperty('rate', speed)    # Скорость в % (может быть > 100)
    tts.setProperty('volume', volume)  # Громкость (значение от 0 до 1)

if "__main__" == __name__:
    speak("Привет как дела ?")
    txt = input()
    speak(txt)