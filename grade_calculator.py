print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = maths + science + english

print("Total Marks =", total)

percentage = total / 3

print(f"Percentage = {percentage:.2f}")
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n====================")
print("     RESULT")
print("====================")
print("Student Name =", name)
print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("====================")