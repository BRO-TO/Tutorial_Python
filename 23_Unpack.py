numbers = (1,2,3)

# x = numbers[0]
# y = numbers[1]
# z = numbers[2]

# Unpack

x,y,z = numbers

print(z)

x, *a = numbers
print(a)