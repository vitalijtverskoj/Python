
cub_list = []
all_sum_1 = 0
all_sum_2 = 0

for i in range(1, 1000):
    if i % 2 != 0:
        cub_list.append(i**3)


for n in cub_list:
    pop = n
    pip = 0
    sum_num = 0
    while pop != 0:
        pip = pop % 10
        pop = pop // 10
        sum_num = sum_num + pip
    if sum_num % 7 == 0:
        all_sum_1 += n

print(all_sum_1)

for i, pr in enumerate(cub_list):
    cub_list[i] += 17

for n in cub_list:
    pop = n
    pip = 0
    sum_num = 0
    while pop != 0:
        pip = pop % 10
        pop = pop // 10
        sum_num = sum_num + pip
    if sum_num % 7 == 0:
        all_sum_2 += n

print(all_sum_2)
