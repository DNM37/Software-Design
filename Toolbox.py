from tools import ToolIf

class Toolbox:
    def __init__(self, name):
        self.name = name
        self.total_cost = 0.0
        self.items = []
        self.num_items = 0
    
    def add_tool(self, tool: ToolIf):
        if self.num_items < 4:
            self.items.append(tool)
            self.num_items += 1
            self.total_cost += tool.get_cost()
            return True
        return False
    
    def display(self):
        print(f"\n{self.name} is a toolbox with the following items:")
        for item in self.items:
            item.display()
        print(f"The total cost of these items is ${self.total_cost:.2f}\n")
