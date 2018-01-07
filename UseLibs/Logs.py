import logging
import logging.handlers
logpath = 'weblogs.log'
logger = logging.getLogger('web')
handler = logging.FileHandler(logpath)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(handler)



