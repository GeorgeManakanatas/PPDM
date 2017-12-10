# -*- coding: utf-8 -*-
import os
import timeit
import json
from Anonym_methods import Anonymise_simple
from Anonym_methods import Kanon_file
from Data_Mining_Methods import Apriori_timer
from functions import get_db_info
from functions import pgp_encryption_file
# from GUI import My_main_GUI_single
# from GUI import licence


def main():
    """
    run the gui
    """
    os.system('python GUI/GUI_call_from_main.py')
    """
    Still not shure how to run the GUI properly.

    Will read these values from the config file.

    data_file is the csv file containing the original data
    min_sup is the minimum level of supprot
    min_conf is the minimum level of confidence
    kmin = k anonymity level
    nums = columns to anonymize
    encrypt_col = columns to encrypt
    file_name = temp output file name
    """
    with open('config.json') as json_data_file:
        conf = json.load(json_data_file)
    """
    assign values to variables
    """
    kmin = int(conf["kmin"])
    nums = conf["nums"]
    encrypt_col = conf["encrypt_col"]
    min_supp = float(conf["min_supp"])
    min_conf = float(conf["min_conf"])
    data_file = conf["data_file_location"]+conf["data_file_name"]
    file_name = conf["file_name"]
    enc_temp_file = conf["enc_temp_file"]
    """
    Get the number of lines in the csv file
    """
    lines = get_db_info.db_lines(data_file)
    """
    Get the number of columns in the csv file
    """
    columns = get_db_info.db_columns(data_file)
    """
    calling the encryption and recompile routines
    """
    start = timeit.default_timer()  # starting timer
    pgp_encryption_file.master(enc_temp_file, lines, encrypt_col, data_file)
    Kanon_file.master(enc_temp_file, lines, nums)
    stop = timeit.default_timer()
    print "prep time is:", stop-start
    # winsound.Beep(2000, 500)

    """
    calling k-anonymity for the encrypted file
    perhaps just return the list of lists and not go to file at all?
    """
    start = timeit.default_timer()
    print "running k-anonymity"
    Anonymise_simple.master(enc_temp_file, file_name, lines, nums, kmin)
    stop = timeit.default_timer()
    print "anonym time is:", stop-start
    # winsound.Beep(2000, 500)

    """
    calling the apriori method
    """
    start = timeit.default_timer()
    print "running apriori"
    Apriori_timer.master(file_name, min_supp, min_conf)
    stop = timeit.default_timer()
    print "apriori time is:", stop-start
    # winsound.Beep(2000, 500)

    """
    deleting temp files
    """
    os.remove(file_name)
    os.remove(enc_temp_file)

    """
    end of program line
    """
    s = raw_input('press enter to end the programm')

if __name__ == '__main__':
    main()
