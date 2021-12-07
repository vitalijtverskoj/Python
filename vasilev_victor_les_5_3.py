from itertools import islice

tutors = ['Иван', 'Анастасия', 'Пётр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tut_klass = ((tut, klas) for tut, klas in zip(tutors, klasses))

for n in tut_klass:
    print(n)

print(type(tut_klass))
print(list(islice(tut_klass, 1)))
