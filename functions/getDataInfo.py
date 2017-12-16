import timeit

# get the number of lines in the csv file
def db_lines(data_file):
    f1 = open(data_file, "r")
    totline = 0
    while True:
        info = f1.readline()
        totline = totline + 1
        if info == "":
            break
    f1.close()
    print(totline,' lines in file: ',data_file)
    
    return totline


# get the number of columns in the csv file
def db_columns(data_file):
    f1 = open(data_file, "r")
    line = f1.readline()
    words = line.split(",")
    totcol = len(words)
    f1.close()
    
    return totcol


# get the data out of the csv file
def CreateDataDictionary(lines, data_file):
    start = timeit.default_timer()  # starting timer
    # opening the data file
    openFile = open(data_file, "r")
    # initializing the dictionary
    dataDictionary = {}
    # reading each line into the dictionary
    for index_line in range(lines-1):
        line = openFile.readline()
        line = line.strip('\n')
        words = line.split(",")
        dataDictionary[index_line]=words
    # closing the opened data file   
    openFile.close()
    stop = timeit.default_timer() # stop timer
    print ("get the data from file time", stop-start) # print the time
    
    return dataDictionary