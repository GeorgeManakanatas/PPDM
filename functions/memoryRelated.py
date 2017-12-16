import os
import sys


def checkMemoryRequirement(data_file):
    # Get the size of the csv file
    fileSize = checkTheFileSize(data_file) 
    # Get the max memory available to the system
    memoryStats = checkTheSysemMemory()
    # Get free value from tuple ( 'free', ... ) in memoryStats list of tuples
    freeMem = memoryStats[[i for i, v in enumerate(memoryStats) if v[0] == 'free'][0]][1]
    # Same for buff and cached
    buffMem = memoryStats[[i for i, v in enumerate(memoryStats) if v[0] == 'buff'][0]][1]
    cachedMem = memoryStats[[i for i, v in enumerate(memoryStats) if v[0] == 'cached'][0]][1]
    # calculating upper limit set to 80% of max available memory (configurable in the future)
    maxMemory = freeMem + buffMem + cachedMem
    upperLimit =  maxMemory * 80 /100
    # if data size less than free memory ok 
    if fileSize < freeMem:
        # do nothing
        print('the data is a small fraction of the available memory')
    elif fileSize > freeMem and fileSize < upperLimit:
        # still go on but give warning, print for now popup window later
        print('the data is a significant fraction of the available memory the pc may slow down!')
    elif fileSize > upperLimit:
        # do not move on
        print('the data is too big')
        print('data size: ',fileSize,' and memory limit: ',upperLimit)
        sys.exit(0)
         
    return
    
    
def checkTheFileSize(data_file):
    # information on the file
    fileStatInfo = os.stat(data_file)
    # returning the file size in kB
    returnValue = fileStatInfo.st_size / 1024
    
    return returnValue


def checkTheSysemMemory():
    # linux specific solution for memory info
    with open('/proc/meminfo', 'r') as systemMemory:
            meminfoLines = systemMemory.readlines()
    
    memoryStats = [] 
    # building list of tuples from file info, all values in kB
    memoryStats.append(( 'tot' , int(meminfoLines[0].split()[1]) )) # total memory
    memoryStats.append(( 'free' , int(meminfoLines[1].split()[1]) )) # free memory at the time
    memoryStats.append(( 'buff' , int(meminfoLines[2].split()[1]) )) # memory used by the buffer
    memoryStats.append(( 'cached' , int(meminfoLines[3].split()[1]) )) # memory used as cache
    memoryStats.append(( 'shared' , int(meminfoLines[20].split()[1]) )) # shared memory
    memoryStats.append(( 'swapt' , int(meminfoLines[14].split()[1]) )) # total swap memory
    memoryStats.append(( 'swapf' , int(meminfoLines[15].split()[1]) )) # free swap memory
    
    return memoryStats
    
    
