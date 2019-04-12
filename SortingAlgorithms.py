from sortarray import *
from timeit import default_timer as timer

def selectionSort(sa):
    for i in range(0, sa.getSize()-1):
        min = i
        for j in range(i+1, sa.getSize()):
            if sa.cmp(j,min) < 0:
                min = j
        sa.swap(i,min)


def Insertionsort(sa):
    for i in range(0, sa.getSize()):
        for j in range( i-1, -1, -1):
            if sa.cmp(j,j+1)> 0:
                sa.swap(j,j+1)
            else:
                break 


def bubblesort(sa):
    for passnum in range(sa.getSize()-1, 0, -1):
        for i in range(passnum):
            if sa.cmp(i,i+1)>0:
                        sa.swap(i,i+1)


def quicksort(sa):
    quicksort2(sa, 0, sa.getSize()-1)

def quicksort2(sa,low, hi):
    if low < hi:
        p=partition(sa,low,hi)
        quicksort2(sa, low, p-1)
        quicksort2(sa, p+1, hi)
        
def partition( sa, low, hi):
    mid=(hi+low)//2
    pivot=hi
    if sa.cmp(low,mid)<0:
        if sa.cmp(mid,hi)<0:
            pivot = mid
    elif sa.cmp(low,hi)<0:
        pivot = low
    pivotIndex=pivot 
    sa.swap(pivotIndex,low)
    border= low
    for i in range(low, hi+1):
        if sa.cmp(i,low)<0:
            border +=1
            sa.swap(i,border)
    sa.swap(low,border)
    return border


debug = False

sa = SortArray()
for size in range(10, 51, 10):
    print ("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print ("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print ("before: ")
            sa.printList()
        start = timer()
        quicksort(sa)
        end=timer()
        print('Time for this search method:',end-start)

        if debug:
            print ("after: ")
            sa.printList()

        sa.printInfo()
    
    print()
