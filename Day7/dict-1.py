student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

#print(student["grades"]["history"])
#result=0
#for i in student:
result=student["grades"].get("history")

print(result)