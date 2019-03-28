
#Justin Ruiloba
#Lab 4
#3/27/2019
#Instructor Dr.Fuentes
#B-tree
class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)

#my mehtods
#searchs for k returns depth k is in
def SearchD(T,k,d):
    # Returns depth where k is, or None if k is not in the tree
    #if k is in node return depth
	if k in T.item:
		return d
	#if leaf k is not in tree return none	
	if T.isLeaf:
		return None
	#keep searching the right child till u find k or dont find k add 1 to depth because you are going down a depth	
	return SearchD(T.child[FindChild(T,k)],k,d+1)
#finds minumum element at a given depth	
def minumumelement(T,d):
  #if d == 0 we are at right depth return minumum element in node
  if d==0:
    return T.item[0]
  #if leaf tree does not have that many depths return -1
  if T.isLeaf:
    return -1;
  #else go to smallest child first child d -1 because we are going down a level
  return minumumelement(T.child[0],d-1)
#maximum element at given depth
def maximumelement(T,d):
  #if d is ==0 at right depth return largest item in node
  if d==0:
    return T.item[-1]
  #depth to large		
  if T.isLeaf:
    return -1
  # keep going down a depth -1
  return maximumelement(T.child[-1],d-1)       
#checks and counts how many full nodes in tree
def nodesFull(T):
  count=0
  #if node full add one to count
  if IsFull(T):
    count+=1
    return count 
  #if leaf and not full return 0 to not infinite loop
  if T.isLeaf:
    return 0
  #llop to acess all children
  for i in range (len(T.item)+1):
    #adds one for each full children
	  count+=nodesFull(T.child[i])
	#return total full	
  return count
#return total numbers of leaf nodes that are full  
def leafnodesFull(T):
  count=0
  #if it is leaf and full add one
  if T.isLeaf and IsFull(T):
    count+=1
    return count 
  #if it is a leaf not full return 0 avoid infinite loop	
  if T.isLeaf:
    return 0
  #loop to acess all children	
  for i in range (len(T.item)+1):
    #add count to as many full leafs
    count+=leafnodesFull(T.child[i])
  return count 
#returns number of children at given depth  
def NumberofnodesA(T,d):
  #if at right depth return 1	
  if d==0:
    return 1 
  count=0
  #loop to acess all children	
  for i in range (len(T.item)+1):
    #call that - depth and acess each child
	  count+=NumberofnodesA(T.child[i],d-1)  
  return count 
#prints all items at the depth  
def PrintatDepth(T,d):
  # if d is equal to 0 print all items in node
  if d==0:
    for t in T.item:
      print(t,end=' ')
    return 
  #loop to acess all children  
  for i in range (len(T.item)+1):
	#print recursive call	
	  print(PrintatDepth(T.child[i],d-1))  
def heightT(T):
    if T.isLeaf:
        return 0
    return 1 + heightT(T.child[-1])      
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')

SearchAndPrint(T,60)
SearchAndPrint(T,200)
SearchAndPrint(T,25)
SearchAndPrint(T,20)
print("Depth search",SearchD(T,10,0))
print("min at depth",minumumelement(T,0))
print("max at depth",maximumelement(T,3))
print(nodesFull(T))
print(leafnodesFull(T))
print("num nodes at depth",NumberofnodesA(T,2))
print("Printmethod")
PrintatDepth(T,2)
print(heightT(T))


