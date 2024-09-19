class RetailStore:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.total_grocery_revenue = 0.0
        self.total_tool_revenue = 0.0
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def add_revenue(self, grocery_cost, tool_cost):
        self.total_grocery_revenue += grocery_cost
        self.total_tool_revenue += tool_cost
    
    def display_statistics(self):
        total_revenue = self.total_grocery_revenue + self.total_tool_revenue
        avg_spend = total_revenue / len(self.customers) if self.customers else 0
        
        print(f"\nRetail Store: {self.name} Statistics")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Average Spend per Customer: ${avg_spend:.2f}")
        
        if total_revenue > 0:
            grocery_percentage = (self.total_grocery_revenue / total_revenue) * 100
            tool_percentage = (self.total_tool_revenue / total_revenue) * 100
            print(f"Percentage spent on Groceries: {grocery_percentage:.2f}%")
            print(f"Percentage spent on Tools: {tool_percentage:.2f}%")
