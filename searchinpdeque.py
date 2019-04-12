from timeit import default_timer as timer
import collections
dict1D = collections.deque([])
dict2D = collections.deque([])

## Read the words in dict1.txt and dict2.txt and append them into a deque which I created above.
for line in open("dict1.txt", 'r'):
    dict1D.append(line)   
for line in open("dict2.txt", 'r'):
    dict2D.append(line)


## Implementing Sequentional and Binary search algorithms 
def sequentionalS(dict1D,target):
   for i in range(len(dict1D)):
       if dict1D[i]==target:
         return i
   return -1

def binaryS(dict1D,target):
    low = 0
    high = len(dict1D)-1
    index=-1
    for i in range(low,high):
        mid = (low + high)//2
        if dict1D[mid] == target:
            index=mid
        elif dict1D[mid] > target:
            high = mid-1
        else:
            low = mid
    return index


## measuring the actual time they take to run
start = timer()
for d in dict2D:
    sequentionalS(dict1D,d)
end=timer()
print('Time for Squentional Search with deque:',end-start)

start = timer()
for d in dict2D:
    binaryS(dict1D,d)
end=timer()
print('Time for Binary Search with deque:',end-start)
