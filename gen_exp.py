from Module import Module

def next_series_node(arr, mod):
        return [module for module in arr if module.left_node == mod.right_node][0]
def buildExpression(array: list, start_node, end_node):
    no_of_mode = 0
    # def get_end_node(parallel_modules):# TODO: wrong algorithm, Needs to br fixed
    #     return max([mod.right_node for mod in parallel_modules])
    
    
    def get_end_node(parallel):
        end_node = parallel[0].right_node
        for index in range(len(parallel)-1):
            mod1 = parallel[index]
            mod2 = parallel[index+ 1]
            while(mod1.right_node != mod2.right_node):
                if mod1.right_node < mod2.right_node:
                    end_node = mod2.right_node
                    mod1 = next_series_node(array, mod1)
                elif mod1.right_node > mod2.right_node:
                    end_node = mod1.right_node
                    mod2 = next_series_node(array, mod2)
        return end_node

    def recursive_build(node, end_node_parallel):
        nonlocal no_of_mode 
        # Base case
        if node == end_node:
            return []# [array[node - 1].name] if 0 < node <= len(array) else [] # Subtract 1 as the node index starts from 1

        
        # Recursive case
        parallel_modules = [module for module in array if module.left_node == node]
        if len(parallel_modules) == 1:
            mod = parallel_modules[0]
            array.remove(mod)
            no_of_mode += 1
            # print(mod, 'ser')
            if array:
                if mod.right_node < end_node_parallel:
                    return [mod.name]  + recursive_build(mod.right_node, end_node_parallel) + ['*']
                elif mod.right_node == end_node_parallel:
                    return [mod.name] + ['*']
            else:
                if no_of_mode == 1:
                    return [mod.name] 
                return [mod.name]+ ['*']
        elif len(parallel_modules) > 1:
            results = []
            end_node_parallel = get_end_node(parallel_modules)
            # print(end_node_parallel)
            count = 1
            for mod in parallel_modules:
                # print(mod, "p")
                # print(f"{mod.right_node} {end_node_parallel}")
                if mod.right_node < end_node_parallel:
                    paths = recursive_build(mod.right_node, end_node_parallel)
                    # print(paths)
                    if count == 1:
                        results.extend([mod.name] + paths )
                    else:
                        results.extend([mod.name] + ['|'] + paths )
                elif mod.right_node == end_node_parallel:
                    # print(paths)
                    if count == 1:
                        results.extend([mod.name])
                    else:
                        results.extend([mod.name] + ['|'])
                count += 1
                array.remove(mod)
                no_of_mode += 1
            # print('res',results)
            # print(end_node_parallel, 'endpara')
            if end_node_parallel < end_node:
                # print(array, 'after arr')
                remaining_modules = [module for module in array if end_node_parallel == module.left_node]
                # print("rem",remaining_modules)
                # print(end_node, 'end')
                paths = recursive_build(end_node_parallel, end_node)
                # print(paths, 'after')
                results.extend(paths)
                # for mod in remaining_modules:
                #     paths = recursive_build(mod.left_node, mod.right_node)
                #     results.extend([mod.name] + paths + ['*'])
            return results

        return []

    result = recursive_build(start_node, end_node)
    if not result:
        return "No valid path from start_node to end_node."
    return result

# Test with no valid path from start_node to end_node
# text_inp = [
#     Module('A', 1, 2, 0.99), 
#     Module('B', 2, 3, 0.99),
#     Module('C', 3, 5, 0.99), 
#     Module('D', 2, 4, 0.99),
#     Module('E', 4, 5, 0.99)
#     ]
# start_node = 1
# end_node = 5
# result = buildExpression(text_inp, start_node, end_node)
# print(result)


def is_operator(c):
    return c in {'*', '|'}

def postfix_to_infix(postfix_expr):
    stack = []
    for token in postfix_expr:
        if not is_operator(token):  # Operand
            stack.append(token)
        elif is_operator(token):  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Adding parentheses to maintain operator precedence
            infix_expression = f"({operand1} {token} {operand2})"
            stack.append(infix_expression)
            
    return stack[0]
            
def dictionarize(modules):
    new_dict = {}
    # print(modules)
    for module in modules:
        # print('module')
        # print(module)
        new_dict[module.name] = module
        
    return new_dict       
            
# exp = ['a', 'b', 'A', '*', '|']

# ans = postfix_to_infix(exp)
# modules = [
#     Module('A', 1, 2, 0.9),
#     Module('B', 2, 3, 0.9),
#     Module('C', 3, 4, 0.9)
    #  Module('D', 4, 5, 0.9)
# ]

# exp = buildExpression(modules, 1, 4)
# print(exp)