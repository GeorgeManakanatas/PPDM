import itertools


def master(enc_temp_file, lines, nums):
    selection = grab_columns(enc_temp_file, lines, nums)
    checklist = checklist_generate(lines, nums, selection)

    return


def grab_columns(enc_temp_file, lines, nums):
    """ gets the selected columns from the new encrypted file
    also initialises the temp and selection lists """
    f1 = open(enc_temp_file, "r")
    selection = []
    temp = []
    """ getting the designated columns from the file """
    for index_line in range(lines-1):
        line = f1.readline()
        words = line.split(",")
        for index_col in range(len(nums)):
            temp.append(words[nums[index_col]])
        selection.append(temp)
        temp = []
    f1.close()
    """ make the list of lists into list of tuples """
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
