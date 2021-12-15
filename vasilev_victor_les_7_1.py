# import os
#
# folder_list = ['settings', 'mainapp', 'adminapp', 'authapp']
#
# if not os.path.exists('my_project'):
#     os.mkdir('my_project')
#
# for f in folder_list:
#     folder = os.path.join('my_project', f)
#     if not os.path.exists(folder):
#         os.mkdir(folder)

import os

folder_list = {'my_project': [{'settings': []},
                              {'mainapp': []},
                              {'adminapp': []},
                              {'authapp': []}]}

for key, value in folder_list.items():
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
