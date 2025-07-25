class State:
    def __init__(self,rabbits):
        self.rabbits=rabbits
        self.empty_index=rabbits.index('_')

    def goalTest(self):
        if self.rabbits==['R','R','R','_','L','L','L']:
            return True
        return False

    def moveGen(self):
        children=[]
        i=self.empty_index
        n=len(self.rabbits)
        if i-1>=0 and self.rabbits[i-1]=='L':
            new_rabbits=self.rabbits.copy()
            new_rabbits[i],new_rabbits[i-1]=new_rabbits[i-1],new_rabbits[i]
            children.append(State(new_rabbits))
        if i-2>=0 and self.rabbits[i-2]=='L' and self.rabbits[i-1]!='_':
            new_rabbits=self.rabbits.copy()
            new_rabbits[i],new_rabbits[i-2]=new_rabbits[i-2],new_rabbits[i]
            children.append(State(new_rabbits))
        if i+1<n and self.rabbits[i+1]=='R':
            new_rabbits=self.rabbits.copy()
            new_rabbits[i],new_rabbits[i+1]=new_rabbits[i+1],new_rabbits[i]
            children.append(State(new_rabbits))
        if i+2<n and self.rabbits[i+2]=='R' and self.rabbits[i+1]!='_':
            new_rabbits=self.rabbits.copy()
            new_rabbits[i],new_rabbits[i+2]=new_rabbits[i+2],new_rabbits[i]
            children.append(State(new_rabbits))
        return children

    def __str__(self):
        return f"{self.rabbits}"
    
    def __eq__(self,other):
        return self.rabbits==other.rabbits
    
    def __hash__(self):
        return hash(tuple(self.rabbits))

def reconstructPath(node_pair,CLOSED):
    parent_map={}
    for node,parent in CLOSED:
        parent_map[node]=parent
    path=[]
    node,parent=node_pair
    path.append(node)
    while parent is not None:
        path.append(parent)
        parent=parent_map[parent]
    return path


def removeSeen(children,OPEN,CLOSED):
    open_nodes=[node for node,parent in OPEN]
    close_nodes=[node for node,parent in CLOSED]
    new_nodes=[node for node in children if node not in open_nodes and node not in close_nodes ]
    return new_nodes


def bfs(start):
        OPEN=[(start,None)]
        CLOSED=[]
        while OPEN:
            node_pair=OPEN.pop(0)
            node,parent=node_pair
            if node.goalTest():
                print("Goal found")
                path = reconstructPath(node_pair, CLOSED)
                path.reverse()
            
                for p in path:
                    print("->", p)

                return
            else:
                CLOSED.append(node_pair)
                children=node.moveGen()
                new_nodes=removeSeen(children,OPEN,CLOSED)
                new_pairs=[(c,node) for c in new_nodes]
                OPEN=OPEN+new_pairs
        return []

def dfs(start):
        OPEN=[(start,None)]
        CLOSED=[]
        while OPEN:
            node_pair=OPEN.pop(0)
            node,parent=node_pair
            if node.goalTest():
                print("Goal found")
                path = reconstructPath(node_pair, CLOSED)
                path.reverse()
            
                for p in path:
                    print("->", p)

                return
            else:
                CLOSED.append(node_pair)
                children=node.moveGen()
                new_nodes=removeSeen(children,OPEN,CLOSED)
                new_pairs=[(c,node) for c in new_nodes]
                OPEN=new_pairs+OPEN
        return []


rabbits=['L','L','L','_','R','R','R']
new_state=State(rabbits)

bfs(new_state)
dfs(new_state)
