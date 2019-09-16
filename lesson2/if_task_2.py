str_1 = input('Введите что-нибудь: ')
str_2 = input('Введите что-нибудь еще: ')
print(str_1)
print(str_2)

def string_compare(str_1, str_2):
    if type(str_1) != str and type(str_2) != str:
        return '0'
    if str_1 == str_2:
        return '1'
    if str_1 != str_2 and len(str_1) >  len(str_2):
        return '2'
    if str_1 != str_2 and str_2 == 'learn':
        return '3'
    
result = string_compare(str_1, str_2)
print(result)

