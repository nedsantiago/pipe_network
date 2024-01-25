# PROCESS:
# structure and pipe objects


class GraphComponentTracker():
    def __init__(self):
        self.element_list = list()

    def add(self, element):
        """This method only adds an element when not existing
        in the node list. This aims to stop duplicate 
        elements in list"""
        
        # if element not in frontier
        if element not in self.element_list:
            # append to frontier
            self.element_list.append(element)
        # else (already in frontier)
        else:
            # pass
            pass

    def contains_element(self, element):
        return element in self.element_list

    def empty(self):
        return len(self.element_list) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.element_list[-1]
            self.element_list = self.element_list[:-1]
            return node

class GraphComponent():
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


class Structure(GraphComponent):
    """this object encapsulates all the properties of a generic structure.
    Naming borrowed from Storm and Sanitary Analysis
    - id
    - coordinates (northing, easting)
    - """
    
    @property
    def coordinates(self) -> tuple:
        """Get the coordinates of the current structure"""
        return self._coordinates


class Link(GraphComponent):
    """this object encapsulates all the properties of a generic link.
    Naming borrowed from Storm and Sanitary Analysis
    - id
    - id1 = structure connection one
    - id2 = structure connection two"""

    @property
    def coordinates(self) -> tuple:
        """Get the coordinates of the current structure"""
        return self._coordinates