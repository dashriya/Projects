num = int(input("Number: "))

tog = num
summed = 0

while num > 0:
    print(num)
    summed += num
    num -= 1

print(summed)