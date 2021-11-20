
duration = int(input("Введите продолжительность в секундах: "))
seconds = 0
minutes = 0  # 60 сек в минуте
hours = 0  # 3600 сек в часе
days = 0  # 86400 сек в дне

if duration >= 86400:
    days = duration // 86400
    duration = duration % 86400

if duration >= 3600:
    hours = duration // 3600
    duration = duration % 3600

if duration >= 60:
    minutes = duration // 60
    duration = duration % 60

if 0 < duration < 60:
    seconds = duration

print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
