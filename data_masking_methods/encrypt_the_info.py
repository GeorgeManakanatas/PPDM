# import csv
import timeit
import logging
from cryptography.fernet import Fernet


def encrypt_the_proper_columns(start_dataframe, encrypt_col):
    start = timeit.default_timer()
    # generating key
    key = Fernet.generate_key()
    logging.info('the key used to encrypt the run : '+str(key))
    f = Fernet(key)
    for index_line in range(start_dataframe.shape[0]):
        for index_col in encrypt_col:
            byteValueToEncrypt = bytes(str(start_dataframe.loc[index_line, encrypt_col]), 'utf-8')
            encryptedValue = f.encrypt(byteValueToEncrypt)
            start_dataframe.loc[index_line, encrypt_col] = encryptedValue.decode("utf-8")

    stop = timeit.default_timer()
    print("encrypt the proper fields time", stop-start)  # print the time
    return start_dataframe
