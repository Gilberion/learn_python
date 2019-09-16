while True:
    ask_user = input('Задай вопрос: ') 
    answer_list = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}
    if answer_list.get(ask_user) != None:
        print(answer_list.get(ask_user))
    else:
        print('Затрудняюсь ответить!')
