"""
    +==========+==========-==========*==========-==========+==========+
    ||                      A SHUFFLING PROBLEM                      ||
    ||                                                               ||
    ||  Description: By computer simulation this program determines  ||
    ||              the probability of a deck of 52 cards having at  ||
    ||              least one unmoved card element after shuffling.  ||
    ||              (Answer: 0.63, rounded)                          ||
    ||                                                               ||
    +==========+==========-==========*==========-==========+==========+
"""

###########################<START OF PROGRAM>##########################

def printHeading():
    print('                         A SHUFFLING PROBLEM')
    print('                       (currently calculating...)')

#----------------------------------------------------------------------

def shuffleArrays():
    totalArrays = 0     # Arrays with at least one unmoved element
                        # after shuffling
    for trial in range(TRIAL_RUNS):
        array = list(range(LIST_SIZE))
        shuffle(array)

    for num in range(LIST_SIZE):
        if array[num] == num:
            totalArrays += 1
            break

    probability = round(totalArrays/TRIAL_RUNS, 2)
    return probability

#----------------------------------------------------------------------

def printResult(probability):
    print('     Result:', probability, 'is the probability of an array having at')
    print('     least one unmoved element after shuffling. This is based')
    print('     on a computer simulation with an array size =', LIST_SIZE, 'and')
    print('     ', TRIAL_RUNS, 'trial runs.')

#================<GLOBAL CONSTANTS AND GLOBAL IMPORTS>=================

from random import shuffle
TRIAL_RUNS  = 1000000
LIST_SIZE   =      52
assert LIST_SIZE > 1, 'LIST_SIZE must be greater than 1.'

#----------------------------------------------------------------------

def main():
    printHeading()
    probability = shuffleArrays()
    printResult(probability)

#----------------------------------------------------------------------

if __name__ == '__main__':
    from time import clock;     START_TIME = clock();   main()
    print('\n   '+'-    '*12)
    print('     PROGRAM RUN TIME:%6.2f'%(clock()-START_TIME), 'seconds.')

############################<END OF PROGRAM>###########################

