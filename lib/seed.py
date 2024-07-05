#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.vertebrate import Vertebrate
from models.animal import Animal

def seed_database():
    Animal.drop_table()
    Vertebrate.drop_table()
    Vertebrate.create_table()
    Animal.create_table()

    # Create seed data
    Mammals = Vertebrate.create("Mammals", "Warm")
    Reptiles = Vertebrate.create("Reptiles", "Cold")
    Animal.create("Rabbit", "Forest", Mammals.id)
    Animal.create("Snake", "Jungle", Reptiles.id)


seed_database()
print("Seeded database")