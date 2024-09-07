
from abc import ABC, abstractmethod
import random
import string

class ToolIf(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

def generate_random_string(length):
    # Generate a random string of a given length
    letters = string.ascii_letters + string.digits  # Includes uppercase, lowercase letters, and digits
    return ''.join(random.choice(letters) for _ in range(length))


class Hammer(ToolIf):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is a hammer and costs ${self.cost:.2f}.")

class Screwdriver(ToolIf):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is a screwdriver and costs ${self.cost:.2f}.")

def create_tool():
    tool = None
    select = random.choice([1, 2])
    name = ""
    cost = 0
        
    if select == 1:
        name = generate_random_string(4)
        cost = round(random.uniform(5, 10), 2)
        tool = Hammer(name, cost)
    elif select == 2:
        name = generate_random_string(4)
        cost = round(random.uniform(5, 10), 2)
        tool = Screwdriver(name, cost)
    else:
        print("Invalid selection, try again!")
    
    return tool

class Toolbox:
    def __init__(self, name):
        self.name = name
        self.total_cost = 0.0
        self.items = []
        self.num_items = 0
    
    def add_tool(self, tool):
        if self.num_items < 4:
            self.items.append(tool)
            self.num_items += 1
            self.total_cost += tool.get_cost()
            return True
        return False
    
    def display(self):
        print()
        print(f"{self.name} is a toolbox with the following items:")
        for item in self.items:
            item.display()
        print(f"The total cost of these items is ${self.total_cost:.2f}\n")

def main():
    NUM_TOOLS = random.randrange(0, 3)
    toolbox = Toolbox("Data Processing Support")
    tools = []

    for _ in range(NUM_TOOLS):
        tool = create_tool()
        ret = toolbox.add_tool(tool)
        if not ret:
            print("Unable to add the tool!")
        else:
            tools.append(tool)

    toolbox.display()

    for tool in tools:
        tool = None

    return toolbox  # Return the Toolbox instance


if __name__ == "__main__":
    main()