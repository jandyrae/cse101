
print (" ")
print ("Letter Grade Checker")
print ("********************")
print ("Check your average letter grade here, just follow the prompts.")

total = 0
for i in range(5):
  score = int(input("What was your score? "))
  total = total + score
  avg = total / 5

def letter_grade(grade):
  if grade >= 93:
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
print ("For a average score of " + str(avg) + ", your letter grade is " + letter_grade(avg))
