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

    -n1 -mModuleA -r0.99 -n2
    -n2 -mModuleB -r0.97 -n3
    -n2 -mModuleC -r0.98 -n3
    -n3 -mModuleD -r0.90 -n4
  

Each line represents a module with options -n for the left node, -m for the module value, -r for the relaibility value, and -n for the right node

The Expression shouuld be:

    ModuleA * (ModuleB | ModuleC) * ModuleD


