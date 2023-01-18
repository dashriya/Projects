width = int(input("Choose the width of the rectangular prism: "))
length = int(input("Choose the length of the rectangular prism: "))
height = int(input("Choose the height of the rectangular prism: "))


def prism(l, w, h):
   return l * w * h


print("The volume of the rectangular prism is " + str(prism(length, width, height)) + " cubic feet.")