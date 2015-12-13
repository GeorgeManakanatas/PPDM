import os.path
'''counts the total lines and the number of columns in the database file '''
def db_lines(data_file):
    f1 = open(data_file, "r")
    totline = 0
    while True:
        info = f1.readline()
        totline = totline + 1
        if info == "":
            break
    f1.close()
    return totline

def db_columns():
    f1 = open(data_file, "r")
    totline = 0
    line = f1.readline()
    words = line.split(",")
    totcol = len(words)
    f1.close()
    return totcol