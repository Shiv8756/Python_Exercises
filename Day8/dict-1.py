user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
extractValue=["id", "username", "email"]
d={}
for i in extractValue:
    val=user.get(i)
    d[i]=val

print(d)
