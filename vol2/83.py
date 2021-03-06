from urllib2 import urlopen

import time
t0 = time.time()

f = urlopen('https://projecteuler.net/project/resources/p083_matrix.txt')
grid = {}
counter = 1
for line in f:
   temp = line.replace('\n','')
   temp = temp.split(',')
   for a in range(len(temp)):
       grid[(counter,a+1)] = int(temp[a])
   counter += 1
rows = 80
cols = 80

def findNeighbors(vertex):
   i, j = vertex[0], vertex[1]
   output = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]  # all neighbors
   remove = []
   for v in output:
      if v[0] < 1 or v[0] > rows or v[1] < 1 or v[1] > cols:  
         remove.append(v)
   final = [x for x in output if not x in remove]
   return final
      
# Let's implement Dijkstra's algo from Wikipedia
def dka(graph, source):    # graph will be our grid, source will be (1,1)
   dist = {}
   for v in graph:
      dist[v] = float("inf")
   dist[source] = graph[source]
   Q = dist.copy()   #make a copy of graph, as a hash
   length = len(Q)
   while length > 0:
      u = min(Q, key=Q.get)
      if dist[u] == float("inf"):
         break
      if u == (rows, cols):
         break
      del Q[u]
      length -= 1
      n = findNeighbors((u))
      neighbors = [x for x in n if x in Q]
      for v in neighbors:
         alt = dist[u] + grid[v]
         if alt < dist[v]:
            dist[v] = alt
            Q[v] = alt
   return dist

answerGrid = dka(grid,(1,1))

print "The answer is ", answerGrid[(rows,cols)]
t1= time.time()
total = t1-t0
print total, "seconds"