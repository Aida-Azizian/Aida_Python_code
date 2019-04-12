class StringAlignmentTable:
    
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.table = []
        # builds the table
        for _ in range(len(self.s1)+1):
            column = []
            for _ in range(len(self.s2)+1):
                column.append(None) # i.e. empty cell
            self.table.append(column)
                
    def __str__(self):  
        ostr = "        "
        for i in range(0,len(self.s1)+1):
            if i > 0:
                # top row of letters
                ostr = ostr + "   " + self.s1[i-1]
        ostr = ostr + '\n'
        for j in range(0,len(self.s2)+1):
            if j > 0:
                # first column of letters
                ostr = ostr + "   " + self.s2[j-1]
            else:
                ostr = ostr + "    "
            for i in range(0,len(self.s1)+1):
                # ordinary cells, width 4, with
                # distance and operation letter
                ostr = ostr + ("    " +  \
                        str(self.table[i][j][0]) + \
                        self.table[i][j][1])[-4:]
            ostr = ostr + '\n'
        return ostr 

    def levenshtein(self):

        # The letter for first row is always d: delete
        for letter in range(0,len(self.s1)+1):
            self.table[letter][0] = [letter,'d']
        # The letter for first column is always i:insert
        for letter in range(0,len(self.s2)+1):
            self.table[0][letter] = [letter,'i']
            
        for j in range(1, len(self.s1)+1):
            for k in range(1, len(self.s2)+1):
                prevRow = self.table[j-1]
                currRow = self.table[j]
                if self.s1[j-1] == self.s2[k-1]:#match case
                    currRow[k] = prevRow[k-1][:]
                    currRow[k][1]="m"
                    
                else:#other conflict cases
                    if prevRow[k-1][0]<= currRow[k-1][0] and prevRow[k-1][0]<= prevRow[k][0]:#substitute case
                        currRow[k] = prevRow[k-1][:]
                        currRow[k][1] = "s" 
                     
                    elif currRow[k-1][0]< prevRow[k-1][0] and currRow[k-1][0]<= prevRow[k][0]:#insertion case
                        currRow[k] = currRow[k-1][:]
                        currRow[k][1] = "i" 
                   
                    else: #deletion case
                        currRow[k] = prevRow[k][:]
                        currRow[k][1] = "d"
                    currRow[k][0] = currRow[k][0] + 1

                    
        return self.table#return the final distance table 


#lt = StringAlignmentTable('Saturday','Sunday')
#lt.levenshtein()
#print(lt)
