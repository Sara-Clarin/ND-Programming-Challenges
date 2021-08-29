# Python program to find the number of occurrences of one word within another
# 
#By Sara Clarin

import sys

## FUNCTIONS ##

def convert_to_list( string ):
    return [ char for char in string]


def get_num_occurrences( word, substring):
    occurrences = 0
    word_ind = 0
    end_of_word = len(substring)
    done = False

    while not done:

        for ch in substring:
            try:                 #if character in large word, remove from list
                word.remove(ch)
                word_ind += 1

                if word_ind == end_of_word:
                    occurrences += 1
                    word_ind = 0

            except ValueError:     # if any character no longer in list, quit
                done = True

    print(occurrences)

## MAIN EXECUTION ##

def main():

    for line in sys.stdin.readlines():
        s1, s2 = line.split()
        word = convert_to_list(s1)
        substring = convert_to_list(s2)

        get_num_occurrences( word, substring)

if __name__ == "__main__":
    main()        
