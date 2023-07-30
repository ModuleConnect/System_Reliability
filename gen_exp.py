import Module
def buildExpression(array: list, start_node, end_node):
    def get_end_node(parallel_modules):
        return max([mod.right_node for mod in parallel_modules])

    def recursive_build(node, end_node_parallel):
        # Base case
        if node == end_node:
            return [array[node - 1].value] if 0 < node <= len(array) else [] # Subtract 1 as the node index starts from 1

        
        # Recursive case
        parallel_modules = [module for module in array if module.left_node == node]
        if len(parallel_modules) == 1:
            mod = parallel_modules[0]
            array.remove(mod)
            if array:
                if mod.right_node <= end_node_parallel:
                    return [mod.value]  + recursive_build(mod.right_node, end_node_parallel) + ['*']
        elif len(parallel_modules) > 1:
            results = []
            end_node_parallel = get_end_node(parallel_modules)
            print(end_node_parallel)
            count = 1
            for mod in parallel_modules:
                if mod.right_node <= end_node_parallel:
                    paths = recursive_build(mod.right_node, end_node_parallel)
                    if count == 1:
                        results.extend([mod.value] + paths )
                    else:
                        results.extend([mod.value] + ['|'] + paths )
                count += 1
            results
            remaining_modules = [module for module in array if end_node_parallel < module.left_node <= end_node]
            for mod in remaining_modules:
                paths = recursive_build(mod.left_node, mod.right_node)
                results.extend([mod.value] + paths + ['*'])
            return results

        return []

    result = recursive_build(start_node, end_node)
    if not result:
        return "No valid path from start_node to end_node."
    return result

# # Test with no valid path from start_node to end_node
# text_inp = [Module('A', 1, 2), Module('B', 2, 3), Module('C', 2, 3), Module('E', 3, 4), Module('E', 4, 5)]
# start_node = 1
# end_node = 5
# result = buildExpression(text_inp, start_node, end_node)
# print(result)


def is_operator(c):
    return c in {'*', '|'}

def postfix_to_infix(postfix_expr):
    stack = []
    for token in postfix_expr:
        if token.isalpha():  # Operand
            stack.append(token)
        elif is_operator(token):  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Adding parentheses to maintain operator precedence
            infix_expression = f"({operand1} {token} {operand2})"
            stack.append(infix_expression)
            
    return stack[0]
            
            
            
exp = ['a', 'b', 'A', '*', '|']

ans = postfix_to_infix(exp)

print(ans)