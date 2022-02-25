def halo_user(name, level):
    print(f"Halo {name} - {level}")
    print("Selamat belajar Python")

print("Start")
halo_user("BrotoFS", 10)
print("============")
halo_user("ZiZaZu", 10)
print("Finish")

print("Start")
#Keyword Argument
halo_user(level = 10, name = "BrotoFS")
print("============")
#Keyword Argument
halo_user(level = 10, name = "ZiZaZu")
print("Finish")

