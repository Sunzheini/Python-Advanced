

from os import listdir
from os.path import isdir, join


def directory_traversal(path, files_by_ext):
    for element in listdir(path):
        if isdir(join(path, element)):
            directory_traversal(join(path, element), files_by_ext)
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


result = {}
directory_traversal('./', result)

result = sorted(result.items(), key=lambda x: (x[0], x[1]))

new_dict = {}

for i in result:
    key = i[0]
    value = i[1]
    new_dict[key] = value

with open('./result.txt', 'w') as output_file:
    for ext, files in new_dict.items():
        output_file.write(ext + '\n')

        for file in files:
            output_file.write(f'- - - {file}\n')
