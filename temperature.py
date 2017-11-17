def convert_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convert_celsius(fahrenheit):
    return (fahrenheit - 32) * 5  / 9
         

new_temp1 = convert_celsius(72)
new_temp2 = convert_fahrenheit(37)

print(f"72 degrees F = {new_temp1} degrees C")
print(f"37 degrees C = {new_temp2} degrees F")

#Another way to print

print("72 degrees F = {} degrees C".format(new_temp1))
print("37 degrees C= {} degrees F".format(new_temp2))
