"""
Read two csv files, and compare them based on the first entry in each line. Prints out those entries that can be found
in the first but not the second, and in the second but not the first.
"""
import csv, sys


def readFile(f):
    """
    Read a csv file, and create a set of the first item in the entries. Return a set of
    entries in the list
    :param f: An open csv file
    :return: A set of the entries in the list
    """
    ret_set = set()
    for l in f:
        ret_set.add(l[0])
    return ret_set


def compareFiles(f1, f2):
    """
    Compare the first entry of the open files and return lists of those entries that are in one list but not the other
    :param f1: A csv file, the first entry of which is to be compared to the first entry of the other file
    :param f2: A csv file, the first entry of which is to be compared to the first entry of the other file
    :return: two lists; one containing any entries in the first file that are not in the second, and the second containing
    entries in the second file that are not in the first
    """
    set1 = readFile(csv.reader(f1))
    set2 = readFile(csv.reader(f2))
    missing_from_2 = list(set1 - set2)
    missing_from_1 = list(set2 - set1)

    return missing_from_1, missing_from_2


def print_missing(missing_list, n1, n2):
    """
    Print the entries in one file that are not present in the other
    :param missing_list: A list of the entries in one file that are not in the other
    :param n1:  The name of the file containing entries not in the other file
    :param name2: The name of the file in which entries of the first file are missing
    :return: None
    """
    if len(missing_list) > 0:
        print('items occurring in ', n2, 'but not in', n1)
        print("; ".join(missing_list))
    else:
        print('All items in', n2, 'occur in', n1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage compareLists file1.csv file2.csv')
        sys.exit(1)

    filen1 = sys.argv[1]
    filen2 = sys.argv[2]
    file1 = open(filen1, 'r')
    file2 = open(filen2, 'r')

    missing_from_1, missing_from_2 = compareFiles(file1, file2)
    print_missing(missing_from_1, filen1, filen2)
    print_missing(missing_from_2, filen2, filen1)

    file1.close()
    file2.close()
