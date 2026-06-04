student = {
    "name" : "shubh" , 
    "age" : 25, 
    "city" : "dholpur"
}

print(student)
# student["grade"] = "a"
student.update({"grade": "A"})
student["marks"] = 89


print(student)
student.pop("city")
print(student)

if "salary" in student :
    print("key exists")
else:
    print("key does not exist")

#count number of keys 
print(len(student))
print(student.keys())
print(student.values)

d1 = {"a": 1, "b": 2} 
d2 = {"c": 3, "d": 4}

# d1.update(d2)
# print(d1)
d2.update(d1)
print(d2)

# find subjects with highest marks
marks = {"math":90, "science":85, "english" : 88}
max_marks = max(marks, key=marks.get)
print(max_marks)
