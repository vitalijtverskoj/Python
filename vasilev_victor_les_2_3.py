less_list = ['в', '5', 'часов', '17', 'минут', 'температура',
             'воздуха', 'была', '+5', 'градусов']
x = 0
#   ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут','температура',
#   'воздуха', 'была', '"', '+05', '"', 'градусов']


for n, v in enumerate(less_list):
    if x != n:
        continue
    if v[1:].isdigit() or v.isdigit():
        if v.isdigit():
            less_list[n] = f'{int(v):02d}'
        else:
            less_list[n] = f'{v[0]}{int(v[1:]):02d}'
        less_list.insert(n + 1, '"')
        less_list.insert(n, '"')
        x = x + 2
    x += 1
print(less_list)
print(" ".join(less_list))
