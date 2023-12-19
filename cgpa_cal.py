# A cgpa calclator
# Parameters required = Number of Total units, grade and unit of each course. 
# False code """ request for sum of total units. calculate points gotten in each course, divide by total unit.


U = int(input("input the total number of units offered: "))
grade_value = {"A":5,"B":4,'C':3,"D":2,"E":1,"F":0}

sum = 0
while True:
   user_input = input("input grade and course unit like so eg. A,3 :")
   if user_input == "stop":
      print("your final cgpa is ", current_cgpa)
      break
   else:
      grade, unit = user_input.split(",")
      grade_point = grade_value[grade]
      point = int(grade_point)*int(unit)
      sum+=point
      current_cgpa =sum/U
      print ("your current cgpa is ",current_cgpa )

