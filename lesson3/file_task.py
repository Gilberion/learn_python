with open('referat.txt', 'r', encoding='utf-8') as ref:
    content = ref.read()
    print(content)
    print(len(content))
    print(len(content.split()))
    content = content.replace('.', '!')
    print(content)
with open('referat2.txt', 'w', encoding='utf-8') as ref2:
    ref2.write(content)