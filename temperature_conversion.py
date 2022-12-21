'''
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in.
Your program should convert the temperature to the other unit. The conversions are:
F= (9/5)* C + 32 and C=(5/9)*(F-32)

'''
temperature= float(input("Enter a temperature: "))
unit=input("Enter unites: ")

if (unit=="C"):
    C=temperature
    F=(9/5)* C + 32
    print("Temperature in Fahrenheit is: ",F)
else:
    F=temperature
    C=(5/9)*(F-32)
    print("Temperature in Celsius is: ",C)
