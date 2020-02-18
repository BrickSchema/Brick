def make_readable(res):
    """
    Eliminates the namespace from each element in the results of a
    SPARQL query.
    """
    return [[uri.split("#")[-1] for uri in row] for row in res]
