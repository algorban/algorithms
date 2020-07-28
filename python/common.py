from collections import defaultdict


class Graph:

    @staticmethod
    def build_graph(edges):
        g = defaultdict(set)
        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])
        return g

    @staticmethod
    def build_digraph(edges):
        g = defaultdict(set)
        for edge in edges:
            g[edge[0]].add(edge[1])
        return g