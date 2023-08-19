# SYSTEM RELIABILTY

## Introduction

A Canonical System is system whose system is arranged either in *series* or *parallel* or both.

This program is designed to automatically calculate for the reliability of a given system.

The program takes input in the form of modules, where each module is represented by a value, a left node, a right node, and a reliabilty value. The left and right nodes signify the connections between modules, forming a directed graph. The goal is to find valid paths from the specified start node to the end node while handling parallel modules 


Constructs expressions from modules and their connections.

## Output
The output of the program is to provide the reliability of the system given in the a netlist format.

### For Simplicity, assuming a system contains to module say ```A``` and ```B```;

If the Modules are in ```Series```, the Reliability of the sytem will be expressed as

    R(sys) = A * B 
    where * denotes as the serires connection


If the Modules are in Parallel, the Reliability of the sytem will be expressed as

    R(sys) = A | B 
    where | denotes as the parallel connection


## Sample Input
This input should be a text file of the following format:

    \START1 \END5
    -L_n1 -MModuleA -R0.99 -RN2
    -L_n2 -MModuleB -R0.97 -RN3
    -L_n2 -MModuleC -R0.98 -RN3
    -L_n3 -MModuleD -R0.90 -RN4
  

Each line represents a module with options -L_N for the left node, -M for the module value/name, -R for the relaibility value, and -R_N for the right node. ALso The Iinput needs to have a starting node and an ending node

The Expression shouuld be:

    ModuleA * (ModuleB | ModuleC) * ModuleD


