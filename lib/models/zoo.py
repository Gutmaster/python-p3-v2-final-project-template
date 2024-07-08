# lib/models/department.py
from models.__init__ import CURSOR, CONN

class Zoo:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Zoo {self.id}: {self.name}, {self.location}>"

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
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError(
                "Location must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Zoo instances """
        sql = """
            CREATE TABLE IF NOT EXISTS zoos (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Zoo instances """
        sql = """
            DROP TABLE IF EXISTS zoos;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        """ Initialize a new Zoo instance and save the object to the database """
        zoo = cls(name, location)
        zoo.save()
        return zoo

    def save(self):
        """ Insert a new row with the name and location values of the current Zoo instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO zoos (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """Update the table row corresponding to the current Zoo instance."""
        sql = """
            UPDATE zoos
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Zoo instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM zoos
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing a Zoo object per row in the table"""
        sql = """
            SELECT *
            FROM zoos
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return a Zoo object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        zoo = cls.all.get(row[0])
        if zoo:
            # ensure attributes match row values in case local instance was modified
            zoo.name = row[1]
            zoo.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            zoo = cls(row[1], row[2])
            zoo.id = row[0]
            cls.all[zoo.id] = zoo
        return zoo

    @classmethod
    def find_by_id(cls, id):
        """Return a Zoo object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM zoos
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def get_animals(self):
        from models.animal import Animal
        """Return a list containing a Animal object per row in the table where the zoo_id matches the current Zoo instance's id"""
        sql = """
            SELECT *
            FROM animals
            WHERE zoo_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()

        return [Animal.instance_from_db(row) for row in rows]