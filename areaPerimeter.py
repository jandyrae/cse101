import math

# TODO -> Add welcome function here
def displayWelcome():
  #name = raw_input("What is your name? ")
  print "Welcome to my area and perimeter calculator"
  print "=================================================="
print "=================================================="
# TODO -> Add circle area function here
def calcAreaCircle(radius):
  #radius = int(raw_input("What is the radius of the circle? "))
  area = radius ** 2 * 3.14159
  return area
# TODO -> Add circle perimeter function here
def calcPerimeterCircle(radius):
  #radius = int(raw_input("What is the radius of the circle? "))
  perimeter = 2 * 3.14159 * radius
  return perimeter
# TODO -> Add square area function here
def calcAreaSquare(side):
  #side = int(raw_input("What is the length of a side? "))
  area = side * side 
  return area
# TODO -> Add Square perimeter function here
def calcPerimeterSquare(side):
  #side = int(raw_input("What is the length of a side? ")) 
  perimeter = side * 4
  return perimeter
# TODO -> Add rectangle area function here
def calcAreaRect(width, height):
  #width = int(raw_input("What is the width of the rectangle? "))
  #height = int(raw_input("What is the height of the rectangle? "))
  area = width * height
  return area
# TODO -> Add rectangle perimeter function here
def calcPerimeterRect(width, height):
  #width = int(raw_input("What is the width of the rectangle? "))
  #height = int(raw_input("What is the height of the rectangle? "))
  perimeter = width * 2 + height * 2
  return perimeter
# TODO -> Add triangle area function here
def calcAreaTriangle(base, height):
  #base = int(raw_input("What is the base of the triangle? "))
  #height = int(raw_input("What is the height of the triangle? "))
  area = base * height / 2
  return area
# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))