import re
from collections import defaultdict

def load_data(filepath):
    data = None
    with open(filepath, 'r') as file:
        data = file.read()
    return data


def get_most_frequent_words(text):
    words = defaultdict(int) # provide initial value for new keys 
    for word in re.split(r'\W+', text):
    	words[word] += 1
    return sorted(words.items(), key = lambda x: x[1], reverse = True)[:10]


def show_words(data):
	for position, (x, y) in enumerate(data, start = 1):
		print('{2} "{0}": {1}'.format(x, y, position))


if __name__ == '__main__':
    words = get_most_frequent_words(
    	load_data(input('Введите путь к файлу: '))
    )
    show_words(words)
