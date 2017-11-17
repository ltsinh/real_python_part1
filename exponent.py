input_1 = float(input("Enter a base: "))
input_2 = float(input("Enter a exponent: "))
power_1 = float(input_1 ** input_2)
power_2 = round(power_1, 3)

print(f"Print version 1: {input_1} to the power of {input_2} = {power_2}")
print("Print version 2: {} to the power of {} = {}".format(input_1, input_2, power_2))
