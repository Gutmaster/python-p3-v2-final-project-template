#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_zoos,
    create_zoo,
    update_zoo,
    close_zoo,
    list_animals,
    create_animal,
    update_animal,
    transfer_animal,
    free_animal,
    list_animals_by_species,
    list_animals_by_zoo
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
            update_zoo()
        elif choice == "4":
            close_zoo()
        elif choice == "5":
            list_animals()
        elif choice == "6":
            create_animal()
        elif choice == "7":
            update_animal()
        elif choice == "8":
            transfer_animal()
        elif choice == "9":
            free_animal()
        elif choice == "10":
            list_animals_by_species()
        elif choice == "11":
            list_animals_by_zoo()
        else:
            print("\nInvalid choice")
        input("\nPress Enter to continue...")


def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. List zoos")
    print("2. Add a new zoo")
    print("3. Update a zoo")
    print("4. Close a zoo")
    print("5. List all animals")
    print("6. Add an animal")
    print("7. Update an animal")
    print("8. Transfer an animal")
    print("9. Free an animal")
    print("10. Get all animals of a given species")
    print("11. List animals by zoo")


if __name__ == "__main__":
    main()
