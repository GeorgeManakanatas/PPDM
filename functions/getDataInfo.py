import timeit
import pandas as pd
pd.set_option('display.max_columns', None)


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
#    print(totline, ' lines in file: ', data_file)

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
def CreateDataDictionary(data_file):
    start = timeit.default_timer()  # starting timer
    # Get the number of lines in the csv file
    lines = db_lines(data_file)
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
#    print ("create dictionary time", stop-start) # print the time
    
    return dataDictionary


def create_dataframe(data_file):
    start = timeit.default_timer()  # starting timer
    new_dataframe = pd.read_csv(data_file, header=None)
    stop = timeit.default_timer() # stop timer
#    print ("create dataframe time", stop-start) # print the time
    return new_dataframe
