import csv
import timeit
from cryptography.fernet import Fernet

def EncryptTheProperFields(lines, encrypt_col, dataDictionary):
    # generating key
    key = Fernet.generate_key()
    f = Fernet(key)
    numOfColToEnc = len(encrypt_col)
    for index_line in range(lines-1):
        for index_col in range(numOfColToEnc):
            # getting the value out of the table in the dictionary
            valueToEncrypt = dataDictionary[index_line][encrypt_col[index_col]]
            # transforming to bytes for the encryption to digest
            byteValueToEncrypt = bytes(valueToEncrypt, 'utf-8')
            # the real encryption step
            encryptedValue = f.encrypt(byteValueToEncrypt)
            # turn back to sting
            strEncryptedValue = encryptedValue.decode("utf-8")
            # replace with ecrypted value
            dataDictionary[index_line][encrypt_col[index_col]] = strEncryptedValue
    # in te end return the now encrypted info
    
    return dataDictionary


def getDataWithEncryption (enc_temp_file, lines, encrypt_col, data_file):
    
    start = timeit.default_timer()  # starting timer
    # get the data
    dataDictionary = CreateDataDictionary(lines, data_file)
    stop = timeit.default_timer() # stop timer
    print ("get the data time", stop-start) # print the time
    
    start = timeit.default_timer()  # starting timer
    # encrypt the proper fields
    encryptedDataDictionary = EncryptTheProperFields(lines, encrypt_col, dataDictionary)
    stop = timeit.default_timer() # stop timer
    print ("encrypt the proper fields", stop-start) # print the time
    
    start = timeit.default_timer()  # starting timer
    # place the values in new temp file just to maintain commonality with old code 
    with open(enc_temp_file, "w") as csvfile:
        grafias = csv.writer(csvfile, delimiter=',', lineterminator='', quoting=csv.QUOTE_NONE, escapechar=" ")
        for index_line in range(lines-1):
            # print(encryptedDataDictionary[index_line])
            grafias.writerow(encryptedDataDictionary[index_line])
    
    stop = timeit.default_timer() # stop timer
    print ("Write file time", stop-start) # print the time
    
    return encryptedDataDictionary


def CreateDataDictionary(lines, data_file):
    # opening the data file
    openFile = open(data_file, "r")
    # initializing the dictionary
    dataDictionary = {}
    # reading each line into the dictionary
    for index_line in range(lines-1):
        line = openFile.readline()
        line = line.strip('\n')
        words = line.split(",")
        dataDictionary[index_line]=words
    # closing the opened data file   
    openFile.close()
    
    return dataDictionary