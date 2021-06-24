import logging

def setup_custom_logger(name, logging_conf):
    # logging setup
    my_logger = logging.getLogger(name)
    my_logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(logging_conf['folder']+logging_conf['filename'])
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    my_logger.addHandler(file_handler)
    # 
    return my_logger