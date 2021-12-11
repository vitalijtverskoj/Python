from itertools import zip_longest
from json import dump

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('us_hob.py', 'w', encoding='utf-8') as us_hob:
                z = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                dict = {str(el[0]).strip(): str(el[1]).strip() for el in z}
                dump(dict, us_hob, ensure_ascii=False, indent=4)
            print(dict)
        else:
            exit(1)
