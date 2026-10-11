a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
s = int(input("Enter s: "))

if s <= a:
    tax = 0
elif s <= b:
    tax = s * 0.10
elif s <= c:
    tax = s * 0.25
else:
    tax = s * 0.50

print(tax)
