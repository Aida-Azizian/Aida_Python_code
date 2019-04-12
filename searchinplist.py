from timeit import default_timer as timer
import collections
#List
dict2=[]
dict2=[line.strip() for line in open("dict2.txt", 'r')]
data=[]
data = [line.strip() for line in open("dict1.txt", 'r')]

#Deque
dict1D= collections.deque([])
dict2D= collections.deque([])
for line in open ( "dict1.txt", 'r'):
    dict1D.append(line)
for line in open ("dict2.txt",'r'):
    dict2D.append(line)


#Dictionary
dict1Dic={}
dict2Dic={}
for i in range(len(data)):
    dict1Dic[data[i]]=i

for i in range(len(dict2)):
    dict2Dic[dict2[i]]=i


def sequentionalS(data,target):
   for i in range(0,len(data)-1):
        if data[i]==target:
            return i
   return -1
#sequentionalS(data,target)


def binaryS(data,target):
    low=0
    high=len(data)-1
    for i in range(low,high):
        mid=(low+high)//2
        if data[mid] == target:
            return mid
        elif high-low<=1:
            if data[high]==target:
                return high
            else:
                return -1
        elif data[mid] > target:
            high = mid-1
        else:
            low = mid+1
    else:
        return -1
#binaryS(data,target)


#sequentinaltimelist
start = timer()
for d in dict2:
    sequentionalS(data,d)
end=timer()
print('Time for squentional search with list:',end-start)


#binarytimelist
start = timer()
for d in dict2:
    binaryS(data,d)
end=timer()
print('Time for binary search with list:',end-start)

#sequentinaltimedeque
start = timer()
for d in dict2D:
    sequentionalS(dict1D,d)
end=timer()
print('Time for squentional search with deque:',end-start)

#binarytimedeque
start = timer()
for d in dict2D:
    binaryS(dict1D,d)
end=timer()
print('Time for binary search with deque:',end-start)


#DictionarySearch
def DicSearch(data,target):
        if target in data:
            return data[target]
        else:
            return -1    


#Searchtimeictionary
start = timer()
for d in dict2Dic:
    DicSearch(dict1Dic,d)
end=timer()
print('Time for search with dictionary:',end-start)


