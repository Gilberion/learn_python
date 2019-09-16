import random

def cut_cake(people):
    try:    
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except:# (ZeroDivisionError, TypeError):
        print('Не могу делить')


cut_cake('4')

while True:
    p = random.randint(1, 10)
    cut_cake(p)