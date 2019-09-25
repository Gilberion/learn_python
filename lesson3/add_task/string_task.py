word = 'Архангельск'

# Вывести последнюю букву в слове
print(word[-1])

# Вывести количество букв "а" в слове
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
count_vowel = 0
vowel_list ='аоэеиыуёюя'
for let in word.lower():
    if let in vowel_list:
        count_vowel = count_vowel + 1
print(count_vowel) 


sentence = 'Мы приехали в гости'

# Вывести количество слов в предложении
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
for word_2 in sentence.split():
    print(word_2[0]) 

# Вывести усреднённую длину слова.
value_len = 0
count_word = 0
for word_2 in sentence.split():
    value_len = value_len + len(word_2)
    count_word = count_word + 1
print(value_len/count_word)


