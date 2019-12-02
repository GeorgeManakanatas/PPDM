''' anonymise the data module.
functions:
    master: selects the type of anonymisation to be performed on the data
'''

# import csv
from . import k_anonymity
import logging


def master(start_dataframe, nums, kmin, save_to_file, anonym_file):
    """ perform simple
    import the column selection """

    print("running k-anonymity")
    logging.info('running k-anonymity on columns : '+str(nums)+' with kmin : '
                 + str(kmin))
    logging.info('dataframe before anonymisation : ' +
                 str(start_dataframe.shape))
    anonymized_and_masked_data = k_anonymity.simple_kanonymity(start_dataframe,
                                                               nums, kmin)
    logging.info('dataframe after anonymisation : ' +
                 str(anonymized_and_masked_data.shape))
    if save_to_file:
        start_dataframe.to_csv(anonym_file, index=False, header=False)

    return anonymized_and_masked_data


if __name__ == '__main__':
    master()
