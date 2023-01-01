'''
Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.
'''
import math

angle=float(input("Enter the angle in degree: "))  # converting angle in degree to radian

angle_in_radian= math.radians(angle)

sine=math.sin(angle_in_radian)   
print("The sine of", angle, "is: ",sine)