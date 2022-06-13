

from os.path import exists
from os import remove

while 1:
    line = input()
    if line == 'End':
        break

    explode = line.split('-')
    command, file_name = explode[0], explode[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass

    elif command == 'Add':
        content = explode[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        if not exists(f'./{file_name}'):
            print("An error occurred.")
            continue

        old_string, new_string = explode[2], explode[3]
        with open(f'./{file_name}', 'r+') as file:
            file_content = file.read().replace(old_string, new_string)

            file.seek(0)
            file.truncate(0)
            file.write(file_content)

    else:
        if not exists(f'./{file_name}'):
            print("An error occurred.")
            continue

        remove(f'./{file_name}')
