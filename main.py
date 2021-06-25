# -*- coding: utf-8 -*-
import os
import timeit
from config import my_config
from custom_logger.custom_logger import setup_custom_logger
from data_anonym_methods import anonymise_the_data
from data_mining_methods import Apriori_timer
from functions import get_data_info, memory_related, fileFunctions
from data_masking_methods import mask_the_info




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

total_prep_time_start = timeit.default_timer()

# Reading config file into variable
my_config.config_file()
# setting up custom logger
logger = setup_custom_logger('PPDM', my_config.config_values['logging_configuration'])
logger.info("--- starting new run ---")

# assign values to variables from configuration file
data_file = my_config.config_values["data_file_location"]+my_config.config_values["data_file_name"]
anonym_file = my_config.config_values["temp_folder_location"]+my_config.config_values["anonym_file"]
masked_file = my_config.config_values["temp_folder_location"]+my_config.config_values["masked_file"]
# Check the size of the data to be imported
memory_related.check_memory_requirement(data_file, logger)
# load data into dataframe
start_dataframe = get_data_info.create_dataframe(data_file, logger)




total_prep_time_stop = timeit.default_timer()
logger.info(" Total prep time is:" +
                str(total_prep_time_stop-total_prep_time_start))
# encrypting / masking the proper columns
start_dataframe = mask_the_info.masking_method_selection(
        start_dataframe,
        my_config.config_values["mask_col"],
        my_config.config_values["mask_method"],
        my_config.config_values["save_to_file"],
        masked_file,
        logger)

# calling k-anonymity for the masked data file
start_dataframe = anonymise_the_data.master(start_dataframe,
                                            my_config.config_values["nums"],
                                            my_config.config_values["kmin"],
                                            my_config.config_values["save_to_file"],
                                            anonym_file,
                                            logger)

# calling the apriori method for the masked and anonymised data
Apriori_timer.master(start_dataframe, anonym_file,
                     my_config.config_values["min_supp"],
                     my_config.config_values["min_conf"],
                     logger)
logger.info("--- execution is finished ---")
print('--- execution is finished ---')

# end of program input to keep the window open
# throw_away_variable = input('press enter to end the programm')