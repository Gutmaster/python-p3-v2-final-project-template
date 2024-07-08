from models.zoo import Zoo
from models.animal import Animal


def exit_program():
    print("Goodbye!")
    exit()

def list_zoos():
    zoos = Zoo.get_all()
    if not zoos:
        print("No zoos found!")
        return -1
    else:
        for zoo in zoos:
            print(zoo)

def list_animals():
    animals = Animal.get_all()
    if not animals:
        print("No animals found!")
    else:
        for animal in animals:
            print(animal)

def list_animals_by_zoo():
    if list_zoos() == -1:
        return
    zoo_id = int(input('Enter the zoo ID: \n'))
    zoo = Zoo.find_by_id(zoo_id)
    if zoo:
        animals = zoo.get_animals()
        if animals:
            for animal in animals:
                print(animal)
        else:
            print("No animals in this zoo!")
        return zoo_id
    else:
        print("Zoo not found")
        return None

def create_zoo():
    name = input('\nEnter the zoo name: ')
    blood = input("Enter the location: ")
    try:
        zoo = Zoo.create(name, blood)
        print(f'Success: {zoo}')
    except Exception as exc:
        print("Error creating zoo: ", exc)

def update_zoo():
    id_ = input("Enter the zoo's id: ")
    if zoo := Zoo.find_by_id(id_):
        print(f"{zoo}")
        try:
            name = input("Enter the new name (leave blank to keep the same): ")
            blood = input("Enter the new location (leave blank to keep the same): ")
            if name:
                zoo.name = name
            if blood:
                zoo.blood = blood
            zoo.update()
            print(f'\nSuccess: Zoo {zoo.name} updated\n')
        except Exception as exc:
            print("Error updating zoo: ", exc)
    else:
        print(f'\nZoo not found\n')
    
def close_zoo():
    id_ = input("Enter the zoo's id: ")
    if zoo := Zoo.find_by_id(id_):
        animals = zoo.get_animals()
        for animal in animals:
            animal.delete()
            print(f'Goodbye, {animal.name}!')
        try:
            zoo.delete()
            print(f'\nSuccess: Zoo {zoo.name} deleted\n')
        except Exception as exc:
            print("Error deleting zoo: ", exc)


def create_animal():
    name = input("Enter the animal's name: ")
    species = input("Enter the animal's species: ")
    list_zoos()
    zoo_id = int(input("Enter the zoo this animal will be placed in: "))
    try:
        animal = Animal.create(name, species, zoo_id)
        print(f'Success: {animal}')
    except Exception as exc:
        print("Error creating animal: ", exc)

def transfer_animal():
    zoo_id = list_animals_by_zoo()
    if zoo_id is None:
        return
    animal_id = int(input("Enter the animal ID: "))
    animal = Animal.find_by_id(animal_id)
    if animal.zoo_id == zoo_id:
        list_zoos()
        new_zoo_id = int(input("Enter the new zoo ID: "))
        if new_zoo_id == zoo_id:
            print(f'\n{animal.name} is already in this zoo. \n')
            return
        try:
            animal.zoo_id = new_zoo_id
            animal.update()
            print(f'\nSuccess: {animal.name} transferred to {Zoo.find_by_id(new_zoo_id).name}\n')
        except Exception as exc:
            print("Error transferring animal: ", exc)
    else:
        print(f'\n{animal.name} is not in this zoo. \n')


def update_animal():
    id_ = input("Enter the animal's id: ")
    if animal := Animal.find_by_id(id_):
        print(f"{animal}")
        
        try:
            animal.name = input("Enter the animal's new name: ")
            animal.species = input("Enter the animal's species: ")

            animal.update()
            print(f'Success: {animal}')
        except Exception as exc:
            print("Error updating animal: ", exc)
    else:
        print(f'Animal {id_} not found')

def free_animal():
    id_ = input("Enter the animal's id: ")
    if animal := Animal.find_by_id(id_):
        animal.delete()
        print(f'\nSuccess: Animal {animal.name} has been returned to nature.')
        print(f'Goodbye, {animal.name}!\n')
    else:
        print(f'Animal {id_} not found')

def list_animals_by_species(species):
    animals = Animal.find_all_by_species(species)
    print()
    for animal in animals:
        print(animal)
    print()