#! /usr/bin/env python
"""
Create a list of lists of names so that grading can be distributed amongst a number of graders. The names will be
randomly assigned to the lists. Takes as command line arguments the name of a pickled file of a list of names of
students to be graded, and the number of grading groups to form. Prints a list of names, one grading group per line,
to standard output.
"""
import sys, random, pickle


def splitNames(namelist, numGraders):
    '''
    Create a list of names to grade for each of a number of graders. Separate lists will be created for each grader.
    Assignment will be done sequentially after the namelist has been shuffled.
    :param namelist: A list of names of the people who need to be graded
    :param numGraders: The number of graders to whom names need to be assigned
    :return: A list of lists, one for each grader, each containing names to be graded
    '''
    glists = []
    for i in range(numGraders):
        glists.append([])
    i = 0
    random.shuffle(namelist)
    for n in namelist:
        glists[i].append(n)
        i = (i + 1)%numGraders
    return glists

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ('Usage makeGradingGroups classFileName numberOfGroups')
        sys.exit(0)
    classFName = sys.argv[1]
    numGraders = int(sys.argv[2])

    fin = open(classFName, 'rb')
    nameList = pickle.load(fin)
    fin.close()

    lists = splitNames(nameList, numGraders)
    for l in lists:
        l.sort(key = lambda n: n[n.rfind(' '):])
    for i in range(numGraders):
        print ('; '.join(lists[i]))
        print(' ')



