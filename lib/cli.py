# lib/cli.py

from helpers import (
    exit_program,
    list_zoos,
    create_zoo,
    list_animals,
    create_animal,
    transfer_animal
)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_zoos()
        elif choice == "2":
            create_zoo()
        elif choice == "3":
            list_animals()
        elif choice == "4":
            create_animal()
        elif choice == "5":
            transfer_animal()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List zoos")
    print("2. Add a new Zoo")
    print("3. List all animals")
    print("4. Add an animal")
    print("5. Transfer an animal")


if __name__ == "__main__":
    main()
