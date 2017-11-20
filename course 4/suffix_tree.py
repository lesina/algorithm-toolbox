#Uses python3


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.child = dict()

    def add_child(self, value, child):
        self.child[value] = child

    def print(self):
        for child in self.child.values():
            child.print()
        if self.value != "NAN":
            print(self.value)


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
                    current_node = current_node.child[current_symbol]
        for pattern in pattern_list:
            current_node = self.root
            for i in range(len(pattern)):
                current_symbol = pattern[i]
                if current_symbol not in current_node.child:
                    continue
                while len(current_node.child[current_symbol].child) == 1:
                    current_node.child[current_symbol].value += list(current_node.child[current_symbol].child.values())[0].value
                    current_node.child[current_symbol].child = list(current_node.child[current_symbol].child.values())[0].child
                current_node = current_node.child[current_symbol]


text = input()
pattern_list = list()
for i in range(len(text)):
    pattern_list.append(text[i:])
# print(pattern_list)
trie = Trie()
trie.construct_trie(pattern_list)
trie.root.print()