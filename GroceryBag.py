from abc import ABC, abstractmethod
import random
import string

class GroceryIf(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def display(self):
        pass

class Apple(GroceryIf):
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is an apple. It has {self.calories} calories and costs ${self.cost:.2f}.")

class Orange(GroceryIf):
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories
    
    def get_cost(self):
        return self.cost
    
    def display(self):
        print(f"{self.name} is an orange. It has {self.calories} calories and costs ${self.cost:.2f}.")

def generate_random_string(length):
    # Generate a random string of a given length
    letters = string.ascii_letters + string.digits  # Includes uppercase, lowercase letters, and digits
    return ''.join(random.choice(letters) for _ in range(length))

def create_grocery():
    select = random.choice([1, 2])
    name = generate_random_string(4)
    cost = round(random.uniform(1, 5), 2)
    calories = random.randrange(0, 100)
    
    if select == 1:
        return Apple(name, cost, calories)
    elif select == 2:
        return Orange(name, cost, calories)

class GroceryBag:
    def __init__(self, name):
        self.name = name
        self.total_cost = 0.0
        self.items = []
        self.num_items = 0
    
    def add_grocery(self, grocery):
        if self.num_items < 4:
            self.items.append(grocery)
            self.num_items += 1
            self.total_cost += grocery.get_cost()
            return True
        return False
    
    def display(self):
        print()
        print(f"{self.name} is a grocery bag with the following items:")
        for item in self.items:
            item.display()
        print(f"The total cost of these items is ${self.total_cost:.2f}\n")



def main():
    NUM_GROCERIES = random.randrange(1, 4)  # Generate between 1 and 3 groceries
    grocery_bag = GroceryBag("Data Processing Support")
    groceries = []
    
    for _ in range(NUM_GROCERIES):
        grocery = create_grocery()
        if grocery:
            ret = grocery_bag.add_grocery(grocery)
            if not ret:
                print("Unable to add the grocery!")
            else:
                groceries.append(grocery)

    grocery_bag.display()
    return grocery_bag  # Return the instance for access


if __name__ == "__main__":
    main()
