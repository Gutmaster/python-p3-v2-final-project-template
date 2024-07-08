# Phase 3 CLI+ORM Project 
## Zoos Keeper

## Introduction
This command line interface provides a way to track different zoos and the
animals that live there. You can run this program by entering `python lib.cli.py` 
into the terminal from the project directory. You may need to run `chmod +x` on 
the file first to gain permissions.


# File Descriptions

## seed.py
This file resets and seeds the zoo_network database with initial values for
the program. It can be run by entering `python lib/seed.py`. Permission may
need to be granted with `chmod +x`.



## cli.py
This file provides the user interface for the program. Users can select
from a list of options to manipulate and view the data in the database.

### main
This is the function that is called when the program is started and which
runs the entire time the program is being executed. It's a simple while 
loop that waits for user input and then displays the appropriate data and
options that the user requests.

### menu
Menu is a helper function that simply displays the primary input options
available to the user.



## helpers.py
This file contains all the helper function that are called by the CLI in cli.py.

### exit_program
Prints a goodbye message and closes the interface.

### list_zoos
Displays a list of all zoos in the zoos database.

### create_zoo
Prompts the user for a name and location for a new zoo to add to the database.

### update_zoo
Allows a user to select an existing zoo to edit the name and location.

### close_zoo
Closes a zoo in the database, deleting it and all animals associated with it
from their respective database.

### list_animals
Displays a list of all animals in the animals database.

### create_animal
Prompts the user for a name and species of a new animal, as well as the id of
the zoo it will be assigned to.

### update_animal
Allos a user to update the name and species of an animal.

### transfer_animal
Allows the user to transfer an animal from one zoo to another by selecting the
source zoo, an animal within, and the new zoo it will go to.

### free_animal
Deletes an animal from the animals database, and displays a farewell message.

### list_animals_by_species
Prompts the user for a species and lists all animals of that species.

### list_animals_by_zoo
Prompts the user for a zoo id and lists all animals in that zoo.



## zoo.py
This file defines the structure of our zoos database and contains all of the functions
that interact directly with it. All functions are contained within the Zoo class, which
corresponds with our zoos database and copies and tracks each row as a Python object.

### __init__
Takes a name and location for the Zoo object and runs it through our validataions to 
ensure that valid strings are passed in.

### __repr__
Defines how our Zoo object will be formatted and printed to the console.

### create_table
Class method that uses SQL through sqlite to create and persist a database table for all zoos.

### drop_table
Class method that uses SQL through sqlite to drop the zoos table.

### create
Class method that creates a new row for the zoos table.

### save
Instance method that uses sqlite to save the current instance to the zoos database.
    
### update
Instance method that update the corresponding entry in the zoos table with the current
instance's attributes.

### delete
Instance method that deletes the corresponding entry in the zoos table.

### get_all
Class method that returns all entries from the zoos table as Python objects.

### instance_from_db
Class method that takes a row from the database and finds and returns the corresponding
instance from the Zoo class, creating a new instance if it doesn't exist.

### find_by_id
Class method that takes an ID and returns the corresponding database entry as a Python object.

### get_animals
Instance method that returns an array of all animals in the animals database who's foreign key
matches the Zoo instance it is called on.



## animal.py
This file defines the structure of our animals database and contains all of the functions
that interact directly with it. All functions are contained within the Animal class, which
corresponds with our animals database and copies and tracks each row as a Python object.

### __init__
Takes a name, species, and zoo_id for the Animal object and runs it through our validataions to 
ensure that valid values are passed in.

### __repr__
Defines how our Animal object will be formatted and printed to the console.

### create_table
Class method that uses SQL through sqlite to create and persist a database table for all animals.

### drop_table
Class method that uses SQL through sqlite to drop the animals table.

### create
Class method that creates a new row for the animals table.

### save
Instance method that uses sqlite to save the current instance to the animals database.
    
### update
Instance method that update the corresponding entry in the animals table with the current
instance's attributes.

### delete
Instance method that deletes the corresponding entry in the animals table.

### get_all
Class method that returns all entries from the animals table as Python objects.

### instance_from_db
Class method that takes a row from the database and finds and returns the corresponding
instance from the Animal class, creating a new instance if it doesn't exist.
    
### find_by_id
Class method that takes an ID and returns the corresponding database entry as a Python object.
    
### find_all_by_species
Class method that takes a species as a string and returns a list of corresponding Python objects
from the database.
