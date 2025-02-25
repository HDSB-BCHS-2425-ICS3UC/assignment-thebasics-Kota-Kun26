#Kota
#2025/02/25

#A simple introduction/instructions for the user
print("To calculate a discriminant, please enter three numbers. :>")

#This is fetching the number for A
a=int(input("Enter number A then press enter:"))
print ("Value A is:")
print(a)
#This is fetching the number for B
b=int(input("Enter number B then press enter:"))
print ("Value B is:")
print(b)
#This is fetching the number for C
c=int(input("Enter number C then press enter:"))
print ("Value c is:")
print(c)

#This calculates the discriminant from the values that the user inputs
exponent=b**2
product= 4*a*c
delta=exponent-product
#This tells the user what the discriminant of the values they entered is by printing it to the screen
print("The discriminant is:")
print(int(delta))