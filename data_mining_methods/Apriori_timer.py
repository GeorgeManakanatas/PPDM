'''
Description     : Simple Python implementation of the Apriori Algorith
'''
import csv
import timeit
from itertools import chain, combinations
from collections import defaultdict
from itertools import islice


def master(start_dataframe, file_name, min_supp, min_conf, logger):
    '''
    Apriori data mingi implementation

    Arguments:
        file_name(str): the name of the file containing the data
        min_supp(float): list of column numbers for the attributes to mask
        min_conf(float): the way the attributes should be masked
        logger: custom logging method

    Returns:
        Nothing output is in a file dataFromList
    '''
    total_apriori_start = timeit.default_timer()
    # inFile_old = dataFromFile(file_name)
    inList = dataFromList(start_dataframe.to_csv(header=None, index=False).strip('\n').split('\n'))
    minSupport = min_supp
    minConfidence = min_conf
    items, rules = runApriori(inList, minSupport, minConfidence, logger)

    # printResults(items, rules)
    with open("data/output/Apriori_items.txt", "w") as f1:
                mywriter = csv.writer(f1, delimiter=',')
                for i in range(len(items)):
                    mywriter.writerow(items[i])
                f1.close()
    with open("data/output/Apriori_rules.txt", "w") as f1:
                mywriter = csv.writer(f1, delimiter=',')
                for i in range(len(rules)):
                    mywriter.writerow(rules[i])
                f1.close()
    # print ("results with min support:", minSupport, "and min confidence:", minConfidence)

    total_apriori_stop = timeit.default_timer()
    # logging the excecution time
    logger.debug(" Total apriori time is:" +
                 str(total_apriori_stop-total_apriori_start))
    return


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet, logger):
        """calculates the support for items in the itemSet and returns a subset
       of the itemSet each of whose elements satisfies the minimum support"""

        logger.debug('in returnItemsWithMinSupport')
        _itemSet = set()
        localSet = defaultdict(int)

        for item in itemSet:
                for transaction in transactionList:
                        if item.issubset(transaction):
                                freqSet[item] += 1
                                localSet[item] += 1

        for item, count in localSet.items():
                support = float(count)/len(transactionList)

                if support >= minSupport:
                        _itemSet.add(item)

        return _itemSet


def joinSet(itemSet, length, logger):
        """Join a set with itself and returns the n-element itemsets"""
        logger.debug('in joinSet')
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator, logger):
    logger.debug('in getItemSetTransactionList')
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))              # Generate 1-itemSets
    return itemSet, transactionList


def runApriori(data_iter, minSupport, minConfidence, logger):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    logger.debug('In run apriori')
    itemSet, transactionList = getItemSetTransactionList(data_iter, logger)

    freqSet = defaultdict(int)
    logger.debug('freqSet: '+str(freqSet))
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules
    logger.debug('Sending to returnItemsWithMinSupport')
    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet, logger)
    logger.debug('Before loop')
    currentLSet = oneCSet
    logger.debug('currentLSet: '+str(currentLSet))
    k = 2
    while(currentLSet != set([])):
        logger.debug('in loop')
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k, logger)
        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet, logger)
        currentLSet = currentCSet
        k = k + 1
    logger.debug('Before getSuppot')
    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])
    logger.debug('Before retrules')
    toRetRules = []
#    for key, value in largeSet.items()[1:]:
    for key, value in islice(largeSet.items(), 1, None):
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))
    return toRetItems, toRetRules


def printResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    for item, support in items:
        print ("item: %s , %.3f" % (str(item), support))
    print ("\n------------------------ RULES:")
    for rule, confidence in rules:
        pre, post = rule
        print ("Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence))


def dataFromFile(fname):
        """Function which reads from the file and yields a generator"""
        file_iter = open(fname, 'rU')
        for line in file_iter:
            line = line.strip().rstrip(',')                         # Remove trailing comma
            record = frozenset(line.split(','))
            yield record

def dataFromList(data_list):
        """Function which reads from the list and yields a generator"""
        for line in data_list:                       # Remove trailing comma
            record = frozenset(line.split(','))
            yield record

if __name__ == '__main__':
    master()