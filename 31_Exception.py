"""
level = input("Level kamu : ")
level = int(level)
print(level)
"""

try:
    level = input("Level kamu : ")
    level = int(level)
    level = level / 0
    print(level)
except ZeroDivisionError:
    print("Erorr tidak bisa dibagi 0")
except ValueError:
    print("Yang dimasukkan bukan angka")


