"""
This script creates the application 
that implements the F IFO, LRU, and optimal page replacement algorithms 

Author: Sydney Muganda (mgnsyd001@myuct.ac.za)
Date: 2nd April 2023
"""

import copy 



pages="701203042303120"
pages="701203042303212017"
pages="5760717201710"
#pages=[4, 8, 8, 6, 8, 9, 2, 5, 9, 6, 6, 0, 7, 0, 0, 8, 4, 7, 0, 9, 5, 5, 1, 7, 2, 8, 8, 7, 5, 4, 7, 1, 8, 6, 0, 3, 9, 1, 2, 3, 5, 1, 0, 4, 7, 1, 4, 5, 9, 5, 5, 8, 1, 8, 8, 3, 0, 2, 0, 6, 7, 9, 4, 9, 1, 7, 7, 7, 4, 7, 7, 5, 9, 4, 2, 4, 5, 1, 5, 9, 7, 5, 2, 2, 8, 3, 5, 1, 3, 9, 5, 0, 4, 5, 5, 3, 9, 5, 2, 5]
def FIFO(frames,pages):
    ''''
    This function implements the FIFO page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults

    '''
    stack=[]
    fault=0
    page_list=[]

    if not (type(pages) is list):
        for char in pages:
            page_list.append(char)
        pages=page_list
       


    for entry in pages:
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
    stack=[]
    fault=0
    page_list=[]

    

    if not (type(pages) is list):
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
            #stack.remove(least) 
            #stack.append(entry)
            stack[least]=entry
            fault=fault+1   
        pointer=pointer+1

    return fault    

def leat_used(stack:list,subpage:list):
    least_used_value=len(subpage)
    r_subpage=list(reversed(subpage))
    stack_copy=copy.copy(stack)
    for p in r_subpage:
        if len(stack)==1:break

        if p in stack:
           stack.remove(p)

        

    return stack_copy.index(stack[0])        


def OPT(frames,pages):  
    '''
    This function implements the Optimal page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults
    '''
    stack=[]
    fault=0
    page_list=[]

    

    if not (type(pages) is list):
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
            #stack.remove(least) 
            #stack.append(entry)
            stack[last]=entry
            fault=fault+1   
        pointer=pointer+1

    return fault    
def last_used(stack:list,subpage:list):
    
    stack_copy=copy.copy(stack)

    for value in stack:
        if value in subpage:
            pass
        else:
            return stack.index(value)

    for p in subpage:
        if len(stack)==1:break

        if p in stack:
           stack.remove(p)

        

    return stack_copy.index(stack[0])  


def main():
    #print(pages.split())
    print(FIFO(3,pages))
    print(LRU(3,pages))
    print(OPT(3,pages))

    print("FIFO:")

    print("Test with FIFO(3,321321). Expected output: 3 actual output:",FIFO(3,"321321"))
    print("Test with FIFO(3,123123). Expected output: 3 actual output:",FIFO(3,"123123"))
    print("Test with FIFO(1,111111). Expected output: 1 actual output:",FIFO(1,"111111"))
    print()
    print("LRU:")
    print()
    print("Test with LRU(3,321321). Expected output: 3 actual output:",LRU(3,"321321"))
    print("Test with LRU(3,123123). Expected output: 3 actual output:",LRU(3,"123123"))
    print("Test with LRU(1,111111). Expected output: 1 actual output:",LRU(1,"111111"))
    print("OPT:")
    print()
    print("Test with OPT(3,321321). Expected output: 2 actual output:",OPT(3,"321321"))
    print("Test with OPT(3,123123). Expected output: 2 actual output:",OPT(3,"123123"))
    print("Test with OPT(1,111111). Expected output: 1 actual output:",OPT(1,"111111"))

 




if __name__ == "__main__":
    main()