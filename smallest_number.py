smallest = None
print("Before")
for value in [10, 15, 25, 5, 20]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)