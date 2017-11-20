# Uses python3

def make_adjacency_lists(vertices, edges):
    adj_list = {i : {} for i in range(vertices)}
    adj_list_rev = {i : {} for i in range(vertices)}
    for i in range(edges):
        vertex1, vertex2, weight = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        adj_list[vertex1][vertex2] = weight
        adj_list_rev[vertex2][vertex1] = weight
    return (adj_list, adj_list_rev)


def relax(u, v, dist, prev, adj_list):
    if dist[v] > dist[u] + adj_list[u][v]:
        dist[v] = dist[u] + adj_list[u][v]
        prev[v] = u


def process(u, adj_list, dist, prev, proc):
    for v in adj_list[u]:
        relax(u, v, dist, prev, adj_list)
    proc.append(u)


def shortest_path(s, dist, prev, proc, t, dist_rev, prev_rev, proc_rev):
    distance = float('inf')
    bestU = None
    for u in proc + proc_rev:
        if dist[u] + dist_rev[u] < distance:
            bestU = u
            distance = dist[u] + dist_rev[u]
    path = list()
    last = bestU
    while last != s:
        path.append(last)
        last = prev[last]
    path = path[::-1]
    last = bestU
    while last != t:
        last = prev_rev[last]
        path.append(last)
    return (distance, path)


def find_min(dist, valid):
    ID_MIN = -1
    min_weight = float('inf')
    for i in range(len(dist)):
        if dist[i] < min_weight and valid[i]:
            min_weight = dist[i]
            ID_MIN = i
    return ID_MIN


def bidirectional_dijkstra(adj_list, adj_list_rev, s, t):
    dist = [float('inf')] * vertices
    dist_rev = [float('inf')] * vertices
    dist[s] = 0
    dist_rev[t] = 0
    prev = [None] * vertices
    prev_rev = [None] * vertices
    proc = list()
    proc_rev = list()
    valid = [True] * vertices
    valid_rev = [True] * vertices
    while True:
        v = find_min(dist, valid)
        if v != -1:
            valid[v] = False
            process(v, adj_list, dist, prev, proc)
            if v in proc_rev:
                return shortest_path(s, dist, prev, proc, t, dist_rev, prev_rev, proc_rev)
        v_rev = find_min(dist_rev, valid_rev)
        if v_rev != -1:
            valid_rev[v_rev] = False
            process(v_rev, adj_list_rev, dist_rev, prev_rev, proc_rev)
            if v_rev in proc:
                return shortest_path(s, dist, prev, proc, t, dist_rev, prev_rev, proc_rev)
        if v == -1 or v_rev == -1:
            return (-1, ())


vertices, edges = list(map(int, input().split()))
# adjacency_list, adjacency_list_rev = make_adjacency_lists(vertices, edges)
# k = int(input())
# for i in range(k):
#     a, b = list(map(int, input().split()))
#     a -= 1
#     b -= 1
#     print(bidirectional_dijkstra(adjacency_list, adjacency_list_rev, a, b)[0])
# a, b = list(map(int, input().split()))
# a -= 1
# b -= 1
# print(bidirectional_dijkstra(adjacency_list, adjacency_list_rev, a, b)[0])


import heapq
# from Digraph import Digraph
from random import choice
from random import uniform
from time import time

