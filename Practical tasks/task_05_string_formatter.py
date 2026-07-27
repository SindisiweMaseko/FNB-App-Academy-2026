"""
task_05: 
Description: Processes a list of student dictionaries with marks for three subjects, 
             generates a grade and status for each student, produces a full class summary report, 
             and allows searching by student name.
"""

students = [
    {"name": "Alice", "maths": 85, "english": 78, "science": 92},
    {"name": "Bob", "maths": 60, "english": 65, "science": 55},
    {"name": "Charlie", "maths": 45, "english": 50, "science": 40},
    {"name": "Diana", "maths": 90, "english": 95, "science": 92},
    {"name": "Ethan", "maths": 70, "english": 72, "science": 68}
]

results = []
all_averages = []

for student in students:
    name = student["name"]
    maths = student["maths"]
    english = student["english"]
    science = student["science"]
    
    average = (maths + english + science) / 3
    all_averages.append(average)
    
    if average >= 75:
        grade = "A"
        status = "Distinction"
    elif average >= 60:
        grade = "B"
        status = "Pass"
    elif average >= 50:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"
        
    results.append({
        "name": name,
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

class_average = round(sum(all_averages) / len(all_averages), 2)
highest_mark = round(max(all_averages), 2)
lowest_mark = round(min(all_averages), 2)

print("\n--- Class Grade Report ---")
print(f"{'Name':<12} | {'Average':<8} | {'Grade':<6} | {'Status':<12}")
print("-" * 48)
for res in results:
    print(f"{res['name']:<12} | {res['average']:<8} | {res['grade']:<6} | {res['status']:<12}")

print("-" * 48)
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_mark}")
print(f"Lowest Average: {lowest_mark}")

while True:
    search_query = input("\nEnter student name to search (or type 'exit' to quit): ").strip()
    
    if search_query.lower() == "exit":
        print("Exiting search. Goodbye!")
        break
        
    found = False
    for res in results:
        if res["name"].lower() == search_query.lower():
            print(f"Found! Name: {res['name']} | Average: {res['average']} | Grade: {res['grade']} | Status: {res['status']}")
            found = True
            break
            
    if not found:
        print("Student not found.")