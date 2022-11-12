from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

top = Node(1)
node_l = Node(2)
node_r = Node(3)
top.left = node_l
top.right = node_r
node_l_l = Node(4)
node_l_r = Node(5)
node_l.left = node_l_l
node_l.right = node_l_r

node_r_l = Node(6)
node_r.left = node_r_l

node_l_r_l = Node(7)
node_l_r.left = node_l_r_l

node = top
a = node

def print_bfs(top):
    q = deque()
    
    q.append(top)
    
    while len(q) > 0:
        node = q.popleft()
        print(node, end=', ')
        for next_node in [node.left,node.right]:
            if next_node is not None:
                q.append(next_node)

print_bfs(a)