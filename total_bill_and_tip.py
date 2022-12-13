
'''
A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
'''

price=int(input("Enter the price of the meal: "))
print("Total amount is ",price)
percent_tip= float(input("Enter the price of the meal: "))

tip_amt= (percent_tip * price)/100
print("Tip amount is: ",tip_amt)

amount_after_tip = price - tip_amt
print("Amount_after_tip: ",amount_after_tip)

