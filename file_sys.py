from Module import Module


def read_modules_from_file(file_path): 
    """
    A function to read netlist format from file
    """
    modules = []
    start_node = None
    end_node = None
    with open(file_path, 'r') as file:
        for line in file:
            try:
                if line.startswith('\\'):
                    start_node, end_node = get_start_and_end_nodes(line)
                module = parse_line_to_module(line)
                modules.append(module)
            except ValueError as e:
                print(f"Error parsing line: '{line.strip()}'. {e}")
                
    return modules [start_node, end_node]


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
        
            
                
    return Module(value, left_node, right_node, rel)

                
def get_start_and_end_nodes(line):
    parts = line.strip()
    if parts.startswith('\\'):
        if "\START" in parts:
            start_node = parts[6:]
        elif "\END" in parts:
            end_node = parts[4:]
            
    return start_node, end_node
    