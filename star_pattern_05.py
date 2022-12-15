
'''
Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

       *
     * * *
   * * * * *
 * * * * * * *
   * * * * *
     * * *
       *

'''
star="* "
space=" "
for i in range(1,8,2):
    print(space*(7-i)+star*i)

for i in range(5,0,-2):
    print(space*(7-i)+star*i)


