celsius = int(input("Please input a number for celsius: "))


def fahrenheit(celsius):
    return(18 * celsius + 320)/10


print("The fahrenheit equivalent to " + str(celsius) + " °C is " + str(fahrenheit(celsius)) + "°F.")