class Digraph:
    """This class implements a directed, weighted graph with nodes represented by integers. """

    def __init__(self):
        """Initializes this digraph."""
        self.nodes = set()
        self.children = dict()
        self.parents = dict()
        self.edges = 0

    def add_node(self, node):
        """If 'node' is not already present in this digraph,
           adds it and prepares its adjacency lists for children and parents."""
        if node in self.nodes:
            return

        self.nodes.add(node)
        self.children[node] = dict()
        self.parents[node] = dict()

    def add_arc(self, tail, head, weight):
        """Creates a directed arc pointing from 'tail' to 'head' and assigns 'weight' as its weight."""
        if tail not in self.nodes:
            self.add_node(tail)

        if head not in self.nodes:
            self.add_node(head)

        self.children[tail][head] = weight
        self.parents[head][tail] = weight
        self.edges += 1

    def has_arc(self, tail, head):
        if tail not in self.nodes:
            return False

        if head not in self.nodes:
            return False

        return head in self.children[tail].keys()

    def get_arc_weight(self, tail, head):
        if tail not in self.nodes:
            raise Exception("The tail node is not present in this digraph.")

        if head not in self.nodes:
            raise Exception("The head node is not present in this digraph.")

        if head not in self.children[tail].keys():
            raise Exception("The edge (", tail, ", ", head, ") is not in this digraph.")

        return self.children[tail][head]

    def remove_arc(self, tail, head):
        """Removes the directed arc from 'tail' to 'head'."""
        if tail not in self.nodes:
            return

        if head not in self.nodes:
            return

        del self.children[tail][head]
        del self.parents[head][tail]
        self.edges -= 1

    def remove_node(self, node):
        """Removes the node from this digraph. Also, removes all arcs incident on the input node."""
        if node not in self.nodes:
            return

        self.edges -= len(self.children[node]) + len(self.parents[node])

        # Unlink children:
        for child in self.children[node]:
            del self.parents[child][node]

        # Unlink parents:
        for parent in self.parents[node]:
            del self.children[parent][node]

        del self.children[node]
        del self.parents [node]
        self.nodes.remove(node)

    def __len__(self):
        return len(self.nodes)

    def number_of_arcs(self):
        return self.edges

    def get_parents_of(self, node):
        """Returns all parents of 'node'."""
        if node not in self.nodes:
            return []

        return self.parents[node].keys()

    def get_children_of(self, node):
        """Returns all children of 'node'."""
        if node not in self.nodes:
            return []

        return self.children[node].keys()

    def clear(self):
        del self.nodes[:]
        self.children.clear()
        self.parents.clear()
        self.edges = 0


def test():
    digraph = Digraph()
    assert len(digraph) == 0

    for i in range(10):
        assert len(digraph) == i
        digraph.add_node(i)
        assert len(digraph) == i + 1

    digraph.remove_node(8)
    assert len(digraph) == 9
    digraph.remove_node(9)
    assert len(digraph) == 8
    assert digraph.number_of_arcs() == 0

    digraph.add_arc(8, 7, 20.0)
    assert digraph.has_arc(8, 7)
    assert 20.0 == digraph.get_arc_weight(8, 7)
    assert digraph.number_of_arcs() == 1

    digraph.add_arc(9, 8, 10.0)
    assert digraph.number_of_arcs() == 2
    assert digraph.get_arc_weight(9, 8) == 10.0
    assert digraph.has_arc(9, 8)
    assert not digraph.has_arc(8, 9)
    digraph.remove_node(8)
    assert not digraph.has_arc(9, 8)
    assert digraph.number_of_arcs() == 0

    digraph.remove_node(5)
    assert len(digraph) == 8

    digraph.add_arc(0, 3, 1.0)
    digraph.add_arc(1, 3, 2.0)
    digraph.add_arc(3, 6, 3.0)
    digraph.add_arc(3, 7, 4.0)

    assert digraph.number_of_arcs() == 4

    assert 0 in digraph.get_parents_of(3)
    assert 1 in digraph.get_parents_of(3)
    assert 6 in digraph.get_children_of(3)
    assert 7 in digraph.get_children_of(3)

    try:
        digraph.get_arc_weight(3, 100)
        assert False
    except Exception:
        pass

    try:
        digraph.get_arc_weight(100, 3)
        assert False
    except Exception:
        pass

    try:
        digraph.get_arc_weight(2, 3)
        assert False
    except Exception:
        pass

class HeapEntry:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


def traceback_path(target, parents):
    path = []

    while target:
        path.append(target)
        target = parents[target]

    return list(reversed(path))


def bi_traceback_path(touch_node, parentsa, parentsb):
    path = traceback_path(touch_node, parentsa)
    touch_node = parentsb[touch_node]

    while touch_node:
        path.append(touch_node)
        touch_node = parentsb[touch_node]

    return path


