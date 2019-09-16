age = int(input('Введите ваш возраст в земных годах: '))

def age_counter(age):
    if age < 3:
        return 'Сидите дома!'
    elif 3 <= age < 7:
        return 'Маме пора работать. Вам -  в сад!'
    elif 7 <= age < 18:
        return 'Теперь 1 сентября - Ваш праздник'
    elif 18 <= age < 25:
        return 'Пора получать вышку'
    else:
        return 'Пора пахать как краб на галерах'

result = age_counter(age)
print(result)
        


