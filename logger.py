import logging
from container import config
level = getattr(logging, config.logger['level'].upper())
logging.basicConfig(level=level, format='%(asctime)s %(levelname)s:  %(message)s')
logger = logging.getLogger(__name__)
