from pipe_network_obj import Structure, Link
import logging_config
import logging
import pytest

# initialize this module's logger with the name of this file
logger = logging.getLogger(__name__)

# creating the isolation function for the pytests
@pytest.fixture
def structure():
    return Structure()

# testing if structures are correctly compared
def test_structure_compare():
    # after creating three structures
    structure01 = Structure()
    structure02 = Structure()
    structure03 = Structure()

    # is each structure different and not a copy?
    logger.info("Beginning test_structure_compare")
    assert structure01 == structure01
    assert structure01 != structure02
    assert structure02 != structure03
    assert structure03 != structure01

    # do lists work with these structures?
    ls_strucs = [structure01, structure02]
    assert structure01 in ls_strucs
