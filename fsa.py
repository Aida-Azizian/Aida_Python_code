class FSA():
    def __init__(self, states, alphabet, init, accept, transitions):
        self.states= states
        self.alphabet= alphabet
        self.init= init
        self.accept= accept
        self.transitions=transitions
        self.dictransition={}
        for state in self.states:
            self.dictransition[state]=[]
        for i in range(len(transitions)): # create a dictionary with list 
            if transitions[i][0] not in self.dictransition:
                self.dictransition[transitions[i][0]]=[(transitions[i][1],transitions[i][2])]
            else:
                self.dictransition[transitions[i][0]].append((transitions[i][1],transitions[i][2]))


    def accepts(self,string):
        curr=self.init
        for l in string:
            letter_here=False
            for tuple_id in self.dictransition[curr]:
                if l == tuple_id[0]:
                    letter_here=True
                    curr=tuple_id[1]
                    break
            if not letter_here:
                return False
        if curr in self.accept:
            return True
        else:
            return False




    def generate(self,n):
        acceptedStrings=[]
        currentStates=[('', self.init)]
        nextStates=[]
        for i in range(n-1):
            nextStates=[]
            for tuple_id in currentStates:
                for string,next_state in self.dictransition[tuple_id[1]]:
                    testString=tuple_id[0]+ string
                    if self.accepts(testString):
                        acceptedStrings.append(testString)
                    nextStates.append((testString,next_state))
            currentStates=nextStates
        return acceptedStrings
            
        
fsaApa = FSA(['s0','s1','s2','s3','s4','s5','s6','s7','s8'], \
  ['a','n','o','p','r','s'], 's0', ['s3','s4','s5','s7'], \
  [('s0','a','s1'), ('s1','p','s2'), ('s2','a','s3'), ('s2','o','s6'), \
   ('s3','n','s5'), ('s3','s','s4'),('s5','s','s4'),('s6','r','s7'), \
   ('s7','n','s8'),('s7','s','s4'),('s8','a','s5')])
        
print(fsaApa.dictransition)
print(fsaApa.generate(100))

    


