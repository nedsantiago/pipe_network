# PROCESS:
# structure and pipe objects


class UniqueObject():
    """this object initializes with a unique id by default"""

    _id_sets = set()

    def __new__(cls):
        new_instance = super().__new__(cls)

        # initialize a new id
        init_id = len(cls._id_sets) + 1

        # while the id is among the previously declared ids
        while init_id in cls._id_sets:
            # increment by 1 to change it
            init_id += 1

        # now that id is unique, add to collection of ids
        cls._id_sets.add(init_id)

        # give the new instance the id
        new_instance._id = init_id

        # return the current new instance of the object
        return new_instance
    
    @property
    def id(self) -> int:
        """Get the id number of the current structure"""
        return self._id
    
    def __str__(self) -> str:
        return f"{self.id}"


class Structure(UniqueObject):
    """this object encapsulates all the properties of a generic structure.
    Naming borrowed from Storm and Sanitary Analysis
    - id
    - coordinates (northing, easting)
    - """
    
    @property
    def coordinates(self) -> tuple:
        """Get the coordinates of the current structure"""
        return self._coordinates


class Link(UniqueObject):
    """this object encapsulates all the properties of a generic link.
    Naming borrowed from Storm and Sanitary Analysis
    - id
    - id1 = structure connection one
    - id2 = structure connection two"""

    @property
    def coordinates(self) -> tuple:
        """Get the coordinates of the current structure"""
        return self._coordinates