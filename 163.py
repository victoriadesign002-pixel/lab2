room_type = input("Enter room type: ")

if room_type == "triangle":
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5

elif room_type == "rectangle":
    a = float(input())
    b = float(input())

    area = a * b

elif room_type == "circle":
    r = float(input())

    area = 3.14 * r ** 2

print(area)
