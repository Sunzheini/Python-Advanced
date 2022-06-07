# File Handling

#--------------------------------------------------------------
# from io import open
#
#
# def give_contents(file_path):
#     print(f'Opening: "{file_path}"...')
#     file = open(file_path)
#     print(file.read())      # printira sydyrjanieto

# relativen pyt, based on the location of the current file,
# ./ e tekushta direktoriq
#give_contents('./demo.txt')

# ../ e parent direktoriq
#give_contents('../another_demo.txt')


#absolute - based on os file location
#give_contents('D:\Study\Projects\PycharmProjects\Python-Advanced\lab\demo.txt')


# path separator
# windows - D:\\repos\\python-advanced
# linux - /repos/python-advanced

#print(os.sep) # za windows e \

#--------------------------------------------------------------
# opening files errors

# try:
#     open('./demo.txt')          # otvarq fail no ne i direktoriq
#     print('File is found!')
# except FileNotFoundError:       # i pri greshni direktorii
#     print('Not found!')

#--------------------------------------------------------------
# file modes - default e rt

# kakvo shte pravim
# r - read only
# w - open for writing truncating the file first
# x = create a new file and open it for writing
# a - append

# pod kakva forma
# t - text mode
# b - binary mode

print(open('demo.txt', 'rt').read())
# normalno - kato text

print(open('demo.txt', 'rb').read())
# b'I am Daniel\r\nYou are Maimuna\r\nAnd you are Maxi'

# 1:58:48









