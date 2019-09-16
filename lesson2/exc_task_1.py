while True:
    def ask_user(ask):
        answer_list = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}
        if answer_list.get(ask) != None:
            answer = (answer_list.get(ask)) 
            print(answer)  
        else:
            answer = 'Затрудняюсь ответить!'
            print(answer)

    try:
        ask_user(input('Задай вопрос: '))
    except(KeyboardInterrupt):
        print('Пока!')
        break
