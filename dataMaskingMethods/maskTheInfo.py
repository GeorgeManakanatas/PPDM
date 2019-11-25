from . import encryptTheInfo

def maskingMethodSelection(start_dataframe, enc_temp_file, encrypt_col):
#    print(start_dataframe, enc_temp_file, encrypt_col)
    # should be a list with selection in the future
    dataWithMasking = encryptTheInfo.getDataWithEncryption(start_dataframe, 
                                                           enc_temp_file,
                                                           encrypt_col)
    
    return dataWithMasking
