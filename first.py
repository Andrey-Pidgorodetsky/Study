a=('Abcdefghij')
b=2
def encrypt(text, n):

    if(n < 1):
        return text

    if text == None or text == '':
        print('You need enter text')
        return text

    result_str = text

    odd_chars = []
    even_chars = []
    for idx, char in enumerate(result_str):
        if (idx + 1) % 2 == 0:
            even_chars.append(char)
        else:
            odd_chars.append(char)
        result_str = (''.join(even_chars)) + (''.join(odd_chars))

    return encrypt(result_str, n - 1)

c=encrypt(a, b)
print(c)
def derypt(text, n):
    if(n < 1):
        return text
    if text == None or text == '':
        return text
    result_str = text
    odd_chars = []
    even_chars = []
    for idx, char in enumerate(result_str):
        if (idx + 1) % 2 == 0:
            odd_chars .append(char)
        else:
            even_chars.append(char)
        result_str = (''.join(even_chars)) + (''.join(odd_chars))

    return encrypt(result_str, n - 1)
print(derypt(c,b))
