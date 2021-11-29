num_dict = {'one': 'один', 'two': 'два',
            'tree': 'три', 'four': 'четыре',
            'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь',
            'nine': 'девять', 'ten': 'десять'}


def num_translate():
    print(num_dict.get(input('Введите число от 1 до 10 по английски: ')))


num_translate()
