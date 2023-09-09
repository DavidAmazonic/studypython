def palindromo(text):
    Value = False
    text = text.replace(' ', '')
    text = text.strip()
    text = text.lower()
    alreves = arevesadobe(text)
    print(alreves)
    if alreves == text:
        Value = True
    return Value


def arevesadobe(text):
    Valur = ""
    num = len(text)
    r = 0
    for i in range(num):
        r = num - i - 1
        Valur += text[r]
    return Valur


x = input("Palindromo: ")
print(x, palindromo(x))
