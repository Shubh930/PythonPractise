# 2 built in methods of tuple


# 1 > count() method
numbers = (1, 2, 3, 2, 2, 5)
print(numbers.count(2))

# 2 > index() method
fruits = ("apple", "banana", "mango")
print(fruits.index("banana")) 

# These are not tuple methods, but they are commonly used with tuples.
t = (10, 20, 30)
print(len(t))

t = (5, 9, 2, 7)
print(max(t))
print(min(t))

t = (1, 2, 3, 4)
print(sum(t))

marks = (85, 90, 85, 70, 85)
print("Count of 85:", marks.count(85))
print("Index of 70:", marks.index(70))

# important methods of tuple
#  concatenation(+)
t1 = (1, 2, 3)
t2 = (4, 5)

result = t1 + t2

print(result)

# Repetition(*)
t = ("Python",)

print(t * 3)

# Membership Operators (in, not in)
t = (10, 20, 30)

print(20 in t)
print(50 not in t)

# Tuple Slicing
t = (0, 1, 2, 3, 4, 5)

print(t[1:4])

# Nested Tuples
t = ((1, 2), (3, 4))

print(t[1])
print(t[1][0])

# sorted() Function
t = (4, 1, 3, 2)

print(sorted(t))

# tuple() Constructor
lst = [1, 2, 3]

t = tuple(lst)

print(t) # list gets change here into tuple


# Packing and Unpacking
t = (10, 20, 30)

a, b, c = t

print(a)
print(b)
print(c)

# Iterating Through Tuple
t = ("a", "b", "c")

for i in t:
    print(i)

#Comparing Tuples 
t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(t1 < t2)