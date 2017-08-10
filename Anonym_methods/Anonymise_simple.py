import csv
import random
import Kanon_file


def master(enc_temp_file, file_name, lines, nums, kmin):
    """ perform simple  """
    """ import the column selection """
    selectcol = Kanon_file.grab_columns(enc_temp_file, lines, nums)
    """ import the checklist """
    checklist = Kanon_file.checklist_generate(lines, nums, selectcol)
    """ bringing in newdb the encrypted DB """
    newdb = newdb_listoflists(enc_temp_file)

    """ reading the first generated combination of the columns """
    for i in range(len(checklist)):
            kanonDB = []
            val3 = checklist[i]  # reads a line from the checklist start at top and repeat for all the rest
            instances = []  # initialising the instances table for this combo
            totline = 0  # initialising linecouter
            for j in range(len(selectcol)):
                val2 = selectcol[j]  # reads a line from the actual combinations in the DB (selectedcolumns)
                if val3 == val2:  # if the two match
                    instances.append(totline)  # then we save the line number
                totline += + 1  # increases linecounter
            suppcount = len(instances)  # we find the actual number of matches

            """ if the number of matches is greater or equal to kmin just copy the lines """
            if suppcount >= kmin:
                for a in range(len(instances)):
                    kanonDB.insert(0, newdb[instances[a]])
            """ if the number of matches is less than kmin still copy the lines found """
            if suppcount < kmin:
                for a in range(len(instances)):
                    kanonDB.insert(0, newdb[instances[a]])
            """ if the difference of kmin and lines found > than 0 then add the required
             number of lines to reach required minimum """
            if kmin-suppcount > 0:
                for a in range(kmin-suppcount):
                    ranval = random.randint(0, len(newdb)-1)
                    ranline = newdb[ranval]
                    for b in range(len(val3)):
                        ranline[nums[b]] = val3[b]
                    kanonDB.insert(0, ranline)

            with open(file_name, "a") as f1:
                mywriter = csv.writer(f1, delimiter=',', quotechar='|')
                for line in range(len(kanonDB)):
                    mywriter.writerow(kanonDB[line])
                f1.close()

    return


def newdb_listoflists(enc_temp_file):
    """ reading the data from the file containing the encrypted form of the DB (perhaps pass direct?) """
    newdb = []
    with open(enc_temp_file, "r") as f1:
        myreader = csv.reader(f1, delimiter=',')
        for row in myreader:
            vari = row
            newdb.append(vari)
        f1.close()
    return newdb
