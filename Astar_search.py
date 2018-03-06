import random
import math
class AStarSearch():

	def __init__(self,size_x,size_y,src,dest,no_of_blocks):
		self.size_x = size_x
		self.size_y = size_y
		self.src = src
		self.dest = dest
		self.no_of_blocks = no_of_blocks
		self.x = src[0]
		self.y = src[0]
		self.createGrid()

	def createGrid(self):
		self.grid = [['-']*self.size_y for i in range(self.size_x)]
		for i in range(self.no_of_blocks):
			x = random.randint(0,self.size_x-1)
			y = random.randint(0,self.size_y-1)
			self.grid[x][y] = 'x'
		self.cost = [[random.randint(0,100) for j in range(self.size_y)]for i in range(self.size_x)]
		self.adj_pos = [(self.x-1,self.y),(self.x+1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y+1),(self.x-1,self.y+1),(self.x+1,self.y-1),(self.x-1,self.y-1)]

	def heuristic(self,cur,dest):
		return math.sqrt((cur[0]-dest[0])**2+(cur[1]-dest[1])**2)

	def aStar(self):
		self.visited = []
		self.distance = []
		self.queue = []
		self.distance = [1000 for i in range(self.size_x*self.size_y)]
		self.distance[self.src[0]*self.size_x+self.src[1]] = 0
		self.cameFrom = []
		self.fscore = [1000 for i in range(self.size_x*self.size_y)]
		self.queue.append(self.src)
		self.fscore[self.src[0]*self.size_x+self.src[1]] = self.heuristic(self.src,self.dest)
		while(len(self.queue)!=0):
			current = 2000
			if(len(self.visited)>=self.size_x*self.size_y):
				return False
			for i in self.fscore:
				if(current>i and self.fscore.index(i) not in self.visited):
					current = i
					index = self.fscore.index(i)
			current = index
			if(current == 0):
				cur_pos = (0,0)
			else:
				cur_pos = (current/self.size_x,current - (current/self.size_x)*self.size_x)
			if(cur_pos == self.dest):
				return True
			self.queue.remove(cur_pos)
			self.visited.append(current)
			self.x = cur_pos[0]
			self.y = cur_pos[1]
			flag = True
			for (i,j) in self.adj_pos:
				if(i>=0 and i<=self.size_x-1 and j>=0 and j<=self.size_y-1):
					if(self.grid[i][j]!='x' and (i*self.size_x+j) in self.visited):
						continue
					flag = True
					for (a,b) in self.queue:
						if(a==i and b==j):
							flag = False
							break

					if(flag):
						self.queue.append((i,j))
						flag = False
					dist = self.distance[current] + self.cost[i][j]
					if(dist>=self.distance[i*self.size_x+j]):
						continue
					self.cameFrom.append([(i,j),cur_pos])
					self.distance[i*self.size_x+j] = dist
					self.fscore[i*self.size_x+j] = dist + self.heuristic((i,j),self.dest)
					 
			self.adj_pos = [(self.x-1,self.y),(self.x+1,self.y),(self.x,self.y-1),(self.x,self.y+1),(self.x+1,self.y+1),(self.x-1,self.y+1),(self.x+1,self.y-1),(self.x-1,self.y-1)]    
		return False


obj = AStarSearch(20,20,(0,0),(26,30),15)
print obj.grid	
print(obj.aStar())










