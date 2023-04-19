#author : sydney muganda~mgnsyd001

import copy 



pages="701203042303120"
pages=[5, 5, 7, 3, 6, 4, 0, 4, 8, 2, 3, 5, 0, 2, 2, 1, 4, 0, 7, 9, 1, 4, 8, 1, 5, 1, 9, 1, 7, 8, 7, 1, 8, 8, 2, 0, 6, 4, 8, 5, 4, 4, 6, 0, 5, 2, 3, 8, 5, 5, 6, 4, 5, 6, 8, 1, 2, 5, 6, 2, 6, 3, 1, 7, 5, 6, 5, 1, 7, 0, 0, 7, 5, 5, 9, 6, 1, 2, 2, 1, 7, 0, 3, 1, 7, 1, 8, 2, 1, 9, 4, 9, 8, 4, 5, 1, 8, 4, 0, 4]
def FIFO(frames,pages):
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
        if pointer==len(pages)-1:
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

 




if __name__ == "__main__":
    main()