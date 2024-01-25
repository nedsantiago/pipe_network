from pipe_network_obj import Structure, Link
import logging_config
import logging

# initialize this module's logger with the name of this file
logger = logging.getLogger(__name__)

structure01 = Structure()
structure02 = Structure()
structure03 = Structure()
link01 = Link()
ls_strucs = [structure01, structure02]

logger.debug(f"struc1==struc1:{structure01==structure01}struc1==struc2:{structure01==structure02}")
logger.info(f"structure01 in ls_struc:{structure01 in ls_strucs}")
logger.warning(f"structure03 in ls_struc:{structure03 in ls_strucs}")