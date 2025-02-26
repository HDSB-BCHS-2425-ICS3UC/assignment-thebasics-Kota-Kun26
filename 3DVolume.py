#Kota Colley
#2025/02/25

#Cube

#This asks the user to input the lengths for the cube and calculates it
length=int(input("Please enter the length of one edge of your cube:"))
cube=length*length*length
#This tells the user the volume of the cube in units
print("The cube's volume is:", cube," units")

#Sphere

#This asks the user to input the radius for the sphere and calculates it
radius=int(input("Please enter the radius of your sphere:"))
sphere=4/3*3.1416*radius*radius*radius
#This tells the user the volume of the sphere in units
print("The sphere's volume is:", sphere, " units")

#Cone

#This asks the user to input the height and radius for the cone and calculates it
height=int(input("Please enter the height of your cone:"))
radius=int(input("Please enter the radius of your cone:"))
cone=1/3*3.1416*radius*radius*height
#This tells the user the volume of the sphere in units
print("The cone's volume is:", cone, "units")

#Cylinder

#This asks the user to input the height and radius for the cylinder and calculates it
height=int(input("Please enter the height of your cylinder:"))
radius=int(input("Please enter the radius of your cylinder:"))
cylinder=3.1416*radius*radius*height
#This tells the user the volume of the cylinder in units
print("The cylinder's volume is:", cylinder, "units")