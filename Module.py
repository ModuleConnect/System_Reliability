import math

class Module:
    def __init__(self, name: str, left_node: int, right_node: int, rel: float):
        self.name = name
        self.left_node = left_node
        self.right_node = right_node
        self.rel = rel
        
    @property
    def get_failure(self):
        return (1 - self.rel)
    
    def __mul__(self, other):
        new_rel = self.rel * other.rel
        return Module("New_System", self.left_node, other.right_node, new_rel)
    def __or__(self, other):
        new_rel = 1 - (other.failure * self.failure)
        return Module('New_System',self.left_node, self. right_node, new_rel)
    def __repr__(self) -> str:
        return ( "\n{} has a reliability of {:5f}".format(self.name, self.rel))
    
    