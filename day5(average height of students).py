# Input a Python list of student heights
student_heights = input("Enter student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#our code
total_height=0
for height in student_heights:
  total_height+=height
print(f"total height = {total_height}")
number_student=0
for student in student_heights:
  number_student+=1
print(f"number of students = {number_student}")


average_height=round(total_height/number_student)
print(f"average height = {average_height}")