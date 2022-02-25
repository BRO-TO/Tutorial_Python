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
#except ZeroDivisionError:
#    print("Erorr tidak bisa dibagi 0")
#except ValueError:
#asd    print("Yang dimasukkan bukan angka")
except:
    print("Terjadi kesalahan")


