import networkx as nx

dep_graph = nx.read_dot('total_no_extras.dot')

edges = set()
for dep in dep_graph.edges_iter():
    sorted_dep = tuple(sorted(dep))
    if sorted_dep not in edges:
        edges.add(sorted_dep)
    else:
        print('Circular dependency between {0}'.format(dep))
