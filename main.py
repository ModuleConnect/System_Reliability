from gen_exp import *
from file_sys import *
from Module import Module

file_name = input("Enter you file name\n")
print(f"Your file name is {file_name}")

list_of_Modules, nodes = read_modules_from_file(file_name)
print(list_of_Modules)
print(f"Start Node:{nodes[0]} and End Node:{nodes[1]}")

exp = buildExpression(list_of_Modules, nodes[0], nodes[1], )
print(exp)