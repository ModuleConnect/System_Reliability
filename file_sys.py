from Module import Module


def read_modules_from_file(file_path): 
    """
    A function to read netlist format from file
    """
    modules = []
    S_node = None
    E_node = None
    with open(file_path, 'r') as file:
        for line in file:
            try:
                if line.startswith('\\'):
                    S_node, E_node = get_start_and_end_nodes(line)
                else:
                    module = parse_line_to_module(line)
                    modules.append(module)
            except ValueError as e:
                print(f"Error parsing line: '{line.strip()}'. {e}")
                
    return modules, [S_node, E_node]


def parse_line_to_module(line: str):
    """_summary_
    Partition the line to retreive attributes of each module 
    Args:
        line (_type_): _description_
        

    Returns:
        _type_: _description_
        returns an instance of Module with the given attributes
    """
    parts = line.strip().split()
    value = None
    left_node = None
    right_node = None
    rel = None
    
    
    for i in range(len(parts)):
        if parts[i].startswith('-'):
            if "-L_N" in parts[i]:
                left_node = parts[i][4:]
            elif "-R_N" in parts[i]:
                right_node = parts[i][4:]
            elif "-M" in parts[i]:
                value = parts[i][2:]
            elif "-R" in parts[i]:
                rel = parts[i][2:]
        
    print(f"lnode:{left_node} rnode:{right_node} value:{value} rel:{rel}")
                
    return Module(str(value), int(left_node), int(right_node), float(rel))

                
def get_start_and_end_nodes(line):
    start_node = None
    end_node = None
    parts = line.strip().split()
    for i in range(len(parts)):
        if parts[i].startswith('\\'):
            if "\START" in parts[i]:
                start_node = parts[i][6:]
            elif "\END" in parts[i]:
                end_node = parts[i][4:]
            
    return start_node, end_node
    
    
# ans = parse_line_to_module("\END4")
# L, S = get_start_and_end_nodes("\END4")
# print(L,S)