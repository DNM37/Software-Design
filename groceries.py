from abc import ABC, abstractmethod

# Grocery Interface
class GroceryIf(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

# Apple Class
class Apple(GroceryIf):
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is an apple. It has {self.calories} calories and costs ${self.cost:.2f}.")

# Orange Class
class Orange(GroceryIf):
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is an orange. It has {self.calories} calories and costs ${self.cost:.2f}.")
