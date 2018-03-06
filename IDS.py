class graph_IDFS():

	def __init__(self,vertices):
		self.no_of_vertices = vertices
		self.adj_list = {i:[] for i in range(self.no_of_vertices)}

	def addEdge(self,u,v):
		self.adj_list[u].append(v)  

	def IDFS(self,src,dest,depth):
		for level in range(depth+1):
			if(self.DFS(src,dest,level)):
				return True
		return False

	def DFS(self,src,dest,level):
		print src
		if(src == dest):
			return True
		if(level<=0):
			return False
		for child in self.adj_list[src]:
			if(self.DFS(child,dest,level-1)):
				return True
				
		return False

g = graph_IDFS(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
src = 0
dest = 7
level = 2
print g.adj_list
if(g.IDFS(src,dest,level)):
	print "target vertex "+str(dest)+" is reachable"
else:
	print "target vertex "+str(dest)+" is not reachable"


		


