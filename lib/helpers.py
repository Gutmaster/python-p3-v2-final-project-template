from models.zoo import Zoo
from models.animal import Animal


def exit_program():
    print("\nGoodbye!")
    exit()

def list_zoos():
    print()
    zoos = Zoo.get_all()
    if not zoos:
        print("\nNo zoos found!")
        return -1
    else:
        for zoo in zoos:
            print(zoo)

def list_animals():
    print()
    animals = Animal.get_all()
    if not animals:
        print("No animals found")
    else:
        for animal in animals:
            print(animal)

def list_animals_by_zoo():
    if list_zoos() == -1:
        return
    try:
        zoo_id = int(input('\nEnter the zoo ID:'))
    except ValueError:
        print("\nInvalid zoo ID")
        return
    zoo = Zoo.find_by_id(zoo_id)
    if zoo:
        print()
        animals = zoo.get_animals()
        if animals:
            for animal in animals:
                print(animal)
        else:
            print("\nNo animals in this zoo")
        return zoo_id
    else:
        print("\nZoo not found")
        return None

def create_zoo():
    name = input('\nEnter the zoo name: ')
    blood = input("Enter the location: ")
    try:
        zoo = Zoo.create(name, blood)
        print(f'\nSuccess: {zoo}')
    except Exception as exc:
        print("\nError creating zoo: ", exc)

def update_zoo():
    id_ = input("\nEnter the zoo's id: ")
    if zoo := Zoo.find_by_id(id_):
        print(f"{zoo}")
        try:
            name = input("Enter the new name (leave blank to keep the same): ")
            location = input("Enter the new location (leave blank to keep the same): ")
            if name:
                zoo.name = name
            if location:
                zoo.location = location
            zoo.update()
            print(f'\nSuccess: Zoo {zoo.name} updated')
        except Exception as exc:
            print("\nError updating zoo: ", exc)
    else:
        print(f'\nZoo not found')
    
def close_zoo():
    id_ = input("\nEnter the zoo's id: ")
    if zoo := Zoo.find_by_id(id_):
        animals = zoo.get_animals()
        for animal in animals:
            animal.delete()
            print(f'Goodbye, {animal.name}!')
        try:
            zoo.delete()
            print(f'\nSuccess: Zoo {zoo.name} deleted\n')
        except Exception as exc:
            print("\nError deleting zoo: ", exc)
    else:
        print(f'\nPlease enter a valid zoo id')


def create_animal():
    name = input("\nEnter the animal's name: ")
    species = input("Enter the animal's species: ")
    list_zoos()
    zoo_id = int(input("\nEnter the zoo this animal will be placed in: "))
    try:
        animal = Animal.create(name, species, zoo_id)
        print(f'\nSuccess: {animal}')
    except Exception as exc:
        print("\nError creating animal: ", exc)

def transfer_animal():
    print("\nChoose a zoo to transfer from: ")
    zoo_id = list_animals_by_zoo()
    if zoo_id is None:
        return
    try:
        animal_id = int(input("\nEnter the animal ID: "))
    except ValueError:
        print("\nInvalid animal ID")
        return
    animal = Animal.find_by_id(animal_id)
    if animal.zoo_id == zoo_id:
        list_zoos()
        try:
            new_zoo_id = int(input("\nEnter the new zoo ID: "))
        except ValueError:
            print("\nInvalid zoo ID")
            return
        if new_zoo_id == zoo_id:
            print(f'\n{animal.name} is already in this zoo. \n')
            return
        try:
            animal.zoo_id = new_zoo_id
            animal.update()
            print(f'\nSuccess: {animal.name} transferred to {Zoo.find_by_id(new_zoo_id).name}')
        except Exception as exc:
            print("\nError transferring animal: ", exc)
    else:
        print(f'\n{animal.name} is not in this zoo. \n')


def update_animal():
    id_ = input("\nEnter the animal's id: ")
    if animal := Animal.find_by_id(id_):
        print(f"{animal}")
        
        try:
            animal.name = input("Enter the animal's new name: ")
            animal.species = input("Enter the animal's species: ")

            animal.update()
            print(f'\nSuccess: {animal}')
        except Exception as exc:
            print("\nError updating animal: ", exc)
    else:
        print(f'\nAnimal not found')

def free_animal():
    id_ = input("\nEnter the animal's id: ")
    if animal := Animal.find_by_id(id_):
        animal.delete()
        print(f'\nSuccess: Animal {animal.name} has been returned to nature.')
        print(f'Goodbye, {animal.name}!\n')
    else:
        print(f'\nAnimal {id_} not found')

def list_animals_by_species():
    species = input("\nEnter the species name: ")
    animals = Animal.find_all_by_species(species)
    print()
    for animal in animals:
        print(animal)