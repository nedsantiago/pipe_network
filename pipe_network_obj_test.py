from pipe_network_obj import Structure, Link, GraphComponentTracker
import logging_config
import logging
import pytest

# initialize this module's logger with the name of this file
logger = logging.getLogger(__name__)

# creating the isolation function for the pytests
@pytest.fixture
def structure():
    return Structure()

@pytest.fixture
def structure01():
    return Structure()

@pytest.fixture
def structure02():
    return Structure()

@pytest.fixture
def structure03():
    return Structure()

@pytest.fixture
def component_tracker():
    return GraphComponentTracker()


# testing if structures are correctly compared
def test_all_structure_different(structure01, structure02, structure03):
    # is each structure different and not a copy?
    logger.info("Beginning test_structure_compare")
    assert structure01 == structure01
    assert structure01 != structure02
    assert structure02 != structure03
    assert structure03 != structure01

    # do lists work with these structures?
    ls_strucs = [structure01, structure02]
    assert structure01 in ls_strucs

# test nodes/structures
def test_set_structure_id(structure):
    test_value = "ERTFT090"
    structure.id = test_value

    assert structure.id == test_value, "Structure does not accept new id's correctly"

def test_graph_component_tracker_element_set(component_tracker, structure01, structure02):
    # add each structure
    component_tracker.add(structure01)
    component_tracker.add(structure02)
    component_tracker.add(structure03)

    # adding the same structure must cause AssertionError
    with pytest.raises(AssertionError) as e:
        structure01.id = "ERTFT001"
        component_tracker.add(structure01)
        logger.critical(f"test for component tracker ran into a problem: {e}")

def test_tracker_id_unique(component_tracker, structure01, structure02):

    # adding the same structure must cause AssertionError
    with pytest.raises(IndexError) as e:
        structure01.id = "ERTFT001"
        structure02.id = "ERTFT002"
        component_tracker.add(structure01)
        component_tracker.add(structure02)
        structure03.id = "ERTFT001"
        logger.critical(f"Adding should run a uniqueness check: {e}")

    # adding the same structure must cause AssertionError
    with pytest.raises(IndexError) as e:
        structure01.id = "ERTFT001"
        structure02.id = "ERTFT001"
        component_tracker.add(structure01)
        component_tracker.add(structure02)
        logger.critical(f"Tracker should check id uniqueness: {e}")

# test tracker if it is a singleton
def test_tracker_singleton(component_tracker):
    # create a second structure tracker
    component_tracker01 = GraphComponentTracker()
    assert component_tracker is component_tracker01, f"Component Tracker failed as a singleton"


# test edges/links
