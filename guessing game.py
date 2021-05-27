import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

highest = 1000
answer = random.randint(1, highest)
print("Please guess number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    print(answer) # TODO: REMOVE AFTER TESTING
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it.")
        # else:
        #   print("Sorry, you have not guessed correctly")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time.")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("Sorry, you didn't guessed it.")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it.")
#     else:
#         print("Sorry, you didn't guessed it.")
