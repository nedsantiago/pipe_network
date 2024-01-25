# PROCESS:
# structure and pipe objects
import logging_config
import logging

# initialize logger
logger = logging.getLogger(__name__)

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
            msg = f"element:{element} already exists in element list"
            logger.warning(msg)
            raise AssertionError(msg)

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

    def __init__(self):
        self._id = None
    
    @property
    def id(self) -> str:
        """Get the id string of the current component"""
        return self._id
    
    @id.setter
    def id(self, id):
        """Set the id string of the current component"""
        
        # check if among previous id's
        if id in self._id_sets:
            # then assert that it should be unique
            raise AssertionError(f"The id:{id} already exists in network")
        
        # set the value
        self._id = id

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