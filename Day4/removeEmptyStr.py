str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str=[x for x in str_list if ""!=x or x==None]
print(new_str)