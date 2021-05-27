name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if age >= 18 and age <= 31:
    print("You are welcome to go to the holiday, {0}.".format(name))
elif age <= 18:
    print("Come back in {0} years, {1}".format(18 - age, name))
else:
    print("Sorry you are {0} years too old, {1}.".format(age - 30, name))
