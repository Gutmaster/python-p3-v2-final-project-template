from models.__init__ import CURSOR, CONN
from models.zoo import Zoo


class Animal:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, species, zoo_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.zoo_id = zoo_id

    def __repr__(self):
        return (
            f"<Animal {self.id}: {self.name}, Species: {self.species}, " +
            f"Home: {Zoo.find_by_id(self.zoo_id).name}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def zoo_id(self):
        return self._zoo_id

    @zoo_id.setter
    def zoo_id(self, zoo_id):
        if type(zoo_id) is int and Zoo.find_by_id(zoo_id):
            self._zoo_id = zoo_id
        else:
            raise ValueError(
                "zoo_id must reference a Zoo class in the database")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Animal instances """
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            species TEXT,
            zoo_id INTEGER,
            FOREIGN KEY (zoo_id) REFERENCES Zoos(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Animal instances """
        sql = """
            DROP TABLE IF EXISTS animals;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, species, zoo_id):
        """ Initialize a new Animal instance and save the object to the database """
        animal = cls(name, species, zoo_id)
        animal.save()
        return animal
    
    def save(self):
        """ Insert a new row with the name, region, and Zoo id values of the current Animal object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO animals (name, species, zoo_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.species, self.zoo_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def get_all(cls):
        """Return a list containing an Animal object per row in the table"""
        sql = """
            SELECT *
            FROM animals
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return an Animal object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        animal = cls.all.get(row[0])
        if animal:
            # ensure attributes match row values in case local instance was modified
            animal.name = row[1]
            animal.species = row[2]
            animal.zoo_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            animal = cls(row[1], row[2], row[3])
            animal.id = row[0]
            cls.all[animal.id] = animal
        return animal
    
    @classmethod
    def create(cls, name, species, zoo_id):
        """ Initialize a new Animal instance and save the object to the database """
        animal = cls(name, species, zoo_id)
        animal.save()
        return animal

    def update(self):
        """Update the table row corresponding to the current Animal instance."""
        sql = """
            UPDATE animals
            SET name = ?, species = ?, zoo_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.species, self.zoo_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Animal instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM animals
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
    
    @classmethod
    def find_by_id(cls, id):
        """Return Animal object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM animals
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_all_by_species(cls, species):
        """Returns all animals of a given species from the database"""
        sql = """
            SELECT *
            FROM animals
            where LOWER(species) = LOWER(?)
        """

        rows = CURSOR.execute(sql, (species,)).fetchall()
        animals = []
        for row in rows:
            animals.append(cls.instance_from_db(row))

        return animals