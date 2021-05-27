
number = input("Please enter a series of number, using any separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

#print(separators)

