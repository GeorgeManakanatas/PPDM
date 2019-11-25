# import csv
import timeit
from cryptography.fernet import Fernet


def EncryptTheProperFields(start_dataframe, encrypt_col):
    # generating key
    key = Fernet.generate_key()
    f = Fernet(key)
    for index_line in range(start_dataframe.shape[0]):
        for index_col in encrypt_col:
#            print('encrypting: ', index_line, index_col)
            byteValueToEncrypt = bytes(str(start_dataframe.loc[index_line, encrypt_col]), 'utf-8')
            encryptedValue = f.encrypt(byteValueToEncrypt)
            start_dataframe.loc[index_line, encrypt_col] = encryptedValue.decode("utf-8")
#            start_dataframe[index_line][encrypt_col[index_col]] = encryptedValue.decode("utf-8")
#    print(start_dataframe)
    return start_dataframe


def getDataWithEncryption (start_dataframe, enc_temp_file, encrypt_col):

    start = timeit.default_timer()  # starting timer
    # encrypt the proper fields
    EncryptTheProperFields(start_dataframe, encrypt_col)
#    print(start_dataframe)
    stop = timeit.default_timer()  # stop timer
    print("encrypt the proper fields time", stop-start)  # print the time

    return start_dataframe
