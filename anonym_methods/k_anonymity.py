''' k anonymity module

functions:
    master: performs selection of the anonymisation methods
    simple_kanonymity: performs simplistic anonymisation

'''


def master(start_dataframe, nums, kmin):
    ''' implements k Anonymity

    Parameters:
    argument1 (dataframe): the data that we want to anonymise
    argument2 (array): the columns of the dataframe that when combined become
    identifying
    argument3 (int): the minimum acceptable number of combinations

    Returns:
    (dataframe): the anonymised dataframe

    '''
    # should be a list of possible options later
    start_dataframe = simple_kanonymity(start_dataframe, nums, kmin)

    return start_dataframe


def simple_kanonymity(start_dataframe, nums, kmin):
    '''Performs simple k anonymity

    Parameters:
    argument1 (dataframe): the data that we want to anonymise
    argument2 (array): the columns of the dataframe that when combined become
    identifying
    argument3 (int): the minimum acceptable number of combinations

    Returns:
    (dataframe): the anonymised dataframe with no special inteligence involved
    in creating the extra rows
    '''

    # getting a count of the identifying column combination
    combination_counts = start_dataframe.groupby(nums).size()
    # removing those above the threshhold
    in_need_of_expansion = combination_counts[combination_counts <= kmin]
    # looping through all the combinations in need of expansion
    for index_number, identyfying_combination_count in\
            enumerate(in_need_of_expansion):
        # determine number of false entries needed
        false_entries = kmin - identyfying_combination_count
        # generate the number of false entries
        rows = start_dataframe.sample(n=false_entries)
        # append new rows to dataframe
        start_dataframe = start_dataframe.append(rows, ignore_index=True)

    return start_dataframe


if __name__ == '__main__':
    master()
