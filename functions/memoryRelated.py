import os
import sys
import platform
import psutil


def checkMemoryRequirement(data_file):
    # Get the size of the csv file
    fileSize = checkTheFileSize(data_file)
    # check memory depnding on system type
    if get_the_os_type() == 'windows':
        freeMem, upperLimit = check_memory_windows(fileSize)
    else:
        freeMem, upperLimit = check_memory_linux(fileSize)
    # if data size less than free memory ok
    if fileSize < freeMem:
        # do nothing
        print('the data is a fraction of the free memory')
    elif fileSize > freeMem and fileSize < upperLimit:
        # still go on but give warning, print for now popup window later
        print('the data is a significant fraction of the available memory the \
              pc may slow down!')
    elif fileSize > upperLimit:
        # do not move on
        print('the data is too big try to make more memory available')
        print('data size: ', fileSize, ' and memory limit: ', upperLimit)
        sys.exit(0)
    return


def get_the_os_type():
    operating_system = platform.system()
    # print(platform.version())
    # print(platform.platform())
    return operating_system.lower()


def checkTheFileSize(data_file):
    # information on the file
    fileStatInfo = os.stat(data_file)
    # returning the file size in kB
    returnValue = fileStatInfo.st_size / 1024
    return returnValue


def check_memory_windows(fileSize):
    memory_stats = {}
    # building list of tuples from file info, all values in kB
    memory_stats['total'] = int(psutil.virtual_memory().total)
    memory_stats['available'] = int(psutil.virtual_memory().available)
    memory_stats['used'] = int(psutil.virtual_memory().used)
    memory_stats['free'] = int(psutil.virtual_memory().free)
    # free memory and upperlimit
    freeMem = memory_stats.get('free') / 1024
    upperLimit = memory_stats.get('available') * 0.8 / 1024
    return freeMem, upperLimit


def check_memory_linux(fileSize):
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
    freeMem = memory_stats.get('free')
    # Same for buff and cached
    buffMem = memory_stats.get('buff')
    cachedMem = memory_stats.get('cached')
    # calculating upper limit set to 80% of max available memory
    # (configurable in the future)
    maxMemory = (freeMem + buffMem + cachedMem)
    upperLimit = maxMemory * 0.8 / 1024
    return freeMem, upperLimit
