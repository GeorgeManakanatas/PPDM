''' k anonymity module

functions:
    master: performs selection of the anonymisation methods
    simple_kanonymity: performs simplistic anonymisation

'''


def master(start_dataframe, nums, kmin, logger):
    '''
    implements k Anonymity

    Parameters:
    argument1 (dataframe): the data that we want to anonymise
    argument2 (array): the columns of the dataframe that when combined become
    identifying
    argument3 (int): the minimum acceptable number of combinations
    logger: custom logging function

    Returns:
    (dataframe): the anonymised dataframe

    '''
    # should be a list of possible options later
    start_dataframe = simple_kanonymity(start_dataframe, nums, kmin, logger)

    return start_dataframe


def simple_kanonymity(start_dataframe, nums, kmin, logger):
    '''
    Performs simple k anonymity

    Parameters:
    argument1 (dataframe): the data that we want to anonymise
    argument2 (array): the columns of the dataframe that when combined become
    identifying
    argument3 (int): the minimum acceptable number of combinations
    logger: custom logging function

    Returns:
    (dataframe): the anonymised dataframe with no special inteligence involved
    in creating the extra rows
    '''

    logger.info('Performing simplistic K-anonymity')
    # getting a count of the identifying column combination
    combination_counts = start_dataframe.groupby(nums).size()
    logger.info('There are : '+str(len(combination_counts.index))+' identifying combinations')
    # keeping those with fewer entries than the minimum needed
    in_need_of_expansion = combination_counts[combination_counts < kmin]
    logger.info('Only '+str(len(in_need_of_expansion.index))+' are below the '+str(kmin)+' kmin limit')
    # looping through all the combinations that need to be expanded with
    # false entries to reach our minimum goal
    for index_number, identyfying_combination_count in\
            enumerate(in_need_of_expansion):
        # determine number of false entries needed
        false_entries = kmin - identyfying_combination_count
        # generate the number of false entries
        rows = start_dataframe.sample(n=false_entries)
        # loop through every column we want to anonymise
        for column in range(len(in_need_of_expansion.index.names)):
            # set the values of the column to the one we want to mask
            rows[in_need_of_expansion.index.names[column]] = \
                in_need_of_expansion.index[index_number][column]
        # append new rows to dataframe
        start_dataframe = start_dataframe.append(rows, ignore_index=True)

    return start_dataframe


if __name__ == '__main__':
    master()
