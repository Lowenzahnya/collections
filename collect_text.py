import collections
import pdfplumber
from pathlib import Path


# noinspection PyTypeChecker
def pdf_file(file_path):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file_path, 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        return text


def txt_file(file_path):
    if Path(file_path).is_file() and Path(file_path).suffix == '.txt':
        text = open(file_path, encoding='utf-8').read()
        return text


def clear_text(text):
    text = text.lower()
    for i in '.\'?!:;-()[]"`,':
        text = text.replace(i, '')
    return text


def collect(text):
    items = collections.Counter(clear_text(text).split())
    return items


def longest_word(collector):
    sorted_words = sorted(collector, key=len, reverse=True)
    words = [sorted_words[0]]
    i = 1
    while len(sorted_words[0]) == len(sorted_words[i]):
        words.append(sorted_words[i])
        i += 1
    return words


file_path = input("File's path: ")
while True:
    try:
        if file_path.endswith('pdf'):
            pdf_ = pdf_file(file_path)
            collector = collect(pdf_)
        elif file_path.endswith('txt'):
            txt_ = txt_file(file_path)
            collector = collect(txt_)
        else:
            print('Неопознанный файл')
            break
        # noinspection PyUnboundLocalVariable
        if len(collector) == 0:
            print('Пустой файл')
            break
        else:
            mf = collector.most_common()
            if len(mf) > 1:
                if mf[0][1] == mf[1][1] == 1:
                    print(f'Все слова встречаются по одному разу:')
                    for word, amount in mf:
                        print(word, end=' ')
                    break
                else:
                    lw = longest_word(collector)
                    if len(lw) >= 2:
                        print("Самые длинные слова:", *lw, f"- их длина {len(lw[0])} символов.")
                    else:
                        print(f'Самое длинное слово: "{lw[0]}", а его длина {len(lw[0])} символов.')
                    print(f'Самое частое слово: "{mf[0][0]}" - {mf[0][1]} раз(a)\n')
            else:
                print(f'Текст состоит из одного слова "{mf[0][0]}" повторяющегося {mf[0][1]} раз')
        for word, amount in mf[1:]:
            print(f'Слово "{word}" встречается {amount} раз')
        break
    except AttributeError:
        print('Файл не найден')
        break
    except FileNotFoundError:
        print('Файл не найден')
        break
    except UnicodeDecodeError:
        print('Невозможно раскодировать файл')
        break
