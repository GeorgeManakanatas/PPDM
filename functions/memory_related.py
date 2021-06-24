import os
import sys
import platform
import psutil


def check_memory_requirement(data_file, logger):
    # Get the size of the csv file
    file_size = check_the_file_size(data_file, logger)
    # check memory depnding on system type
    if get_the_os_type() == 'windows':
        free_mem, upper_limit = check_memory_windows(logger)
    else:
        free_mem, upper_limit = check_memory_linux(logger)
    # if data size less than free memory ok
    if file_size < free_mem:
        # do nothing
        logger.info('the data is a fraction of the free memory')
        # print('the data is a fraction of the free memory')
    elif file_size > free_mem and file_size < upper_limit:
        # still go on but give warning, print for now popup window later
        logger.info('the data is a significant fraction of the available memory the \
              pc may slow down!')
        # print('the data is a significant fraction of the available memory the \
            #   pc may slow down!') 
    elif file_size > upper_limit:
        # do not move on
        logger.info('the data is too big try to make more memory available')
        logger.info('data size: '+str(file_size)+' and memory limit: '+str(upper_limit))
        # print('the data is too big try to make more memory available')
        # print('data size: ', file_size, ' and memory limit: ', upper_limit)
        sys.exit(0)
    return


def get_the_os_type():
    operating_system = platform.system()
    # print(platform.version())
    # print(platform.platform())
    return operating_system.lower()


def check_the_file_size(data_file, logger):
    '''
    Checking the csv file size.
    
    Arguments:
        data_file: the file we are checking
        logger: custom logging function
    
    Returns:
        returnValue: (int) the file size in kB 
    '''
    try:
        # information on the file
        fileStatInfo = os.stat(data_file)
        # returning the file size in kB
        returnValue = fileStatInfo.st_size / 1024
        return returnValue
    except:
        e = sys.exc_info()[0]
        # log error 
        logger.info('Error in check_the_file_size: '+str(e))
        return 0


def check_memory_windows(logger):
    '''
    Checking memory for windows os
    
    Arguments:
        logger: custom logging function
    
    Returns:
        free_mem: (int) the free memory in kB
        upper_limit: (int) upper memory limit in kB
    '''
    try:
        memory_stats = {}
        # building list of tuples from file info, all values in kB
        memory_stats['total'] = int(psutil.virtual_memory().total)
        memory_stats['available'] = int(psutil.virtual_memory().available)
        memory_stats['used'] = int(psutil.virtual_memory().used)
        memory_stats['free'] = int(psutil.virtual_memory().free)
        # free memory and upper_limit
        free_mem = memory_stats.get('free') / 1024
        upper_limit = memory_stats.get('available') * 0.8 / 1024
        return free_mem, upper_limit
    except:
        e = sys.exc_info()[0]
        # log error 
        logger.info('Error in check_memory_windows: '+str(e))
        return 0


def check_memory_linux(logger):
    '''
    Checking memory for linux os
    
    Arguments:
        logger: custom logging function
    
    Returns:
        free_mem: (int) the free memory in kB
        upper_limit: (int) upper memory limit in kB 
    '''
    try:
        # linux specific solution for memory info
        with open('/proc/meminfo', 'r') as systemMemory:
            meminfoLines = systemMemory.readlines()
        # initialise memory stats
        memory_stats = {}
        # building list of tuples from file info, all values in kB
        memory_stats['tot'] = int(meminfoLines[0].split()[1])
        memory_stats['free'] = int(meminfoLines[1].split()[1])
        memory_stats['buff'] = int(meminfoLines[2].split()[1])
        memory_stats['cached'] = int(meminfoLines[3].split()[1])
        memory_stats['shared'] = int(meminfoLines[20].split()[1])
        # Get free value from tuple ( 'free', ... ) in memory_stats list of tuples
        free_mem = memory_stats.get('free')
        # Same for buff and cached
        buffMem = memory_stats.get('buff')
        cachedMem = memory_stats.get('cached')
        # calculating upper limit set to 80% of max available memory
        # (configurable in the future)
        maxMemory = (free_mem + buffMem + cachedMem)
        upper_limit = maxMemory * 0.8 / 1024
        return free_mem, upper_limit
    except:
        e = sys.exc_info()[0]
        # log error 
        logger.info('Error in check_memory_linux: '+str(e))
        return 0
