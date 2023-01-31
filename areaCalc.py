shape = input("What shape do you need calculated? (Enter R for Rectangle, T for Triangle, or C for Circle) ")

if shape == "C":
  radius = float(input("Enter the circle radius: "))
  Area = 3.14159 * radius ** 2
  print (Area)

elif shape == "T":
  base = float(input("Enter the triangle base: "))
  height = float(input("Enter the triangle height: "))
  area = .5 * base * height
  print (area)
  
elif shape == "R":
  base = float(input("Enter rectangle base: ")) 
  height = float(input("Enter rectangle height: ")) 
  Area = base * height
  print (Area)
  
else:
  print ("That doesn't look like a C, R, or a T! Maybe try uppercase. ")