def dijkstra(graph, source, target):
    open = [HeapEntry(source, 0.0)]
    closed = set()
    parents = dict()
    distance = dict()

    parents[source] = None
    distance[source] = 0.0

    while open:
        top_heap_entry = heapq.heappop(open)
        current = top_heap_entry.node

        if current == target:
            return traceback_path(target, parents)

        closed.add(current)

        for child in graph.get_children_of(current):
            if child in closed:
                continue

            tentative_cost = distance[current] + graph.get_arc_weight(current, child)

            if child not in distance.keys() or distance[child] > tentative_cost:
                distance[child] = tentative_cost
                parents[child] = current
                heap_entry = HeapEntry(child, tentative_cost)
                heapq.heappush(open, heap_entry)

    return []  # Target not reachable from source, return empty list.


def bidirectional_dijkstra(graph, source, target):
    opena = [HeapEntry(source, 0.0)]
    openb = [HeapEntry(target, 0.0)]
    closeda = set()
    closedb = set()
    parentsa = dict()
    parentsb = dict()
    distancea = dict()
    distanceb = dict()

    best_path_length = {'value': 1e9}
    touch_node = {'value': None}

    parentsa[source] = None
    parentsb[target] = None

    distancea[source] = 0.0
    distanceb[target] = 0.0

    def update_forward_frontier(node, node_score):
        if node in closedb:
            path_length = distanceb[node] + node_score

            if best_path_length['value'] > path_length:
                best_path_length['value'] = path_length
                touch_node['value'] = node

    def update_backward_frontier(node, node_score):
        if node in closeda:
            path_length = distancea[node] + node_score

            if best_path_length['value'] > path_length:
                best_path_length['value'] = path_length
                touch_node['value'] = node

    def expand_forward_frontier():
        current = heapq.heappop(opena).node
        closeda.add(current)

        for child in graph.get_children_of(current):
            if child in closeda:
                continue

            tentative_score = distancea[current] + graph.get_arc_weight(current, child)

            if child not in distancea.keys() or tentative_score < distancea[child]:
                distancea[child] = tentative_score
                parentsa[child] = current
                heapq.heappush(opena, HeapEntry(child, tentative_score))
                update_forward_frontier(child, tentative_score)

    def expand_backward_frontier():
        current = heapq.heappop(openb).node
        closedb.add(current)

        for parent in graph.get_parents_of(current):
            if parent in closedb:
                continue

            tentative_score = distanceb[current] + graph.get_arc_weight(parent, current)

            if parent not in distanceb.keys() or tentative_score < distanceb[parent]:
                distanceb[parent] = tentative_score
                parentsb[parent] = current
                heapq.heappush(openb, HeapEntry(parent, tentative_score))
                update_backward_frontier(parent, tentative_score)

    while opena and openb:
        tmp = distancea[opena[0].node] + distanceb[openb[0].node]

        if tmp >= best_path_length['value']:
            return bi_traceback_path(touch_node['value'], parentsa, parentsb)

        if len(opena) + len(closeda) < len(openb) + len(closedb):
            expand_forward_frontier()
        else:
            expand_backward_frontier()
    if source == target:
        return [0]
    else:
        return [-1]


def create_random_digraph(nodes, arcs, max_weight):
    graph = Digraph()
    node_list = []

    for node in range(nodes):
        graph.add_node(node)
        node_list.append(node)

    for _ in range(arcs):
        weight = uniform(0.0, max_weight)
        graph.add_arc(choice(node_list),
                      choice(node_list),
                      weight)

    return graph, node_list


def path_cost(graph, path):
    cost = 0.0

    for i in range(len(path) - 1):
        tail = path[i]
        head = path[i + 1]

        if not graph.has_arc(tail, head):
            raise Exception("Not a path.")

        cost += graph.get_arc_weight(tail, head)

    return cost


def main():
    graph = Digraph()
    node_list = []
    for node in range(vertices):
        graph.add_node(node)
        node_list.append(node)
    for edge in range(edges):
        a, b, weight = list(map(int, input().split()))
        graph.add_arc(a-1, b-1, weight)
    n = int(input())
    for i in range(n):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        path = bidirectional_dijkstra(graph, a, b)
        if path[0] == 0:
            print(0)
        elif path[0] == -1:
            print(-1)
        else:
            print(path_cost(graph, path))

if __name__ == "__main__":
    main()