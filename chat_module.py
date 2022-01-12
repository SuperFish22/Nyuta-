#opts = {
   # "cmds": {
   #    "stop":('стоп','надоела','заткнись'),
   #    "starttalkq":('привет','здравствуй'),
   #    "delaq":('как дела','как ты'),
   #    "cancelq":('нет','отмена')
   #     }   ###Вставить модуль словаря в команды

   #chitchat = {
   # "starttalka": ('Ну как тебе отказать то. О чем поговорим?', 'Да, конечно. О чем поговорим?'),
   # "delaa": ('Да нормально в общем-то', 'Не жалуюсь', 'Могло быть и лучше'),
   # "cantanswera": ('Не совсем поняла вас. Могу посмотреть что вы имели в виду', 'Что вы имеете в виду? Мне поискать?', 'Абоба'),
   # "cancela": ('Ладно', 'Хорошо', 'Абоба, но отрицательная'),
   # "stopa":('Я вас поняла останавливаюсь','Не огресируйте уже все','бу бу бу ')

    #}   ###Модуль ответов

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
