graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : ['G','H'],
  'G' : ['H'],
  'H' : []
  }

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
q=Queue()

def bfs(graph,n):
  print(q.isEmpty())
  visited=[]
  
  visited.append(n)
  q.enqueue(n) #Adding the Node to the queue
  
  while q:
    v=q.dequeue()
    print (v, end = " ") 
    for neighbour in graph[v]:
      if neighbour not in visited:
        q.enqueue(neighbour)
        visited.append(neighbour)

bfs(graph,'B')
