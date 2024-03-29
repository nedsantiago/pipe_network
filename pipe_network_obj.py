# PROCESS:
# structure and pipe objects
import logging_config
import logging

# initialize logger
logger = logging.getLogger(__name__)

class GraphComponentTracker():
    def __init__(self):
        self.element_set = set()

    def __new__(cls):
        """This new function makes this object into a singleton.
        Calling new instances of the object will only call the first
        instance of the object."""

        # if an instance does not yet exist
        if not hasattr(cls, 'instance'):
            # create the instance
            cls.instance = super(GraphComponentTracker, cls).__new__(cls)
        
        # return the instance
        return cls.instance


    def add(self, element):
        """This method only adds an element when not existing
        in the element set. This aims to check if element already
        exists"""
        
        # if element is in element set
        if element in self.element_set:
            # raise an assertion error
            msg = f"element:{element} already exists in element set"
            logger.warning(msg)
            raise AssertionError(msg)
        # else (element is unique and not in set)
        else:
            # add to element set
            self.element_set.add(element)
            
    def contains_element(self, element):
        return element in self.element_set

    def empty(self):
        return len(self.element_set) == 0

    def remove(self):
        if self.empty():
            msg = "empty element set"
            logger.info(msg)
            raise Exception(msg)
        else:
            node = self.element_set[-1]
            self.element_set = self.element_set[:-1]
            return node

class GraphComponent():
    """this object initializes with a unique id by default"""

    def __init__(self):
        self._id = None
    
    @property
    def id(self) -> str:
        """Get the id string of the current component"""
        return self._id
    
    @id.setter
    def id(self, id):
        """Set the id string of the current component"""
        
        # set the value
        self._id = id

    def __str__(self) -> str:
        if self._id == None:
            msg = "Graph Component has no id: please add an id before calling this component"
            logger.critical(msg)
            raise ValueError(msg)
        else:
            return self.id


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