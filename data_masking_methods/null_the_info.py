# -*- coding: utf-8 -*-


def null_the_proper_columns(start_dataframe, encrypt_col):
    
    new_value = 'null'
    # replace column values with the new_value
    for index_col in encrypt_col:
        start_dataframe[encrypt_col] = new_value

    return start_dataframe
