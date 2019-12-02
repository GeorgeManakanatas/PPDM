# -*- coding: utf-8 -*-
import os
import logging
# import sys
import timeit
import json
from data_anonym_methods import anonymise_the_data
from data_mining_methods import Apriori_timer
from functions import getDataInfo, memoryRelated
from data_masking_methods import mask_the_info


def main():
    logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                        filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # run the gui
    # os.system('python3 GUI/licensePage.py')
    # os.system('python3 GUI/GUI_call_from_main.py')
    # os.system('python3 GUI/test2.py')

    """
    A config file is created with the values for this run.

    data_file is the csv file containing the original data
    min_sup is the minimum level of supprot
    min_conf is the minimum level of confidence
    kmin = k anonymity level
    nums = columns to anonymize
    mask_col = columns to encrypt
    anonym_file = temp output file name
    """
    logging.info("--- starting new run ---")
    total_prep_time_start = timeit.default_timer()
    # initialize environment
    with open('config.json', 'r') as json_data_file:
        conf = json.load(json_data_file)
        # trouble getting arrays in to the environment
        # for item in conf:
        # print(item, conf[item])
        # os.environ[item] = str(conf[item])

    # assign values to variables from configuration file
    kmin = int(conf["kmin"])
    nums = conf["nums"]
    mask_col = conf["mask_col"]
    mask_method = conf["mask_method"]
    min_supp = float(conf["min_supp"])
    min_conf = float(conf["min_conf"])
    data_file = conf["data_file_location"]+conf["data_file_name"]
    anonym_file = conf["temp_folder_location"]+conf["anonym_file"]
    masked_file = conf["temp_folder_location"]+conf["masked_file"]
    save_to_file = conf["save_to_file"]
    # Check the size of the data to be imported
    memoryRelated.checkMemoryRequirement(data_file)
    # load data into dataframe
    start_dataframe = getDataInfo.create_dataframe(data_file)
    total_prep_time_stop = timeit.default_timer()
    logging.info(" Total prep time is:" +
                 str(total_prep_time_stop-total_prep_time_start))
#    throw_away_variable = input('press enter to continue the programm')

    # encrypting / masking the proper columns
    total_mask_time_start = timeit.default_timer()
    start_dataframe = mask_the_info.masking_method_selection(start_dataframe,
                                                             mask_col,
                                                             mask_method,
                                                             save_to_file,
                                                             masked_file)
    total_mask_time_stop = timeit.default_timer()
    logging.info(" Total masking time is:" +
                 str(total_mask_time_stop-total_mask_time_start))
#    throw_away_variable = input('press enter to continue the programm')

    # calling k-anonymity for the masked data file
    total_anonymise_start = timeit.default_timer()
    start_dataframe = anonymise_the_data.master(start_dataframe, nums, kmin,
                                                save_to_file, anonym_file)
    total_anonymise_stop = timeit.default_timer()
    logging.info(" Total anonymisation time is:" +
                 str(total_anonymise_stop-total_anonymise_start))
#    throw_away_variable = input('press enter to continue the programm')

    # calling the apriori method for the masked and anonymised data
    total_apriori_start = timeit.default_timer()
    print("running apriori")
    Apriori_timer.master(anonym_file, min_supp, min_conf)
    total_apriori_stop = timeit.default_timer()
    logging.info(" Total apriori time is:" +
                 str(total_apriori_stop-total_apriori_start))
#    throw_away_variable = input('press enter to end the programm')

    # cleaning up the temp files
    os.remove(anonym_file)
    os.remove(masked_file)

    # end of program input to keep the window open
    # throw_away_variable = input('press enter to end the programm')


if __name__ == '__main__':
    main()
