import sys,getopt
from random import randint
from operator import add
from math import log10,floor
from numpy import genfromtxt
class Node:
	def __init__(self,data,label):
		self.data = data
		self.label = label
		self.left = None
		self.right = None

	def updateleft(self,data,label):
		self.left = Node(data,label)

	def updateright(self,data,label):
		self.right = Node(data,label)


# Computing centroid for clusters
def kmus(k,n,clusters,input_data):
	listofClusters = []
	for i in range(k):
		listofClusters.append([])
	for i in range(n):
		listofClusters[clusters[i]].append(i)
	kmu = []
	for i in range(k):
		if (len(listofClusters[i])>0):
			temp = listofClusters[i][0]
			first = input_data[temp] 
			for j in range(1,len(listofClusters[i])):
				second = input_data[listofClusters[i][j]]
				first = list(map(add,first,second))
			for j in range(len(first)):
				first[j] = first[j]/len(listofClusters[i])
			kmu.append(first)
	return kmu

# Computing norm, ||a-b||
def norm(a,b):
	x=0
	for i in range(len(a)):
		x+=(a[i]-b[i])**2
	x=x**0.5
	return x

D = 0
k = 0
n=0

# Parsing arguments
try:
  opts, args = getopt.getopt(sys.argv[1:],"hD:k:n:")
except getopt.GetoptError:
  print('Solution.py -D <dimension> -k <Number of clusters> -n <Number of data points>')
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print('Solution.py -D <dimension> -k <Number of clusters> -n <Number of data points>')
     sys.exit()
  elif opt in ("-D"):
     D = int(arg)
  elif opt in ("-k"):
     k = int(arg)
  elif opt in ("-n"):
     n = int(arg)

# Taking input data

#file = open('/home/lavish/Documents/P1_data/P1_data_train.csv','r')
# input_data = [[float(num) for num in line.split()] for line in file ]
input_data = genfromtxt('P1_data_train.csv',delimiter =',')
labelofdata = genfromtxt('P1_labels_train.csv',delimiter =',')
clusters = []
# Random Initialization
def checkEqual(iterator):
   return len(set(iterator)) <= 1

def randomclusters(n,k):
	clusters = []
	for i in range(n):
		clusters.append(randint(0,k-1))
	while(checkEqual(clusters)==True):
		clusters=[]
		for i in range(n):
			clusters.append(randint(0,k-1))
	return clusters


def iterating(k,n,clusters,input_data):
	mu = kmus(k,n,clusters,input_data)
	# print(clusters)
	#Iteration for mu update
	for d in range(100):	
		newclusters = [0]*n
		for i in range(n):
			mini = norm(input_data[i],mu[0])
			cluster_no = 0
			for j in range(1,k):
				if(len(mu)>j):
					temp = norm(input_data[i],mu[j])
					if temp< mini:
						cluster_no = j
						mini = temp
			newclusters[i] = cluster_no

		if(norm(clusters,newclusters)==0):	
			break

		clusters = newclusters
		mu = kmus(k,n,clusters,input_data)
	return clusters
# print(clusters)
def round1(x):
	return round(x,3)

def Nodesplit(newnode,k):
	n = len(newnode.data)
#	print(k)
	clusters = randomclusters(n,k)

	clusters = iterating(k,n,clusters,newnode.data)

	c=0
	data = newnode.data
	l = []
	llabel = []
	r = []
	rlabel = []
	for i in range(len(clusters)):
		if(clusters[i] == 0):
			l.append(data[i])
			llabel.append(newnode.label[i])
		else:
			r.append(data[i]) 
			rlabel.append(newnode.label[i])
	newnode.left = Node(l,llabel)
	newnode.right = Node(r,rlabel)
	#print(len(newnode.left.data),len(newnode.right.data))
	return newnode.left,newnode.right



queue = []
rootnode = Node(input_data,labelofdata)
queue.append(rootnode)

leaf = []
while(len(queue)>0):
	
	node = queue[len(queue)-1]
	queue.pop()
	print(len(queue))
	leftnode,rightnode = Nodesplit(node,k)
	#print(len(queue),len(leftnode.data),len(rightnode.data))
	if(len(leftnode.data)<50):
		leaf.append(leftnode)
	else:
		queue.insert(0,leftnode)
	if(len(rightnode.data)<50):
		leaf.append(rightnode)
	else:
		queue.insert(0,rightnode)

# file = open('output.txt','w')
# print(clusters)
# for i in range(k):
# 	for j in range(D):
# 		file.write(str(round1(mu[i][j]))+' ')
# 	file.write('\n')


#print(leaf[0].data)

c=0
acc=0
for j in range(0,len(leaf)):
	c=0
	for i in leaf[j].label:
		if(i==5):
			c+=1
	ln = len(leaf[j].label)
	if(c>ln-c):
		print 'Cluster '+str(j)
		acc+=c*100/ln
		print 'Leaf node has label 5 with accuracy '+str(c*100/ln)+'%'
	else:
		print 'Cluster '+str(j)
		acc+=(ln-c)*100/ln
		print 'Leaf node has label 6 with accuracy '+str((ln-c)*100/ln)+'%' 

print 'Average Total accuracy: '+str(acc/float(len(leaf)))			