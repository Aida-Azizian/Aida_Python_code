from weighteddigraph import WeightedDigraph as WeightedDigraph

wg = WeightedDigraph(['A','B','C','D','E','F','G'], \
                       [('A',4,'B'),('A',2,'C'),('B',5,'C'),('B',10,'D'), \
                        ('C',3,'E'),('E',4,'D'),('D',11,'F')])
    
def print_pair(p):
   print(p[0],p[1])
    
wg.cheapest_path('A','A')

wg.cheapest_path('A','F')

wg.cheapest_path('B','D')

wg.cheapest_path('E','C')



