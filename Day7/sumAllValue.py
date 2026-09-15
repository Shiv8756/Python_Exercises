# expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
# val=[x for x in expenses.values()]
# sum=0
# for i in val:
#     sum=sum+i
# print(sum)

emp={"emp1":{"salary":200,
             "name":"shivam"},
     "emp2":{"salary":250,
             "name":"gaurav"}}

#print(emp["emp1"].get("salary"))

for i in emp:
#    for j in emp[i]:
    print(emp[i].get("salary"))
