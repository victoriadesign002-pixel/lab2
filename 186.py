a, b, c = map(int, input("Enter three different integers: ").split())

numbers = [a, b, c]
numbers.sort()

product = numbers[0] * numbers[1]

print(product)
