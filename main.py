# -*- coding: utf-8 -*-
import os
import sys
import timeit
import json
from Anonym_methods import AnonymiseTheData
from Data_Mining_Methods import Apriori_timer
from functions import getDataInfo
from dataMaskingMethods import maskTheInfo
from functions import memoryRelated



def main():
    
    # run the gui
    """
     os.system('python3 GUI/licensePage.py')
     os.system('python3 GUI/GUI_call_from_main.py')
    # os.system('python3 GUI/test2.py')
    """
    """
    A temp config file is created with the values for this run.

    data_file is the csv file containing the original data
    min_sup is the minimum level of supprot
    min_conf is the minimum level of confidence
    kmin = k anonymity level
    nums = columns to anonymize
    encrypt_col = columns to encrypt
    file_name = temp output file name
    """
    totalPrepTimeStart = timeit.default_timer()  # starting timer
    with open('temp/config.json','r') as json_data_file:
        conf = json.load(json_data_file)
    
    # assign values to variables from configuration file #
    
    kmin = int(conf["kmin"])
    nums = conf["nums"]
    encrypt_col = conf["encrypt_col"]
    min_supp = float(conf["min_supp"])
    min_conf = float(conf["min_conf"])
    data_file = conf["data_file_location"]+conf["data_file_name"]
    file_name = conf["tempFileLocation"]+conf["file_name"]
    enc_temp_file = conf["tempFileLocation"]+conf["enc_temp_file"]
    
    # Check the size of the data to be imported
    memoryRelated.checkMemoryRequirement(data_file)
    # Get the number of lines in the csv file
    lines = getDataInfo.db_lines(data_file)
    # Get the number of columns in the csv file  
    columns = getDataInfo.db_columns(data_file)
    # Get dictionary with data from csv
    dataDictionary = getDataInfo.CreateDataDictionary(lines, data_file)
    totalPrepTimeStop = timeit.default_timer() # stop timer
    print (" Total prep time is:", totalPrepTimeStop-totalPrepTimeStart)
    
    # calling the encryption and recompile routines #
    
    totalMaskTimeStart = timeit.default_timer()  # starting timer
    # get the data after sections are masked
    dataWithMasking = maskTheInfo.maskingMethodSelection(dataDictionary, enc_temp_file, lines, encrypt_col)
    totalMaskTimeStop = timeit.default_timer() # stop timer
    print (" Total mask time is:", totalMaskTimeStop-totalMaskTimeStart)  
    
    lines = getDataInfo.db_lines(data_file)
    lines = getDataInfo.db_lines(enc_temp_file)
    
    
    # calling k-anonymity for the encrypted file #
    # perhaps just return the list of lists and not go to file at all? #
    
    start = timeit.default_timer()
    print ("running k-anonymity")
    AnonymiseTheData.master(dataWithMasking, file_name, lines, nums, kmin)
    stop = timeit.default_timer()
    print ("anonym time is:", stop-start)


    # calling the apriori method #
   
    start = timeit.default_timer()
    print ("running apriori")
    Apriori_timer.master(file_name, min_supp, min_conf)
    stop = timeit.default_timer()
    print ("apriori time is:", stop-start)

    # deleting temp files #
    os.remove(file_name)
    os.remove(enc_temp_file)
    #os.remove("temp/config.json")
    
    # end of program input to keep the window open #
    s = raw_input('press enter to end the programm')


if __name__ == '__main__':
    main()
