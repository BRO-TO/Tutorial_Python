user = {
    "name" : "BrotoFS",
    "age" : 30,
    "is_admin" : True
} 

name = user["name"]

print("")
print(name)

age = user["age"]

print("")
print(age)

temp = user.get("username")

print("")
print(temp)

temp = user.get("username", "BROTOFS")

print("")
print(temp)

# Tambah value
user["hobby"] = "coding"
print(user)

# Ubah value
user["name"] = "BFS"
print(user)
