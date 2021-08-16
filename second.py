text_ = input('''Enter text ''')

def some_code(text ):
    lst = []
    for i in text.lower().split():
        if i[0] in lst:
            i+= i[1:]
        lst.append(i)
    _dict = dict()
    for i in lst:
        _dict[i] = _dict.get(i, 0) + 1
    _list = []
    for key, i in _dict.items():
        _list.append((i, key))
        _list.sort(reverse=True)
    for key, i in _list[:3]:
        if len(_list)<3:
            return _list
        print(f'{i:}')
some_code(text_)
