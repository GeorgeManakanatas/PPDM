import itertools
import random
import csv


def master(dataWithMasking, file_name, lines, nums, kmin):
    # should be a list of possible options later
    anonymizedAndMaskedData = kAnonymitySimplistic(dataWithMasking, file_name, lines, nums, kmin)

    return anonymizedAndMaskedData

def grab_columns(dataWithMasking, lines, nums):
    # gets the selected columns from the new encrypted file #
    # also initialises the temp and selection lists #
    selection = []
    temp = []
    # getting the designated columns from the file #
    for index_line in range(lines-1):
        words = dataWithMasking[index_line]
        for index_col in range(len(nums)):
            # print('index_col ',index_col)
            temp.append(words[nums[index_col]])
        selection.append(temp)
        temp = []
    # make the list of lists into list of tuples #
    selection_tuples = [tuple(l) for l in selection]
    
    return selection_tuples


def checklist_generate(lines, nums, selection):

    temp = []
    checklist = []
    for index_col in range(len(nums)):
        for index_line in range(lines-1):
            temp.append(selection[index_line][index_col])
        temp = list(set(temp))
        checklist.append(temp)
        temp = []

    final_list = []
    for temp in itertools.product(*checklist):
        final_list.append(temp)

    return final_list


def kAnonymitySimplistic(dataWithMasking, file_name, lines, nums, kmin):
    # perform simple  #
    # import the column selection #
    selectcol = grab_columns(dataWithMasking, lines, nums)
    with open("temp/selectCol.txt", "w") as f1:
                mywriter = csv.writer(f1, delimiter=',', quotechar='|')
                for line in range(len(selectcol)-1):
                    mywriter.writerow(selectcol[line])
                f1.close()
    
    # import the checklist #
    checklist = checklist_generate(lines, nums, selectcol)
    with open("temp/checklist.txt", "w") as f1:
                mywriter = csv.writer(f1, delimiter=',', quotechar='|')
                for line in range(len(checklist)-1):
                    mywriter.writerow(checklist[line])
                f1.close()
     
    print('\n lines ',lines,'\n dataWithMasking length ',len(dataWithMasking),'\n len(checklist) ',len(checklist))

    # reading the first generated combination of the columns #
    for i in range(len(checklist)):
            appendCounter = lines
            val3 = checklist[i]  # reads a line from the checklist start at top and repeat for all the rest
            instances = []  # initialising the instances table for this combo
            totline = 0  # initialising linecouter
            for j in range(len(selectcol)):
                val2 = selectcol[j]  # reads a line from the actual combinations in the DB (selectedcolumns)
                if val3 == val2:  # if the two match
                    instances.append(totline)  # then we save the line number
                totline += + 1  # increases linecounter
            suppcount = len(instances)  # we find the actual number of matches

            # if the number of matches is less than kmin add the required number of lines to reach required minimum """
            if suppcount < kmin:
                for a in range(kmin-suppcount):
                    appendCounter = appendCounter + 1
                    ranval = random.randint(0, len(dataWithMasking))
                    ranline = dataWithMasking[ranval]
                    for b in range(len(val3)):
                        ranline[nums[b]] = val3[b]
                    dataWithMasking[appendCounter] = ranline
            # create 
            with open(file_name, "a") as f1:
                mywriter = csv.writer(f1, delimiter=',', quotechar='|')
                for line in range(len(dataWithMasking)-1):
                    mywriter.writerow(dataWithMasking[line])
                f1.close()
    
    return dataWithMasking


if __name__ == '__main__':
    master()
