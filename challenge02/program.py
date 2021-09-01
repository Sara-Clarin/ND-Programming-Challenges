''' HTML Linter Program
 Given a series of lines of HTML, determines if the tags are balanced
Sara Clarin
'''
#!/usr/bin/env/python3

import sys
from queue import LifoQueue

## FUNCTIONS

def determine_balance( line ):
    stack = LifoQueue()
    index_1 = 0
    index_2 = 0
    balanced = True
    n = len(line)

    while index_1 < n:
        char = line[index_1]    

        if char == "<":
            
            while line[index_2] != ">": 
                index_2 += 1

            tag = line[index_1 : index_2 + 1]   # pull anything of the form '< * >'

            if "</" not in tag:                  # place opening tags on stack
                stack.put(tag)

            else:                               # closing tag: compare with most recent stack element (opening tag)
                left_check = stack.get()
                left_check = left_check[0] + "/" + left_check[ 1:len(left_check)]
                if left_check != tag:
                    balanced = False
                    break;

           
        index_1 += 1
        index_2 = index_1

    if not stack.empty():
        balanced = False

    return balanced



## MAIN EXECUTION 
def main():
    
    for line in sys.stdin.readlines():
        balanced = determine_balance( line )

        if balanced:
            print("Balanced")
        else:
            print("Unbalanced")



if __name__ == "__main__":
    main()
