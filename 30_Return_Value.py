"""
def halo_user(name, level):
    print(f"Halo {name} - {level}")
    print("Selamat belajar Python")
    return 100

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
print("============")

length = len([1,2,3])
print(length)
print("============")

temp = halo_user("BrotoFS", 10)
print(temp)
"""

# default nilai kembalian dari sebuah fungsi di python adalah "none"
def multiply(a,b):
    # result = a * b
    return a * b

result = multiply(2 ,10)
print(result)  # hasil yang diinginkan >> 2 * 10 = 20