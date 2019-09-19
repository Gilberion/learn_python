with open('txt.txt', 'a', encoding='utf-8') as txt:
    txt.write('Привет мир, \n')

with open('txt.txt', 'r', encoding='utf-8') as txt:
    content = txt.read()
    print(content)

with open('txt.txt', 'r', encoding='utf-8') as txt:
    for ln in txt:
        ln =ln.upper()
        print(ln)
