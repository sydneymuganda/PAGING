#author : sydney muganda~mgnsyd001


pages="701203042303120"
pages=[5, 1, 6, 0, 8, 8, 2, 3, 7, 7, 0, 3, 5, 4, 1, 0, 4, 9, 8, 2, 1, 9, 2, 7, 5, 4, 1, 8, 5, 6, 4, 4, 4, 5, 2, 9, 4, 8, 2, 1, 5, 8, 5, 5, 7, 3, 0, 2, 7, 1, 8, 6, 8, 6, 9, 7, 0, 0, 3, 5, 7, 0, 4, 1, 9, 6, 0, 9, 2, 5, 1, 9, 8, 7, 2, 5, 2, 8, 3, 1, 5, 5, 0, 7, 7, 4, 0, 3, 4, 4, 1, 5, 0, 9, 9, 1, 1, 7, 0, 6]
def FIFO(frames,pages):
    stack=[]
    fault=0
    page_list=[]

    if not (type(pages) is list):
        for char in pages:
            page_list.append(char)
        pages=page_list
        print(pages)
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


def main():
 #print(pages.split())
 print(FIFO(3,pages))




if __name__ == "__main__":
    main()