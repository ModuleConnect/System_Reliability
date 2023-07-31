from gen_exp import *
from file_sys import *
from Module import Module

file_name = input("Enter you file name\n")
print(f"Your file name is {file_name}")

list_of_modules, nodes = read_modules_from_file(file_name)
dictionary = dictionarize(list_of_modules)
print("The following are the information retrieved form the file\n")
print(f"Start Node:{nodes[0]} and End Node:{nodes[1]}")

exp = buildExpression(list_of_modules, int(nodes[0]), int(nodes[1]), )
# print(exp)

final_exp = postfix_to_infix(exp)

print("The Expresion Of The New System:",final_exp)


res = eval(final_exp, dictionary)
print(res)

