numbers = [1, 45, 32, 12, 60]

for i in numbers:
    if i %  8 == 0:
        #reject thelist
        print("The numbers are unacceptable")
        break
    else:
        print("All those numbers are fine")