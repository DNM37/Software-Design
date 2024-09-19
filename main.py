from retail_store import RetailStore
from customer import Customer
from groceries import Apple, Orange
from tools import Hammer, Screwdriver

if __name__ == "__main__":
    store = RetailStore("Data Processing Support Store")
    
    # Define items for each customer
    alice_groceries = [Apple("Alice's Apple", 1.50, 100), Orange("Alice's Orange", 2.00, 80)]
    alice_tools = [Hammer("Alice's Hammer", 10.00), Screwdriver("Alice's Screwdriver", 5.00)]

    bob_groceries = [Apple("Bob's Apple", 1.20, 90), Orange("Bob's Orange", 2.50, 85)]
    bob_tools = [Hammer("Bob's Hammer", 12.00), Screwdriver("Bob's Screwdriver", 6.50)]

    charlie_groceries = [Apple("Charlie's Apple", 1.00, 95), Orange("Charlie's Orange", 2.25, 70)]
    charlie_tools = [Hammer("Charlie's Hammer", 9.50), Screwdriver("Charlie's Screwdriver", 5.75)]

    # Create customers with their predefined shopping lists
    customer1 = Customer("Alice", 100.0, store, alice_groceries, alice_tools)
    customer2 = Customer("Bob", 50.0, store, bob_groceries, bob_tools)
    customer3 = Customer("Charlie", 75.0, store, charlie_groceries, charlie_tools)

    # Add customers to the store
    store.add_customer(customer1)
    store.add_customer(customer2)
    store.add_customer(customer3)

    # Simulate shopping and checkout for each customer
    customer1.fill_cart()
    customer1.checkout()

    customer2.fill_cart()
    customer2.checkout()

    customer3.fill_cart()
    customer3.checkout()

    # Display the store statistics
    store.display_statistics()
