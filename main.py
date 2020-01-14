# -*- coding: utf-8 -*-
import os
import logging
import timeit
import json
from data_anonym_methods import anonymise_the_data
from data_mining_methods import Apriori_timer
from functions import get_data_info, memory_related, fileFunctions
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
    conf["kmin"] = int(conf["kmin"])
    conf["min_supp"] = float(conf["min_supp"])
    conf["min_conf"] = float(conf["min_conf"])
    data_file = conf["data_file_location"]+conf["data_file_name"]
    anonym_file = conf["temp_folder_location"]+conf["anonym_file"]
    masked_file = conf["temp_folder_location"]+conf["masked_file"]
    conf["save_to_file"] = bool(conf["save_to_file"])
    # Check the size of the data to be imported
    memory_related.check_memory_requirement(data_file)
    # load data into dataframe
    start_dataframe = get_data_info.create_dataframe(data_file)

    

    
    total_prep_time_stop = timeit.default_timer()
    logging.info(" Total prep time is:" +
                 str(total_prep_time_stop-total_prep_time_start))
    # encrypting / masking the proper columns
    start_dataframe = mask_the_info.masking_method_selection(
            start_dataframe,
            conf["mask_col"],
            conf["mask_method"],
            conf["save_to_file"],
            masked_file)
    # calling k-anonymity for the masked data file
    start_dataframe = anonymise_the_data.master(start_dataframe,
                                                conf["nums"],
                                                conf["kmin"],
                                                conf["save_to_file"],
                                                anonym_file)
    # calling the apriori method for the masked and anonymised data
    Apriori_timer.master(anonym_file, conf["min_supp"], conf["min_conf"])
    print('execution is finished.')
    # cleaning up the temp files
    if not conf["save_to_file"]:
        os.remove(anonym_file)
        os.remove(masked_file)

    # end of program input to keep the window open
    # throw_away_variable = input('press enter to end the programm')


if __name__ == '__main__':
    main()
