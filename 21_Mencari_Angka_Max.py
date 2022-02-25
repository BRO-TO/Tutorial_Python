numbers = [5,6,7,8,1]

total = sum(numbers)
print(total)

maxNum = max(numbers)
print(maxNum)

numbers.sort()
max_num = numbers[-1]
print(max_num)

maxi = numbers[0]
for number in numbers:
    if number > maxi:
        maxi = number

print(maxi)
