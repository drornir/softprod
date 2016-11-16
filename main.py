"""
k-edge-coloring exercise.
"""

from z3 import *

Petersen_V = range(10)
Petersen_E = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),

    (0, 5),
    (1, 6),
    (2, 7),
    (3, 8),
    (4, 9),

    (5, 7),
    (7, 9),
    (9, 6),
    (6, 8),
    (8, 5),
]


def get_k_edge_coloring(k, V, E):
    #
    # Your solution here...
    #
    pass


def get_k_edge_coloring_core(k, V, E):
    #
    # Your solution here...
    #
    pass


def get_k_edge(k, V, E):
    assert V == range(len(V))
    colors = range(k)
    # variables = [[Bool('v_{}_color_{}'.format(v, c)) for c in colors] for v in V]
    edgesColors = [[Bool('e_{}_col_{}'.format(e, c)) for c in colors] for e in E]

    s = Solver()
    # at least one color per edge
    for e in E:
        s.add(Or([edgesColors[e][c] for c in colors]))

    # at most one ccolor p edge
    for e in E:
        for c1 in range(k):
            for c2 in range(c1 + 1, k):
                s.add(Or(Not(edgesColors[e][c1]), Not(edgesColors[e][c2])))

    #
    for e1 in E:
        for e2 in E:
            if e1 != e2:
                if e1[0] == e2[0] or e1[1] == e2[0] or e1[0] == e2[1] or e1[1] == e2[1]:
                    for c in colors:
                        s.add(Or(Not(edgesColors[e1][c]), Not(edgesColors[e2][c])))


def draw_graph(V, E, coloring={}, filename='graph', engine='circo', directed=False):
    try:
        from graphviz import Graph, Digraph
    except ImportError:
        print "You don't have graphviz python interface installed. Sorry."
        return

    COLORS = ['blue', 'red', 'green', 'pink', 'yellow']
    if directed:
        dot = Digraph(engine=engine)
    else:
        dot = Graph(engine=engine)
    for v in V:
        if v in coloring:
            dot.node(str(v), style="filled", fillcolor=COLORS[coloring[v]])
        else:
            dot.node(str(v))
    for v1, v2 in E:
        if (v1, v2) in coloring:
            dot.edge(str(v1), str(v2), color=COLORS[coloring[(v1, v2)]])
        else:
            dot.edge(str(v1), str(v2))
    dot.render(filename, cleanup=True, view=True)


if __name__ == '__main__':
    #
    # Your tests here...
    #
    pass