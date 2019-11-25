import csv
from . import kAnonymity


def master(start_dataframe, file_name, nums, kmin):
    """ perform simple  """
    """ import the column selection """
    anonymizedAndMaskedData = kAnonymity.master(start_dataframe, file_name, nums, kmin)
    # write the info in a file because the Apriori is not updated #
    with open(file_name, "w") as f1:
        mywriter = csv.writer(f1, delimiter=',', quotechar='|')
        for line in range(len(anonymizedAndMaskedData)):
            mywriter.writerow(anonymizedAndMaskedData[line])
        f1.close()

    return


if __name__ == '__main__':
    master()
