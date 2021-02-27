# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

avg_height = 0
#Write your code below this row 👇

for students in student_heights:
  avg_height += students
print("Total height: ", avg_height)

no_of_students = 0
for numbers in student_heights:
  no_of_students += 1
print("Total students: ", no_of_students)

avg = avg_height / no_of_students
print("avg height of students is ",avg)