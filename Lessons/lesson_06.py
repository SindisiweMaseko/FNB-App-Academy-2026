"""
lesson_06
Description: This lesson covers the basics of lists and dictionaries in Python. It demonstrates how to create, modify, and access elements in these data structures.
"""

# working list

cart = ["Apples", "Eggs", "Milk"]
print(cart[0])

cart.append("Bread")
print(cart)

for item in cart:
    print(item)


print("-" * 80)

# working with dictionaries

student = {
    "name" : "Sindisiwe",
    "age" : 21,
    "course" : "Python Programming"
}

print(student["name"])
print(student["age"])
print(student["course"])