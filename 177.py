n = input("Enter number: ")
n = n.zfill(4)

digits = set(n)

print(len(digits) == 4)
