# SYSTEM RELIABILTY

## Introduction

A Canonical System is system whose system is arranged either in *series* or *parallel* or both.

This program is designed to automatically calculate for the reliability of a given system.

The program takes input in the form of modules, where each module is represented by a value, a left node, a right node, and a reliabilty value. The left and right nodes signify the connections between modules, forming a directed graph. The goal is to find valid paths from the specified start node to the end node while handling parallel modules 


Constructs expressions from modules and their connections.

# Getting Started
In order to get started install the packages from the requirements.txt using 

    ```pip install -r requirements.txt```

    
cd into the gui directory in your terminal and run the ff to start the program;

```python app.py```   or   ```python -m app```   For windows
	
```python3 app.py```  or ```python3 -m app```- For Linux, MacOS


### For Simplicity, assuming a system contains to module say ```A``` and ```B```;

If the Modules are in ```Series```, the Reliability of the sytem will be expressed as

    R(sys) = A * B 
    where * denotes as the serires connection


If the Modules are in Parallel, the Reliability of the sytem will be expressed as

    R(sys) = A | B 
    where | denotes as the parallel connection

## Output
The output of the program is to provide the reliability of the system when given in the a netlist format of the your system as input.

## Sample Input
This input should be a text file of the following format:

    \START1 \END5
    -L_N1 -MModuleA -R0.99 -R_N2
    -L_N2 -MModuleB -R0.97 -R_N3
    -L_N2 -MModuleC -R0.98 -R_N3
    -L_N3 -MModuleD -R0.90 -R_N4
  

Each line represents a module with options -L_N for the left node, -M for the module value/name, -R for the relaibility value, and -R_N for the right node. ALso The Iinput needs to have a starting node and an ending node

The Expression shouuld be:

    ModuleA * (ModuleB | ModuleC) * ModuleD


