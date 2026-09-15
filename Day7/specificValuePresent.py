roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
value=[x for x in roles.values()]
print("manager" in value)
print("editor" in value)