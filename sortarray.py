from random import randint

class SortArray:

    def __init__(self, size=100, method="shuffle"):
        self.method = method
        self.size = size
        self.data = list(range(1,self.size+1))
        self.swaps = 0;
        self.comps = 0;
        self.reset()
        
    def shuffleData(self):
        for i in range(self.size):
            r = randint(0,self.size-1)
            self.swap(i,r)

    def miniShuffleData(self):
        for i in range(self.size):
            r = randint(i-3,i+3)
            if r >= 0 and r < self.size:
                self.swap(i,r)

    def reverseData(self):
        self.data = list(range(self.size, 0,-1))

    def getSize(self):
        return self.size

    def swap(self, i, j):
        self.swaps += 1
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def cmp(self, i, j):
        self.comps += 1
        return self.data[i]-self.data[j]

    def reset(self, size=100, method="shuffle"):
        if size != self.size:
            self.size = size
            self.data = list(range(1,self.size+1))

        self.method = method
        if self.method == "shuffle":
            self.shuffleData();
        elif self.method == "miniShuffle":
            self.miniShuffleData()
        elif self.method == "reverse":
            self.reverseData()
        else:
            raise TypeError("no list organisation method: "+self.method)
    
        self.swaps = 0;
        self.comps = 0;

    def getStats(self):
        return (self.swaps, self.comps)

    def printList(self):
        for i in range(self.size):
            print (self.data[i], end=" ")
        print ()

    def printInfo(self):
        print ("swaps: ", self.swaps, "comps: ", self.comps)
         


            
