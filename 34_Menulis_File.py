"""users = open("users.txt", "r+")

print(users.readable())
print(users.writable())

users.close()"""

# jika pakai  mode w, jika file tidak ada maka akan dibuatkan filenya 
users = open("users.txt", "w")

users.write("Link - link")

users.close()