num_1 = float(input("Input first number: "))
num_2 = float(input("Input second number: "))
style = input("Choose type of operation:\nmultiplication (m)\ndivision(d)\naddition(a)\nsubtraction(s)\n")

if style == "d":
    print(num_1/num_2)
elif style == "m":
    print(num_1 * num_2)
elif style == "a":
    print(num_1 + num_2)
elif style == "s":
    print(num_1 - num_2)
else:
    print("You did not input the choice of operation correctly.")