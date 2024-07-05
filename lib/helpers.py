from models.vertebrate import Vertebrate
from models.animal import Animal


def exit_program():
    print("Goodbye!")
    exit()


def list_vertebrates():
    vertebrates = Vertebrate.get_all()
    for vertebrate in vertebrates:
        print(vertebrate)