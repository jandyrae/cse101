def letter_grade(grade):
  if  grade >= 93:
    return "A"
  elif grade >= 90:
    return "A-"
  elif grade >= 87:
    return "B+"
  elif grade >= 83:
    return "B"
  elif grade >= 80:
    return "B-"
  elif grade >= 77:
    return "C+"
  elif grade >= 73:
    return "C"
  elif grade >= 70:
    return "C-"
  elif grade >= 67:
    return "D+"
  elif grade >= 63:
    return "D"
  elif grade >= 60:
    return "D-"
  else:
    return "F" 
 
math = int(input("Enter your score for Math Class here. (number between 1-100)")) 

english = int(input("Enter your score for English Class here. (number between 1-100)"))

pe = int(input("Enter your score for PE Class here. (number between 1-100)"))

science = int(input("Enter your score for Science Class here. (number between 1-100)"))

art = int(input("Enter your score for Art Class here. (number between 1-100)"))


print ("Your Math score is " + str(math) + ", your grade is " + letter_grade(math))
print ("Your English score is " + str(english) + ", your grade is " + letter_grade(english))
print ("Your PE score is " + str(pe) + ", your grade is " + letter_grade(pe))
print ("Your Science score is " + str(science) + ", your grade is " + letter_grade(science))
print ("Your Art score is " + str(art) + ", your grade is " + letter_grade(art))
