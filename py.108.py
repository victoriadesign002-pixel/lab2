kmh = float(input("Enter speed in km/h: "))
ms = float(input("Enter speed in m/s: "))

kmh_to_ms = kmh / 3.6

if kmh_to_ms > ms:
    print(kmh)
else:
    print(ms)
