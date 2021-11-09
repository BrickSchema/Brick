from rdflib import BNode


class BlankNode:
    counter = -1

    @staticmethod
    def new():
        BlankNode.counter += 1
        return BNode("N" + str(BlankNode.counter))
