def thesaurus(*args):
    name_dict = {}
    name_list = sorted(args)
    print(name_list)
    for i in name_list:
        key = i[0]
        if key in name_dict:
            name_dict[key].append(i)
        else:
            name_dict[key] = [i]
    return name_dict


print(thesaurus('Амвросий', 'Соня', 'Ирина', 'Дездемона', 'Адриан',
                'Ильдар', 'Елена', 'Алёна', 'Алиса', 'Светлана', 'Даниил', 'Евгений', 'Феофан'))
