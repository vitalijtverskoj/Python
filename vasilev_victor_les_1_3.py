
n = 1

while n <= 100:
    if n % 10 == 1 and n != 11:
        print(n, 'процент')
    elif (n % 10 == 2 and n != 12) or (n % 10 == 3 and n != 13) or (n % 10 == 4 and n != 14):
        print(n, 'процента')
    else:
        print(n, 'процентов')
    n += 1
