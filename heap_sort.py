#Program to write heap sort

def heapify(input):
    return input



last = len(input)-1
first = 0
def heap_sort(input,last,first):
    while(last>=first):
        temp = input[0]
        input[0] = input[last]
        input[last] = temp
        last-=1
        input = heapify(input) #this will create a copy

    return input
        
    


