import re
from collections import Counter

def load_data(filepath):
    data = None
    with open(filepath, 'r') as file_with_text:
        data = file_with_text.read()
    return data


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(10)


def show_words(data):
    for position, (x, y) in enumerate(data, start = 1):
        print('{2} "{0}": {1}'.format(x, y, position))


if __name__ == '__main__':
    words = get_most_frequent_words(
        load_data(input('Введите путь к файлу: '))
    )
    show_words(words)
