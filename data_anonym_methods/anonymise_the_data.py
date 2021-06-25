''' anonymise the data module.
functions:
    master: selects the type of anonymisation to be performed on the data
'''

# import csv

import timeit
from . import k_anonymity

def master(start_dataframe, nums, kmin, save_to_file, anonym_file, logger):
    '''
    perform simple K-anonymity for now. Random generation of adequate number
    of extra entries

    Arguments:
        start_dataframe: the dataframe to anonymise
        nums(list): list of column numbers considered an identifying combo
        kmin(str): the minimum number of entries desired
        save_to_file(bool): true to save the output dataframe to temporary file
        anonym_file(str): the file name for the output file
        logger: custom logging method

    Returns:
        dataframe with added false entries
    '''
    total_anonymise_start = timeit.default_timer()
    logger.info('running k-anonymity on columns : '+str(nums)+' with kmin : '
                 + str(kmin))
    logger.info('dataframe before anonymisation : ' +
                 str(start_dataframe.shape))
    anonymized_and_masked_data = k_anonymity.simple_kanonymity(start_dataframe,
                                                               nums, kmin, logger)
    # logging the outcome
    logger.info('dataframe after anonymisation : ' +
                 str(anonymized_and_masked_data.shape))
    # saving to file if that option was set to True
    if save_to_file:
        start_dataframe.to_csv(anonym_file, index=False, header=False)
    total_anonymise_stop = timeit.default_timer()
    # logging the excecution time
    logger.info(" Total anonymisation time is:" +
                 str(total_anonymise_stop-total_anonymise_start))

    return anonymized_and_masked_data


if __name__ == '__main__':
    master()
