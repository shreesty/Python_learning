

'''
Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown
below:

0 --- 0.0---1.0
15 --- 0.2588--- 0.9659
30 --- 0.5--- 0.866
...
345 --- -0.2588--- 0.9659
'''

import math

for i in range(0,346,15):
    angle_in_degree=math.radians(i)
    sine=math.sin(angle_in_degree)
    cosine=math.cos(angle_in_degree)
    print(i,round(sine,4),round(cosine,4),sep="---")
    



