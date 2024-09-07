import GroceryBag
import Toolbox

def testCart():
    grocery_total = 0
    tool_total = 0
    for i in range(3):
        grocery_bag = GroceryBag.main()  # Get the GroceryBag instance
        toolbox = Toolbox.main()  # Assuming Toolbox.main() does something else you need
        grocery_total += grocery_bag.total_cost
        tool_total += toolbox.total_cost

    
    averagespend = grocery_total/3
    total_revenue = grocery_total + tool_total
    percent_tools = (tool_total/total_revenue) * 100
    percent_groceries = (grocery_total/total_revenue) * 100

    print ("the average spend is $" + str(round(averagespend, 3)))
    print ("the total revenue is $" + str(round(total_revenue, 3)))
    print("Tools make up " + str(round(percent_tools,1)) + "% of the revenue")
    print("Groceries make up " + str(round(percent_groceries,1)) + "% of the revenue")

testCart()
