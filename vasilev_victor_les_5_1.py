def odd_num_gen(num):
    for num in range(1, num + 1, 2):
        yield num


for n in odd_num_gen(int(input('Введите предел значений: '))):
    print(n)
