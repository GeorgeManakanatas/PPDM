''' anonymise the data module.
functions:
    master: selects the type of anonymisation to be performed on the data
'''

# import csv
from . import k_anonymity


def master(start_dataframe, nums, kmin):
    """ perform simple
    import the column selection """
    anonymized_and_masked_data = k_anonymity.simple_kanonymity(start_dataframe,
                                                               nums, kmin)
    # write the info in a file because the Apriori is not updated #
#    with open(file_name, "w") as f1:
#        mywriter = csv.writer(f1, delimiter=',', quotechar='|')
#        for line in range(len(anonymized_and_masked_data)):
#            mywriter.writerow(anonymized_and_masked_data[line])
#        f1.close()
    return anonymized_and_masked_data


if __name__ == '__main__':
    master()
