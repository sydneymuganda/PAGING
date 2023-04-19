# Author: [SYDNEY MUGANDA]
# Student Number: [YOUR STUDENT NUMBER]

import sys
import random

# Generate random page-reference string
pages = [random.randint(0, 9) for i in range(100)]
pages="701203042303120"
pages="701203042303212017"
# Implement FIFO algorithm
def FIFO(frames, pages):
    ''''
    This function implements the FIFO page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults

    '''
    count = 0
    queue = []
    for page in pages:
        if page not in queue:
            if len(queue) < frames:
                queue.append(page)
            else:
                queue.pop(0)
                queue.append(page)
            count += 1
    return count

# Implement LRU algorithm
def LRU(frames, pages):
    '''
    This function implements the LRU page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults
    '''
    count = 0
    stack = []
    for page in pages:
        if page not in stack:
            if len(stack) < frames:
                stack.append(page)
            else:
                stack.pop(0)
                stack.append(page)
            count += 1
        else:
            stack.remove(page)
            stack.append(page)
    return count

# Implement OPT algorithm
def OPT(frames, pages):
    '''
    This function implements the Optimal page replacement algorithm

    :param frames: the frames used for RAM 
    :param pages: contains a list or string of entered pages
    :return: number of faults
    '''
    count = 0
    queue = []
    for page in pages:
        if page not in queue:
            if len(queue) < frames:
                queue.append(page)
            else:
                index = -1
                farthest = -1
                for i in range(len(queue)):
                    try:
                        if pages[pages.index(queue[i]):].index(queue[i]) > farthest:
                            farthest = pages[pages.index(queue[i]):].index(queue[i])
                            index = i
                    except:
                        index = i
                        break
                queue[index] = page
            count += 1
    return count

# Main function
def main():
    size = int(sys.argv[1])
    print('FIFO', FIFO(size, pages), 'page faults.')
    print('LRU', LRU(size, pages), 'page faults.')
    print('OPT', OPT(size, pages), 'page faults.')
    print(pages)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python paging.py [number of page frames]')
    else:
        main()
