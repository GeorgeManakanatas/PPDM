'''
information masking section
'''
import logging
from . import encrypt_the_info
from . import null_the_info


def masking_method_selection(start_dataframe, mask_col, mask_method,
                             save_to_file, masked_file):
    '''
    Basic check that all input is properly provided and filtering through the
    various options if no error occurs

    Arguments:
        start_dataframe: the dataframe to mask
        mask_col(list): list of column numbers for the attributes to mask
        mask_method(str): the way the attributes should be masked
        save_to_file(bool): true to save the dataframe to temporary file
        masked_file(str): the file name for the output file

    Returns:
        dataframe with masking
    '''

    print("running data masking")
    logging.info('running masking on columns : '+str(mask_col))
    logging.info('masking method : '+str(mask_method))
    logging.info('dataframe before masking : '+str(start_dataframe.shape))
    # should be a list with selection in the future
    if mask_method == 'encrypt':
        start_dataframe = encrypt_the_info.encrypt_the_proper_columns(
            start_dataframe, mask_col)
    elif mask_method == 'replace':
        start_dataframe = null_the_info.null_the_proper_columns(
            start_dataframe, mask_col)
    else:
        logging.info('improper masking method provided : '+str(mask_method))
    logging.info('dataframe after masking : '+str(start_dataframe.shape))

    if save_to_file:
        start_dataframe.to_csv(masked_file, index=False, header=False)

    return start_dataframe
