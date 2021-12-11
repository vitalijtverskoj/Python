nginx_logs = open('nginx_logs.txt', 'r', encoding='utf-8')
content = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in nginx_logs)
for i in content:
    print(i)
nginx_logs.close()
