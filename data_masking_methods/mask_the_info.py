from . import encrypt_the_info
from . import null_the_info

def masking_method_selection(start_dataframe, mask_col):
    # should be a list with selection in the future
#    start_dataframe = encrypt_the_info.encrypt_the_proper_columns(start_dataframe,
#                                                               mask_col)
    start_dataframe = null_the_info.null_the_proper_columns(start_dataframe,
                                                               mask_col)

    return start_dataframe
