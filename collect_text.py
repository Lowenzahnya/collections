import collections


def clear_text(text):
    text = text.lower()
    for i in '.\'?!:;-()[]"`,':
        text = text.replace(i, '')
    return text


def collect(text):
    items = collections.Counter(clear_text(text).split())
    return items


def longest_word(text):
    longest_word = max(collect(text), key=len)
    return f'Самое длинное слово: "{longest_word}", а его длина {len(longest_word)} символов.'


def most_frequent(text):
    counter = collections.Counter(collect(text)).most_common()
    most_word = counter[0][0]
    total = counter[0][1]
    if len(counter) > 1:
        if total == counter[1][1]:
            return f'Все слова встречаются по одному разу'
        else:
            return f'Самое частое слово "{most_word}" - {total} раз(a)'
    else:
        return f'Текст состоит из одного слова'


text = input("Введите текст: ")
print(collect(text))
print(longest_word(text))
print(most_frequent(text))
