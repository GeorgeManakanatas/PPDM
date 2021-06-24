'''
information masking section
'''
import logging
import timeit
from . import encrypt_the_info
from . import null_the_info


def masking_method_selection(start_dataframe, mask_col, mask_method,
                             save_to_file, masked_file, logger):
    '''
    Basic check that all input is properly provided and filtering through the
    various options if no error occurs. Logging and timer handled here as well.

    Arguments:
        start_dataframe: the dataframe to mask
        mask_col(list): list of column numbers for the attributes to mask
        mask_method(str): the way the attributes should be masked
        save_to_file(bool): true to save the dataframe to temporary file
        masked_file(str): the file name for the output file
        logger: custom logging function

    Returns:
        dataframe with masked properties
    '''
    total_mask_time_start = timeit.default_timer()

    logger.info('running masking method : ' + str(mask_method) +
                 ' on columns : ' + str(mask_col))
    logger.info('dataframe before masking : ' + str(start_dataframe.shape))
    # should be a list with selection in the future
    if mask_method == 'encrypt':
        start_dataframe = encrypt_the_info.encrypt_the_proper_columns(
            start_dataframe, mask_col)
    elif mask_method == 'replace':
        start_dataframe = null_the_info.null_the_proper_columns(
            start_dataframe, mask_col)
    else:
        logger.info('improper masking method provided : '+str(mask_method))
        return False
    # logging the outcome
    logger.info('dataframe after masking : '+str(start_dataframe.shape))
    # saving to file if that option was set to True
    if save_to_file:
        start_dataframe.to_csv(masked_file, index=False, header=False)
    total_mask_time_stop = timeit.default_timer()
    # logging the excecution time
    logger.info(" Total masking time is:" +
                 str(total_mask_time_stop-total_mask_time_start))

    return start_dataframe