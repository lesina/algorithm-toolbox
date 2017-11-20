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
                    current_node = current_node.child[current_symbol]

    def prefix_match(self, text):
        i = 0
        symbol = text[i]
        text_length = len(text)
        v = self.root
        while True:
            if not v.child:
                return True
            elif symbol in v.child:
                v = v.child[symbol]
                i += 1
                if i == text_length and not v.child:
                    return True
                elif i == text_length:
                    return False
                symbol = text[i]
            else:
                return False

    def match(self, text):
        i = 0
        text = list(text)
        indexes = []
        while text:
            if self.prefix_match(text):
                indexes.append(i)
            i += 1
            text.pop(0)
        return indexes


text = input()
n = int(input())
pattern_list = list()
for i in range(n):
    pattern_list.append(input())
trie = Trie()
trie.construct_trie(pattern_list)
print(*sorted(trie.match(text)))