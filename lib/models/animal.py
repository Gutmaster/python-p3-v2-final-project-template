from models.__init__ import CURSOR, CONN
from models.vertebrate import Vertebrate


class Animal:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, region, vertebrate_id, id=None):
        self.id = id
        self.name = name
        self.region = region
        self.vertebrate_id = vertebrate_id

    def __repr__(self):
        return (
            f"<Animal {self.id}: {self.name}, {self.region}, " +
            f"Classification: {self.vertebrate_id}>"
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
    def vertebrate_id(self):
        return self._vertebrate_id

    @vertebrate_id.setter
    def vertebrate_id(self, vertebrate_id):
        if type(vertebrate_id) is int and Vertebrate.find_by_id(vertebrate_id):
            self._vertebrate_id = vertebrate_id
        else:
            raise ValueError(
                "vertebrate_id must reference a vertebrate class in the database")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Animal instances """
        sql = """
            CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY,
            name TEXT,
            region TEXT,
            vertebrate_id INTEGER,
            FOREIGN KEY (vertebrate_id) REFERENCES vertebrates(id))
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
    def create(cls, name, region, vertebrate_id):
        """ Initialize a new Animal instance and save the object to the database """
        animal = cls(name, region, vertebrate_id)
        animal.save()
        return animal
    
    def save(self):
        """ Insert a new row with the name, region, and vertebrate id values of the current Animal object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO animals (name, region, vertebrate_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.region, self.vertebrate_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self