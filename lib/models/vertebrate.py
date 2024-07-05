# lib/models/department.py
from models.__init__ import CURSOR, CONN


class Vertebrate:
    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, blood_type, id=None):
        self.id = id
        self.name = name
        self.blood_type = blood_type

    def __repr__(self):
        return f"<Classification {self.id}: {self.name}, {self.blood_type}>"

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
        

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Vertebrate instances """
        sql = """
            CREATE TABLE IF NOT EXISTS vertebrates (
            id INTEGER PRIMARY KEY,
            name TEXT,
            blood_type TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Vertebrate instances """
        sql = """
            DROP TABLE IF EXISTS vertebrates;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, blood_type):
        """ Initialize a new Vertebrate instance and save the object to the database """
        vertebrate = cls(name, blood_type)
        vertebrate.save()
        return vertebrate

    def save(self):
        """ Insert a new row with the name and location values of the current Vertebrate instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO vertebrates (name, blood_type)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.blood_type))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def get_all(cls):
        """Return a list containing a Vertebrate object per row in the table"""
        sql = """
            SELECT *
            FROM vertebrates
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return a Vertebrate object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        vertebrate = cls.all.get(row[0])
        if vertebrate:
            # ensure attributes match row values in case local instance was modified
            vertebrate.name = row[1]
            vertebrate.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            vertebrate = cls(row[1], row[2])
            vertebrate.id = row[0]
            cls.all[vertebrate.id] = vertebrate
        return vertebrate

    @classmethod
    def find_by_id(cls, id):
        """Return a Vertebrate object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM vertebrates
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None