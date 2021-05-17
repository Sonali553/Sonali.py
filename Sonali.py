# finding the area
import math
r=float(input("radius of the circle="))
area=math.pi*r*r
print(area)

#print extension of file

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])
