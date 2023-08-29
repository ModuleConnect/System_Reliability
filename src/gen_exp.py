##TODO: Group the functions in a class
##TODO: Break the recursive_build function into smaller functions

#Get the next series module
def next_series_node(arr, mod):
        return [module for module in arr if module.left_node == mod.right_node][0]

#Return binary tree structure with a postfix traversal
def buildExpression(array: list, start_node, end_node):
    no_of_mode = 0
    parallel_block_no = 0
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
        nonlocal no_of_mode, parallel_block_no
        # Base case
        if node == end_node:
            return []

        
        # Recursive case
        parallel_modules = [module for module in array if module.left_node == node]
        print('parallel', parallel_modules)
        #When In Series
        if len(parallel_modules) == 1:
            mod = parallel_modules[0]
            array.remove(mod)
            no_of_mode += 1
            if array:
                if mod.right_node < end_node_parallel:
                    if no_of_mode == 1:
                        return [mod.name]  + recursive_build(mod.right_node, end_node_parallel) + ['*']
                    return [mod.name]  + ['*'] + recursive_build(mod.right_node, end_node_parallel) 
                elif mod.right_node == end_node_parallel:
                    return [mod.name] + ['*']
            else:
                if no_of_mode == 1:
                    return [mod.name] 
                return [mod.name]
        #When In Parallel
        elif len(parallel_modules) > 1:
            parallel_block_no += 1
            results = []
            end_node_parallel = get_end_node(parallel_modules)
            print('end_of_parallel', end_node_parallel)
            count = 1
            for mod in parallel_modules:
                array.remove(mod)
                no_of_mode += 1
                if mod.right_node < end_node_parallel:
                    paths = recursive_build(mod.right_node, end_node_parallel)
                    if count == 1:
                        results.extend([mod.name] + paths )
                    else:
                        results.extend([mod.name] + ['|'] + paths )
                elif mod.right_node == end_node_parallel:
                    if count == 1:
                        results.extend([mod.name])
                    else:
                        results.extend([mod.name] + ['|'])
                count += 1
                
            if parallel_block_no != 1:
                    print("Hellooo")
                    results.extend(['*'])
                # array.remove(mod)
                # no_of_mode += 1
            #Check if there are other modules after the end of parallel connection
            if end_node_parallel < end_node:
                remaining_modules = [module for module in array if end_node_parallel == module.left_node]
                paths = recursive_build(end_node_parallel, end_node)
                results.extend(paths)
                
                # if parallel_block_no != 1:
                #     print("Hellooo")
                #     results.extend(['*'])
                # for mod in remaining_modules:
                #     paths = recursive_build(mod.left_node, mod.right_node)
                #     results.extend([mod.name] + paths + ['*'])
            return results

        return []

    result = recursive_build(start_node, end_node)
    if not result:
        return "No valid path from start_node to end_node."
    return result

def is_operator(c):
    return c in {'*', '|'}

def postfix_to_infix(postfix_expr):
    stack = []
    for token in postfix_expr:
        # print(token)
        if not is_operator(token):  # Operand
            stack.append(token)
        elif is_operator(token):  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Adding parentheses to maintain operator precedence
            infix_expression = f"({operand1} {token} {operand2})"
            stack.append(infix_expression)
            print(stack)
            
    return stack[0]
  
#Convert the array of modules into dict
#{
#    'name':Mondule
#}          
def dictionarize(modules):
    new_dict = {}
    for module in modules:
        new_dict[module.name] = module
        
    return new_dict       
            