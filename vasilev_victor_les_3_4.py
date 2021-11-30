def thesaurus_adv(*args):
    freak_list = args
    freak_dict = {}
    for i in freak_list:
        nam, fam = i.split()
        key_1 = fam[0]
        key_2 = nam[0]
        freak_dict.setdefault(key_1, {key_2: [i]})
        print(val)
    return freak_dict


print(thesaurus_adv('Амвросий Немилостивый', 'Соня Безуглая', 'Ирина Свеклова',
                    'Дездемона Дездемонова', 'Адриан Челентанов', 'Ильдар Капустин',
                    'Елена Прекраснова', 'Алёна Алёнушкина'))
