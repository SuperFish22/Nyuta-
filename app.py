#Голосовой помошник Нюта V-1.0
import os
import time
import datetime
from fuzzywuzzy import fuzz
import dictionary #словарь 
from threading import Thread # многопоточнось 
import random
from googlesearch import search  # поиск в Google
import webbrowser #работа с браузером
from Microphone import inputMicrophone
from speker import speak # функция вывода, разговор
import wikipedia # поиск определений в Wikipedia
from scan import scanIp # сканирование на ip сеть

voice = "" #запись голоса
cmd = "" # Переменная для команд
cmdIn = "" # Переменная ответа
opts = dictionary.opts
spikNuta = dictionary.spikNuta

#поиск по гуглу
def search_for_term_on_google(*args: tuple):
    """
    Поиск в Google с автоматическим открытием ссылок только для пк версии
    """
    search_term = "как какать?"
    search_results = []

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)


def search_wiki(search_term):
    """
    нахождение информации в википедии и озвучивание первого обзаца
    """
    wikipedia.set_lang("ru")
    search_results = wikipedia.summary(search_term, sentences=4) 
    return search_results


def timeIn(): #сколько сейчас времени
    global cmdIn
    now = datetime.datetime.now()
    cmdIn = "Сейчас " + str(now.hour) + ":" + str(now.minute)  

def day():# запоминалка 
    print("Скажите, что надо запомнить?")
    a = input()
    print("я это запомню")

def rand():# орел или решка
    global cmdIn
    flips_count, heads, tails = 3, 0, 0

    for flip in range(flips_count):
        if random.randint(0, 1) == 0:
            heads += 1

    tails = flips_count - heads
    cmdIn = "Орел" if tails > heads else "Решка"

# Оснавная функция main или обработка голоса
def inputNuta(voice):
    global cmd
    if voice.startswith(opts["alias"]): # если обратились к Нюте
        cmd = voice
        for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
        # распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])


# нахождение совпадений в словаре
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC


    
#def ifif():
#    if одина название словаря == 2 части словоря то пускай балакает, иначе чекает список

def execute_cmd(cmd):
    global cmdIn
    #print(cmd)
    
    if cmd == 'ctime':# сказать текущее время
        timeIn()
        
    elif cmd == 'stupid1': # расказать анекдот
        cmdIn = random.randint(0, len('anegdot'-1))
        
    elif cmd == 'live':# поддержка
        cmdIn = random.randint(0, len('live'-1))
    
    elif cmd =='day':# напоминалка
        day()

    elif cmd =='random':# орел или решка
        rand()
    
    elif cmd == 'stop':# ответ на огрессию
        cmdIn = random.randint(0, len(spikNuta['stop']-1))

    elif cmd == 'scan':# скан по ip
        cmdIn = scanIp()

    elif cmd == 'Yes':# да пизда
        cmdIn = "Пизда"

    elif cmd == ' ':
        cmdIn = search_wiki()

    elif cmd == 'searchWiki':
        cmdIn = search_wiki()

    else:
        cmdIn = 'Команда не распознана, повторите!'


def Microphone():
    global voice
    while True:
        voice = inputMicrophone()
        print("[log] Нюта получила: "+ voice)

def goNuta():
    global voice
    while True:
        if (voice != ""):
            inputNuta(voice)

def startSpeak():
    global cmdIn
    while True:
        print("[log] нюта говорит: " + cmdIn)
        if cmdIn != "":
            print("[log] нюта говорит: " + cmdIn)
            speak(cmdIn)
            cmdIn = ""

if __name__ == "__main__":
    print("[log] Нюта начинает грузится...")
    th = Thread(target = Microphone)
    th.start()
    th1 = Thread(target = goNuta)
    th1.start()
    th2 = Thread(target = startSpeak)
    th2.start() 