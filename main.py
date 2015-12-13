# -*- coding: utf-8 -*-
import winsound
import os
import timeit
from Anonym_methods import Anonymise_simple
from Anonym_methods import Kanon_file
from Data_Mining_Methods import Apriori_timer
from packages import get_db_info
from packages import pgp_encryption_file
# from GUI import My_main_GUI_single


def main():
    """
    The main funciton calls the GUI for input then runs the encryption - anonymity - data mining modules as they have
    been selected by the user in the GUI. The
    """

    """
    call GUI and return a list with the proper values for:
    name of the file with the data
    level of required support and confidence
    level of Kmin , columns to apply it to , columns to encrypt
    -------------------------------------------
    still problem harvesting the thing to work like I want it.
    will use the following list for now:
    user_input[0] is the level of anonymity we want to apply
    user_input[1] is a list of the attributes we want to anonymise
    user_input[2] is a list of the attributes we want to encrypt
    min_sup is the minimum level of supprot
    min_conf is the minimum level of confidence
    """
    # My_main_GUI_single.start_gui_window()
    user_input = [3, [0, 1, 3], [2]]
    min_supp = 0.3
    min_conf = 0.9
    data_file = "adult_dataset.txt"

    """
    Get the number of lines in the databaze and the number of attributes (columns)
    """
    lines = get_db_info.db_lines(data_file)
    """
    initialising variables and tables
    kmin = k anonymity level
    nums = columns to anonymize
    encrypt_col = columns to encrypt
    """
    kmin = user_input[0]
    nums = user_input[1]
    encrypt_col = user_input[2]

    file_name = "kanonDB_to_delete.txt"
    """
    calling the encryption and recompile routines
    """
    start = timeit.default_timer()
    pgp_encryption_file.master(lines, encrypt_col, data_file)
    Kanon_file.master(lines, nums)
    stop = timeit.default_timer()
    print "prep time is:", stop-start
    winsound.Beep(2000, 500)

    """
    calling k-anonymity for the encrypted file
    perhaps just return the list of lists and not go to file at all?
    """
    start = timeit.default_timer()
    print "running k-anonymity"
    Anonymise_simple.master(lines, nums, kmin)
    stop = timeit.default_timer()
    print "anonym time is:", stop-start
    winsound.Beep(2000, 500)

    """
    calling the apriori method
    """
    start = timeit.default_timer()
    print "running apriori"
    Apriori_timer.master(file_name, min_supp, min_conf)
    stop = timeit.default_timer()
    print "apriori time is:", stop-start
    winsound.Beep(2000, 500)

    """
    deleting temp files
    """
    os.remove("kanonDB_to_delete.txt")
    os.remove("pgp.txt")

    """
    end of program line
    """
    # s = raw_input('press enter to end the programm')

if __name__ == '__main__':
    main()