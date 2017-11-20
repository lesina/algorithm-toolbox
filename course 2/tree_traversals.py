#Uses python3


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


class Node:

    def __init__(self, key):
        self.key = key

    def addLeftChild(self, leftChild):
        self.leftChild = leftChild

    def addRightChild(self, rightChild):
        self.rightChild = rightChild


class Tree:

    def __init__(self, root):
        self.root = root

    # def preOrder(self, node):
    #     print(node.key, end=" ")
    #     if node.leftChild.key != -1:
    #         self.preOrder(node.leftChild)
    #     if node.rightChild.key != -1:
    #         self.preOrder(node.rightChild)

    def preOrder(self, node):
        nodeStack = []
        nodeStack.append(node)
        while (len(nodeStack) > 0):
            node = nodeStack.pop()
            print(node.key, end=" ")
            if node.rightChild.key != -1:
                nodeStack.append(node.rightChild)
            if node.leftChild.key != -1:
                nodeStack.append(node.leftChild)

    # def postOrder(self, node):
    #     if node.leftChild.key != -1:
    #         self.postOrder(node.leftChild)
    #     if node.rightChild.key != -1:
    #         self.postOrder(node.rightChild)
    #     print(node.key, end=" ")

    def postOrder(self, node):
        stack = []
        # ans = []
        while (True):
            while (node.key != -1):
                if node.rightChild.key != -1:
                    stack.append(node.rightChild)
                stack.append(node)
                node = node.leftChild
            node = stack.pop()
            if (node.rightChild.key != -1 and
                        peek(stack) == node.rightChild):
                stack.pop()
                stack.append(node)
                node = node.rightChild
            else:
                ans.append(node.key)
                node = nullNode
            if (len(stack) <= 0):
                break

    # def inOrder(self, node):
    #     if node.leftChild.key != -1:
    #         self.inOrder(node.leftChild)
    #     print(node.key, end=" ")
    #     if node.rightChild.key != -1:
    #         self.inOrder(node.rightChild)

    def inOrder(self, node):
        current = node
        stack = []
        done = False
        while (not done):
            if current.key != -1:
                stack.append(current)
                current = current.leftChild
            else:
                if (len(stack) > 0):
                    current = stack.pop()
                    print(current.key, end=" ")
                    current = current.rightChild
                else:
                    done = True


n = int(input())
nodes = list()
ans = []
nullNode = Node(-1)
dataList = list()
for i in range(n):
    dataList.append(list(map(int, input().split())))
    nodes.append(Node(dataList[i][0]))
for i in range(n):
    if dataList[i][1] != -1:
        nodes[i].addLeftChild(nodes[dataList[i][1]])
    else:
        nodes[i].addLeftChild(nullNode)
    if dataList[i][2] != -1:
        nodes[i].addRightChild(nodes[dataList[i][2]])
    else:
        nodes[i].addRightChild(nullNode)
tree = Tree(nodes[0])
tree.inOrder(tree.root)
print("")
tree.preOrder(tree.root)
print("")
tree.postOrder(tree.root)
print(*ans)