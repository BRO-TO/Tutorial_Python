import random 

#print(random.randint(10, 30))

#for index in range(5):
#   print(random.randint(10, 30))

users = ['Broto', 'Jarpa', 'Cinoy', 'Tancekure', 'Marmar']

# batas_bawah = 0
# batas_atas = len(users) - 1

# # for i in range(5):
# #     random_int = random.randint(batas_bawah, batas_atas)
# #     print(random_int)

# random_int = random.randint(batas_bawah, batas_atas)

# winner = users[random_int]

# print(winner)

winner = random.choice(users)
print(winner)