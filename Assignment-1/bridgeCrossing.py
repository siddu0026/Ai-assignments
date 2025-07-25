class State:
    def __init__(self, amogh, ameya, grandmother, grandfather, time, umbrella):
        self.amogh = amogh
        self.ameya = ameya
        self.grandmother = grandmother
        self.grandfather = grandfather
        self.time = time
        self.umbrella = umbrella

    def goalTest(self):
        if self.amogh == self.ameya == self.grandmother == self.grandfather == 'R' and self.time <= 60:
            return True
        return False

    def moveGen(self):
        children = []
        persons = ["amogh", "ameya", "grandmother", "grandfather", None]
        times = {
            "amogh": 5,
            "ameya": 10,
            "grandmother": 20,
            "grandfather": 25
        }
        new_side = 'R' if self.umbrella == 'L' else 'L'

        for i in range(5):
            first = persons[i]
            if first is not None and getattr(self, first) != self.umbrella:
                continue
            for j in range(i+1, 5):
                second = persons[j]
                if second is not None and getattr(self, second) != self.umbrella:
                    continue

                a = self.amogh
                m = self.ameya
                g = self.grandmother
                f = self.grandfather
                t = self.time
                u = self.umbrella

                if first == "amogh":
                    a = new_side
                elif first == "ameya":
                    m = new_side
                elif first == "grandmother":
                    g = new_side
                elif first == "grandfather":
                    f = new_side

                if second == "amogh":
                    a = new_side
                elif second == "ameya":
                    m = new_side
                elif second == "grandmother":
                    g = new_side
                elif second == "grandfather":
                    f = new_side

                trip_time = 0
                if first and second:
                    trip_time = max(times[first], times[second])
                elif first:
                    trip_time = times[first]
                elif second:
                    trip_time = times[second]

                new_state = State(a, m, g, f, t + trip_time, new_side)

                if new_state.isSafe():
                    children.append(new_state)

        return children

    def isSafe(self):
        return self.time <= 60

    def __str__(self):
        return "Amogh: " + self.amogh + " Ameya: " + self.ameya + " Grandmother: " + self.grandmother + " Grandfather: " + self.grandfather + " Time: " + str(self.time) + " Umbrella: " + self.umbrella

    def __eq__(self,other):
        return (self.amogh == other.amogh and
                self.ameya == other.ameya and
                self.grandmother == other.grandmother and
                self.grandfather == other.grandfather and
                self.time == other.time and
                self.umbrella == other.umbrella)

    def __hash__(self):
        return hash((self.amogh, self.ameya, self.grandmother, self.grandfather, self.time, self.umbrella))

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

start_state = State('L', 'L', 'L', 'L', 0, 'L')
bfs(start_state)
dfs(start_state)
