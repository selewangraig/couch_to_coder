rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915},
]

#In a for loop print out each river's name!
print("River Names:")

for river in rivers:
    print(river["name"])

print("\n")

#In another loop, add up and print out the total length of all rivers!
total = 0

for river in rivers:
    total += river["length"]

print(f"The total length of the rivers is: {total}")
print("\n")

#Print out every river's name that begins with the letter "M"
print("River names starting with 'M':")

for river in rivers:
    if river["name"][0] == "M":
        print(river["name"])

print("\n")

#Print out the length of the rivers in Kilometers. They are in miles. 1 mile = 1.6km
print("River lengths in kilometers:")

for river in rivers:
    print(int(river["length"] * 1.6))