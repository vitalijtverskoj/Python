num_dict = {'one': 'один', 'two': 'два',
            'tree': 'три', 'four': 'четыре',
            'five': 'пять', 'six': 'шесть',
            'seven': 'семь', 'eight': 'восемь',
            'nine': 'девять', 'ten': 'десять'}


def num_translate_adv():
    num = input('Введите число от 1 до 10 по английски: ')
    if num.istitle() and num_dict.get(num.lower()) is not None:
        print(num_dict.get(num.lower()).title())
    else:
        print(num_dict.get(num))


num_translate_adv()
