from abc import ABC, abstractmethod

# Tool Interface
class ToolIf(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

# Hammer Class
class Hammer(ToolIf):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is a hammer and costs ${self.cost:.2f}.")

# Screwdriver Class
class Screwdriver(ToolIf):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is a screwdriver and costs ${self.cost:.2f}.")
