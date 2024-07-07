#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.zoo import Zoo
from models.animal import Animal

def seed_database():
    Animal.drop_table()
    Zoo.drop_table()
    Zoo.create_table()
    Animal.create_table()

    # Create seed data
    WoodlandPark = Zoo.create("Woodland Park Zoo", "Seattle, WA")
    SanDiego = Zoo.create("San Diego Zoo", "San Diego, CA")

    Animal.create("Herbert", "Gorilla", WoodlandPark.id)
    Animal.create("Jonulus", "Panda", SanDiego.id)


seed_database()
print("Seeded database")