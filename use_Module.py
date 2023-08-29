from src.Module import Module
from src.gen_exp import *

A = Module('A', 1, 2, 0.9)

# print(A.get_failure)

ans = postfix_to_infix(['ModA', 'ModB', '*', 'ModC', '|', 'ModB', 'ModD', '|', 'ModE','*','*'])
print(ans)