student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total = 0
for i in student_heights:
    total += i
avg_height = total//len(student_heights)
print(avg_height)