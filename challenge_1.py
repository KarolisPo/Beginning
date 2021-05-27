
while True:
    print("\n1. Learn Python.\n2. Learn Java.\n3. Learn C++.\n4. Go to Bed."
          "\n5. Play PC.\n6. Watch TV.\n7. Go jogging.\n8. WoW.\n9. Quit")
    choice = int(input("What is your choice?: "))

    if choice == 1:
        print("I am happy you are dedicated")
    elif choice == 2:
        print("Better learn python.")
    elif choice == 3:
        print("BOOOOring")
    elif choice == 4:
        print("Good night.")
    elif choice == 5:
        print("CS?")
    elif choice == 6:
        print("TV? Never better.")
    elif choice == 7:
        print("Let's run.")
    elif choice == 8:
        print("LOL")
    elif choice == 9:
        print("Goodbye")
        break
    else:
        print("Invalid choice")
        continue