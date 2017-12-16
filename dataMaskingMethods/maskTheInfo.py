from . import encryptTheInfo

def maskingMethodSelection(dataDictionary, enc_temp_file, lines, encrypt_col):
    
    # should be a list with selection in the future
    dataWithMasking = encryptTheInfo.getDataWithEncryption(dataDictionary, enc_temp_file, lines, encrypt_col)
    
    return dataWithMasking
