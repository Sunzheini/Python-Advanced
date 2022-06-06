# Exercise: Error Handling

#built-in exceptions
# ----------------------------------------------------------
# 1
# numbers_dictionary = {}
#
# line = input()
# while line != "Search":
#     try:
#         number_as_string = line
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
#     line = input()
#
# line = input()
# while line != "Remove":
#     try:
#         searched = line
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# line = input()
# while line != "End":
#     try:
#         searched = line
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)

#custom exceptions
# ----------------------------------------------------------
# 2
# from lab.U03062022_custom_exceptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError
#
# valid_domains = {'.com', '.bg', '.org', '.net'}
#
# while 1:
#     line = input()
#     if line == 'End':
#         break
#
#     email = line
#
#     email_parts = email.split('@')
#
#     if len(email_parts) != 2:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     name, domain_name = email_parts
#
#     if len(name) <= 4:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     domain = f".{domain_name.split('.')[-1]}"        # !!!
#
#     if domain not in valid_domains:
#         raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")
#
# print("Email is valid")

# ----------------------------------------------------------










