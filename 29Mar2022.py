# alpha = 'abcdefghijklmnopqrstuvwxyz'
#
# string_input = input("Enter a string: ")
#
# string_length = len(string_input)
#
# string_output = ""
#
# for i in range(string_length):
#     character = string_input[i]
#     location_for_character = alpha.find(character)
#     new_location = location_for_character + 3
#     string_output += alpha[new_location]


# print(string_output)


import hashlib

# hash_object = hashlib.sha256(b'Derrick')
#
# hash_dig = hash_object.hexdigest()
#
# print(hash_dig)


#
# 1.Create your own version of a ceasar cypher to output
# any cryptographic code.

alpha = 'opqrstuvwxyzabcdefghijklmn'

user_input = input("Enter a string: ")
input_length = len(user_input)
string_result = ""

for i in range(input_length):
    character = user_input[i]
    location_for_character = alpha.find(character)
    print(f'{character} {location_for_character}')
    new_location = location_for_character + 3
    if new_location > len(alpha):
        new_location = new_location -len(alpha)
        string_result += alpha[new_location]
    else:
        string_result += alpha[new_location]


print(string_result)



# 2.Create a hash using sha512 algorithm to output a hexidecimal hash.
