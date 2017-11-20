# Uses python3
#
import math

def distance(x1, x2):
    return math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)


# def make_adjacency_matrix(vertexes, points):
#     matrix = list()
#     for i in range(vertexes):
#         matrix.append([100000] * vertexes)
#     for i in range(vertexes):
#         for j in range(i+1, vertexes):
#             weight = distance(points[i], points[j])
#             matrix[i][j] = weight
#             matrix[j][i] = weight
#     # for i in range(edges):
#     #     vertex1, vertex2, weight = list(map(int, input().split()))
#     #     vertex1 -= 1
#     #     vertex2 -= 1
#     #     matrix[vertex1][vertex2] = weight
#     #     # matrix[vertex2][vertex1] = weight
#     return matrix
#
#
# # def bfs(matrix, start, end):
# #     queue = [start]
# #     visited = [False]*len(matrix)
# #     distance = [float('inf')]*len(matrix)
# #     distance[start] = 0
# #     # answer = 0
# #     current = queue.pop(0)
# #     while queue:
# #         visited[current] = True
# #         min_id = current
# #         MIN = float('inf')
# #         for vertex in range(len(matrix)):
# #             if matrix[current][vertex] and not visited[vertex]:
# #                 queue.append(vertex)
# #             if matrix[current][vertex] and distance[current]+1 < distance[vertex]:
# #                 distance[vertex] = distance[current]+1
# #                 if distance[vertex] < MIN:
# #                     MIN = distance[vertex]
# #                     min_id = vertex
# #
# #         current = min_id
#
#
# # def Dexter(size, start, adjacency_matrix):
# #     valid = [True] * size
# #     weight = [100000] * size
# #     weight[start] = 0
# #     results = [100000] * size
# #     current = start
# #     for i in range(size):
# #         ID_min_weight = -1
# #         min_weight = 100001
# #         for j in range(size):
# #             if valid[j] and weight[j] > matrix[current][j]:
# #                 weight[j] = matrix[current][j]
# #                 if weight[j] < min_weight:
# #                     min_weight = weight[j]
# #                     ID_min_weight = j
# #         current = ID_min_weight
# #         valid[ID_min_weight] = False
# #     return weight
#
#
# def Dexter(size, start, matrix):
#     cost = [float('inf')] * size
#     parent = [None] * size


from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i_edge = 0
        i_result = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        # print self.graph
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while i_result < self.vertices - 1:
            u, v, w = self.graph[i_edge]
            i_edge = i_edge + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                i_result = i_result + 1
                result.append(w)
                self.union(parent, rank, x, y)
                # Else discard the edge
            # if len(result) == k+1:
            #     return result
        print(sum(result))


# vertexes, edges = list(map(int, input().split()))
vertexes = int(input())
points = list()
for i in range(vertexes):
    points.append(list(map(int, input().split())))
# matrix = make_adjacency_matrix(vertexes, points)
# answer = sum(Dexter(vertexes, 0, matrix))
# print(answer)
# print(sum(Dexter(vertexes, 0, matrix)))
graph = Graph(vertexes)
for i in range(vertexes):
    for j in range(i+1, vertexes):
        graph.addEdge(i, j, distance(points[i], points[j]))
graph.KruskalMST()