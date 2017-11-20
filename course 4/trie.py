#Uses python3


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.child = dict()

    def add_child(self, value, child):
        self.child[value] = child


class Trie:
    def __init__(self):
        self.nodes = [0]
        self.root = Node(0, "NAN")

    def construct_trie(self, pattern_list):
        for pattern in pattern_list:
            current_node = self.root
            for i in range(len(pattern)):
                current_symbol = pattern[i]
                if current_symbol in current_node.child:
                    current_node = current_node.child[current_symbol]
                else:
                    current_node.child[current_symbol] = Node(len(self.nodes), current_symbol)
                    self.nodes.append(self.nodes[-1] + 1)
                    ###task
                    print(current_node.key, "->", self.nodes[-1], ":", current_symbol, sep="")
                    ###
                    current_node = current_node.child[current_symbol]


n = int(input())
pattern_list = list()
for i in range(n):
    pattern_list.append(input())
trie = Trie()
trie.construct_trie(pattern_list)