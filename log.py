import logging
import logging.config
import yaml


def get_logger(name=None, path='log.yaml'):
    with open(path, 'rt', encoding='utf-8') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    if name:
        return logging.getLogger(name)
    else:
        return logging.getLogger('root')

logger = get_logger()
