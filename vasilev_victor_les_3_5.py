from random import choice

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['весёлый', 'яркий', 'зелёный', 'утопичный', 'мягкий']


def get_jokes(n):

    """
    Функция генерирует шутки
    n: количество шуток
    return: список шуток
    """

    list_jokes = []
    while n != 0:
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n = n - 1
    print(list_jokes)
    return list_jokes


get_jokes(int(input('Количество шуток: ')))
