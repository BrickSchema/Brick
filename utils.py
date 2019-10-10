from dijkstar import Graph, find_path


def find_conversions(source, target, versions_graph):
    graph = Graph()
    for source_version, target_version in versions_graph.query("""SELECT ?source_version ?target_version{
                        ?source_version version:updatesTo ?target_version .
    }"""):
        graph.add_edge(str(source_version), str(target_version), {'conversions': 1})
        print(str(source_version), str(target_version))
    res = find_path(graph, str(source), str(target), cost_func=lambda u, v, e, prev_e: e['conversions'])
    conversions = []
    print(' -> '.join(res.nodes))
    current = source
    for node in res.nodes:
        conversions.append((current, node))
        current = node
    return conversions[1:]


def convert(conversion, model_graph):
    with open('./conversions/{}-{}.sparql'.format(*conversion), 'r') as file:
        conversion_query = file.read()
    model_graph.query(conversion_query)
