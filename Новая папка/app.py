#Голосовой помошник Нюта V-1.0
import os
import time
import flask
import datetime
from fuzzywuzzy import fuzz
import slovar #словарь 



def talk(cmd):
    global cmdIn
    print (cmd)
    if cmd == "starttalkq":
        random_cmd= random.randint(0, len('starttalka'-1), + '. Если вам надоест дайте знать')
        cmdIn=random_cmd
    elif cmd == "delaq":
        random_cmd= random.randint(0, len('delaa'-1))
        cmdIn=random_cmd
    elif cmd == 'cancelq':
        random_cmd= random.randint(0, len('cancela'-1))
        cmdIn=random_cmd
    elif cmd == 'stop':
        random_cmd= random.randint(0, len('stopa'-1))
        cmdIn=random_cmd
    else:
        random_cmd= random.randint(0, len('cantanswera'-1))
        cmdIn=random_cmd


cmd = "" # Переменная для команд
cmdIn = "" # Переменная ответа
opts = slovar.opts

def speak(): # функция вывода, разговор
    global cmdIn
    print(cmdIn)
    cmdIn = ""

def inputNuta():# Оснавная функция main или обработка голоса
    global cmd
    print("я принимю информацию:")
    voice = input()
    if voice.startswith(opts["alias"]): # если обратились к Нюте
        cmd = voice

        for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
        
        for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

        # распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
    

def execute_cmd(cmd):
    global cmdIn
    print(cmd)
    if cmd == 'ctime':# сказать текущее время
        timeIn()

    elif cmd == 'stupid1':
        cmdIn = "колобок повесился"

    elif cmd == 'live':
        cmdIn = "я тебя люблю"
    
    elif cmd =='spic':
        speak()
    
    elif cmd =='day':
        day()

    else:
        cmdIn = 'Команда не распознана, повторите!'

def timeIn():
    global cmdIn
    now = datetime.datetime.now()
    cmdIn = "Сейчас " + str(now.hour) + ":" + str(now.minute)

def spiket():
    print("скажите когда вам надоест")
    

def day():
    print("Скажите, что надо запомнить?")
    a = input()
    print("я это запомню")
    



if __name__ == "__main__":
    print("Go")
    while True:
        inputNuta() # получаем команду
        speak() # отвечаем 