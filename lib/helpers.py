from models.zoo import Zoo
from models.animal import Animal


def exit_program():
    print("Goodbye!")
    exit()

def list_zoos():
    zoos = Zoo.get_all()
    for zoo in zoos:
        print(zoo)

def list_animals():
    animals = Animal.get_all()
    for animal in animals:
        print(animal)

def list_animals_by_zoo():
    list_zoos()
    zoo_id = int(input('Enter the zoo ID: \n'))
    zoo = Zoo.find_by_id(zoo_id)
    if zoo:
        animals = zoo.get_animals()
        for animal in animals:
            print(animal)
        return zoo_id
    else:
        print("Zoo not found")

def create_zoo():
    name = input('\nEnter the zoo name: ')
    blood = input("Enter the location: ")
    try:
        zoo = Zoo.create(name, blood)
        print(f'Success: {zoo}')
    except Exception as exc:
        print("Error creating zoo: ", exc)

def create_animal():
    name = input("Enter the animal's name: ")
    species = input("Enter the animal's species: ")
    list_zoos()
    zoo_id = int(input("Enter the zoo this animal will be transferred to: "))
    try:
        animal = Animal.create(name, species, zoo_id)
        print(f'Success: {animal}')
    except Exception as exc:
        print("Error creating animal: ", exc)

def transfer_animal():
    zoo_id = list_animals_by_zoo()
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
            print(f'\nSuccess: Animal {animal.name} transferred to zoo {new_zoo_id}\n')
        except Exception as exc:
            print("Error transferring animal: ", exc)
    else:
        print(f'\n{animal.name} is not in this zoo. \n')


# def update_employee():
#     id_ = input("Enter the employee's id: ")
#     if employee := Employee.find_by_id(id_):
#         try:
#             employee.name = input("Enter the employee's new name: ")
#             employee.job_title = input("Enter the employee's new job title: ")
#             employee.department_id = int(input("Enter the employee's new department id: "))

#             employee.update()
#             print(f'Success: {employee}')
#         except Exception as exc:
#             print("Error updating employee: ", exc)
#     else:
#         print(f'Employee {id_} not found')