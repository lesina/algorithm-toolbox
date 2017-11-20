# Uses python3

class node:
    def __init__(self, data = None):
        self.data   = data
        self.kids   = []

    def addChild(self, data):
        self.kids.append(data)


class Tree:
    def __init__(self, data):
        self.root = node(data)

    def newNode(self, data):
        return node(data)


def height(node):
    h = 0
    queue = [node]
    queue.append(None)
    while queue:
        NODE = queue.pop(0)
        if NODE == None:
            if queue:
                queue.append(None)
            h += 1
        else:
            queue += list(kid for kid in NODE.kids)
    return h
    # res = 0
    # for child in node.kids:
    #     res = max(res, height(child)+1)
    # return res
    #return 1 + max((height(c) for c in node.kids), default=-1)


n = int(input())
tree = list(map(int, input().split()))
mytree = Tree(tree.index(-1))
nodes = []
for i in range(n):
    nodes.append(mytree.newNode(data=i))
    # print(nodes[i])
for i in range(n):
    if tree[i] >= 0:
        nodes[tree[i]].addChild(nodes[i])
# for i in range(n):
#     print(nodes[i].kids)
mytree.root = nodes[tree.index(-1)]
print(height(mytree.root))