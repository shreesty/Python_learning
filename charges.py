'''
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
'''
n=int(input("Enter the number of item they want to buy: "))
if(n<10):
    charges_per_item=12
    total_cost=charges_per_item * n
    print("Total no of items that you are buying is: ",n)
    print("Total_cost=",total_cost)
elif(n>=10 and n<99):
    charges_per_item=10
    total_cost=charges_per_item * n
    print("Total no of items that you are buying is: ",n)
    print("Total_cost=",total_cost)
elif(n>=100):
    charges_per_item=7   
    total_cost=charges_per_item * n
    print("Total no of items that you are buying is: ",n)
    print("Total_cost=",total_cost)


