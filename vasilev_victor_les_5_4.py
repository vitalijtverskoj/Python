scr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [v for i, v in enumerate(scr) if scr[i] > scr[i - 1] and i != 0]
print(result)
