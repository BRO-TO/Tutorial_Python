import csv

#users = open("users.csv", "r")

with open("users.csv", "r") as users:
    users_csv = csv.reader(users, delimiter=",")

#print(users_csv)

    for row in users_csv:
    #print(row)
        print(f"Name : {row[0]}. Username : {row[1]}. Role : {row[-1]}")

