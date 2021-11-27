less_list_1 = ['в', '5', 'часов', '17', 'минут', 'температура',
               'воздуха', 'была', '+5', 'градусов']
less_list_2 = []

#   ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут','температура',
#   'воздуха', 'была', '"', '+05', '"', 'градусов']


for n in less_list_1:
    if n[1:].isdigit() or n.isdigit():
        less_list_2.append('"')
        if n.isdigit():
            less_list_2.append(f'{int(n):02d}')
        else:
            less_list_2.append(f'{n[0]}{int(n[1:]):02d}')
        less_list_2.append('"')
    else:
        less_list_2.append(n)
print(less_list_2)
print(" ".join(less_list_2))
