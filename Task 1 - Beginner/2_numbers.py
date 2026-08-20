# Task 2: Numbers

# 1. Format function
def format_number(number, representation):
    return format(number, representation)

result = format_number(145, 'o')

print("Formatted number:", result)
print("Representation used: Octal")


# 2. Area of circular pond
radius = 84
pi = 3.14

area = pi * radius ** 2

print("Area of the pond:", area)


# Bonus: Amount of water
water_per_square_meter = 1.4

water = area * water_per_square_meter

print("Total water:", int(water), "liters")


# 3. Speed
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed:", int(speed), "meters per second")
