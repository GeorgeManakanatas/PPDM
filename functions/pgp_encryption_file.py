import csv
from cryptography.fernet import Fernet


def master(enc_temp_file, lines, encrypt_col, data_file):

    """calling the function that removes the selected columns from DB"""
    final = remove_columns(lines, encrypt_col, data_file)

    '''calling the routine that encrypts the text of the removed columns'''
    encrypted_text = encrypt_routine(lines, encrypt_col, final)

    '''calling the routine that createsd the new encrypted DB file
    and commiting the end result to pgp.txt'''
    new_db = recompile_file(lines, encrypt_col, encrypted_text, data_file)

    with open(enc_temp_file, "wb") as csvfile:
        print ("creating file")
        grafias = csv.writer(csvfile, delimiter=',', lineterminator='', quoting=csv.QUOTE_NONE, escapechar=" ")
        for index_line in range(lines-1):
            grafias.writerow(new_db[index_line])
    return

'''
moves the selected column-columns from the original DB file
to a list of lists that is then returned to master.
'''


def remove_columns(lines, encrypt_col, data_file):
    final = []
    temp = []
    '''opening the data file, should we have the name from external input?'''
    '''
    outer loop reading one line at a time & separating the values
    inner loop copy the values in the selected columns then making
    a temporary list that we append to a list of lists
    '''

    f1 = open(data_file, "r")

    for index_line in range(lines-1):
        line = f1.readline()
        line = line.strip('\n')
        words = line.split(",")
        for index_col in range(len(encrypt_col)):
            temp.append(words[encrypt_col[index_col]])
        final.append(temp)
        temp = []

    f1.close()
    print ("end of remove columns")
    return final

''' gets the list of lists with the selected columns from master
    turns it into a single string and encrypts it '''


def encrypt_routine(lines, encrypt_col, final):
    """ from list of lists to string """
    unitary_string = ""
    for index_line in range(lines-1):
        for index_col in range(len(encrypt_col)):
            unitary_string = unitary_string + final[index_line][index_col]
    '''generating key and encrypting string'''
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypt_thing = f.encrypt(unitary_string)
    print ("end of encrypt routine")
    return encrypt_thing

'''recompiling the DB into an encrypted one and saved in a file'''


def recompile_file(lines, encrypt_col, encrypted_text, data_file):
    """calculating the number of slots to be filled"""
    slots = lines*len(encrypt_col)

    '''calculating the modulus of encrypted text to slots
    if it exists we add characters to the next exact number.'''
    if len(encrypted_text) % slots != 0:
        for index in range(slots-(len(encrypted_text) % slots)):
            encrypted_text += "X"

    '''calculating the number of characters for each slot (equal number for all)
    and creating a list of lists with the entire database'''
    character_lenth = len(encrypted_text)/slots

    '''reading the DB one line at a time and replacing the apropriate values'''
    f1 = open(data_file, "r")
    counter = 0
    final_DB = []
    for index_line in range(lines-1):
        line = f1.readline()
        words = line.split(",")
        for index_col in range(len(encrypt_col)):
            words[encrypt_col[index_col]] = encrypted_text[counter:counter+character_lenth]
            counter += character_lenth
        final_DB.append(words)

    f1.close()
    print ("end of recompile file")
    return final_DB
