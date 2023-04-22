"""
This script creates the application 
that implements the FIFO, LRU, and optimal page replacement algorithms 

Author: Sydney Muganda (mgnsyd001@myuct.ac.za)
Date: 2nd April 2023
"""

import copy 
import sys
import random


pages="701203042303120"
pages="701203042303212017"
#pages="23456712340987"

#pages=[4, 8, 8, 6, 8, 9, 2, 5, 9, 6, 6, 0, 7, 0, 0, 8, 4, 7, 0, 9, 5, 5, 1, 7, 2, 8, 8, 7, 5, 4, 7, 1, 8, 6, 0, 3, 9, 1, 2, 3, 5, 1, 0, 4, 7, 1, 4, 5, 9, 5, 5, 8, 1, 8, 8, 3, 0, 2, 0, 6, 7, 9, 4, 9, 1, 7, 7, 7, 4, 7, 7, 5, 9, 4, 2, 4, 5, 1, 5, 9, 7, 5, 2, 2, 8, 3, 5, 1, 3, 9, 5, 0, 4, 5, 5, 3, 9, 5, 2, 5]
def FIFO(frames,pages):
    ''''
    This function implements the FIFO page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults

    '''
    stack=[] #holds the memory
    fault=0 #number of faults
    page_list=[] #converts string input of pages to a list for testing

    if not (type(pages) is list):#converts string input of pages to a list for testing
        for char in pages:
            page_list.append(char)
        pages=page_list
       


    for entry in pages:#FIFO IMPLEMENTATION
        if entry in stack:
            continue

        if len(stack)<frames:
            
            stack.append(entry)
            fault=fault+1 
        else:
            stack.pop(0)
            stack.append(entry)
            fault=fault+1 




    return fault
def LRU(frames,pages):
    '''
    This function implements the LRU page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults
    '''
    stack=[]#holds the memory
    fault=0#number of faults
    page_list=[]#converts string input of pages to a list for testing

    

    if not (type(pages) is list):#converts string input of pages to a list for testing
        for char in pages:
            page_list.append(char)
        pages=page_list

    pointer=0
    for entry in pages:
        if entry in stack:
            pointer=pointer+1
            continue

        if len(stack)<frames:
            
            stack.append(entry)
            fault=fault+1 
        else:
            least=leat_used(stack[:],pages[:pointer])
            
            stack[least]=entry
            fault=fault+1   
        pointer=pointer+1

    return fault    

def leat_used(stack:list,subpage:list):
    ''''
    This function finds the least used paage entry in stack to treplace

    :param stack: the frames used for RAM 
    :param subpage: contains a list or string of entered pages
    :return: index of least used pagwe entry

    '''
    r_subpage=list(reversed(subpage)) #reverses subpage to find least used
    stack_copy=copy.copy(stack)#makes copy of stack
    for p in r_subpage:
        if len(stack)==1:break

        if p in stack: #remove most reently used page entry in stack till only the least recently used is left
           stack.remove(p)

        

    return stack_copy.index(stack[0])    #return index of least recently used in stack    


def OPT(frames,pages):  
    '''
    This function implements the Optimal page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults
    '''
    stack=[]
    fault=0
    page_list=[]#converts string input of pages to a list for testing

    

    if not (type(pages) is list):#converts string input of pages to a list for testing
        for char in pages:
            page_list.append(char)
        pages=page_list

    pointer=0
    for entry in pages:
        
        if entry in stack:
            pointer=pointer+1
            continue
        if pointer>=len(pages)-1:
            fault=fault+1
            break

        if len(stack)<frames:
            
            stack.append(entry)
            fault=fault+1 
        else:
            last=last_used(stack[:],pages[pointer+1:])
            
            stack[last]=entry
            fault=fault+1   
        pointer=pointer+1

    return fault    
def last_used(stack:list,subpage:list):
    ''''
    This function finds the most used paage entry in stack to treplace

    :param stack: the frames used for RAM 
    :param subpage: contains a list or string of entered pages
    :return: index of most used pagwe entry

    '''
    stack_copy=copy.copy(stack)

    for value in stack:#if value in stack not in pages then it is never used thus returned
        if value in subpage:
            pass
        else:
            return stack.index(value)

    for p in subpage:#remove most likely to be used page entry in stack till only the last  used is left
        if len(stack)==1:break

        if p in stack:
           stack.remove(p)

        

    return stack_copy.index(stack[0])   #return index of last likely  used in stack


def main():
    size = int(sys.argv[1])
    reference_size=int(input("enter size of reference string:\n"))
    pages=[random.randint(0, 9) for i in range(reference_size)]
    print()
    print('FIFO', FIFO(size, pages), 'page faults.')
    print('LRU', LRU(size, pages), 'page faults.')
    print('OPT', OPT(size, pages), 'page faults.')
    print()
    print("The entered string:")
    print(pages)
    

 




if __name__ == "__main__":
    main()