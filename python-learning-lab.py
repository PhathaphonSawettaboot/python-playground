student = {
    "name" : "John",
    "age" : 25,
    "major" : "Computer Science"
}

print(student["name"])
print(student["age"])

student["age"] = 26
print(student["age"])

student["gpa"] = 3.5
del student["major"]
print(student)

print("gpa" in student)
print("major" in student)

keys = student.keys()
values = student.values()
print(keys)
print(values)

for key, value in student.items():
    print(key, ":" , value)