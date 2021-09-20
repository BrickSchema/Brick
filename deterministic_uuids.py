# Monkey patch uuid library to generate deterministic UUIDs.  BNode
# uses UUIDs when creating id and will now get deterministic sort
# order. This will remove the random order of some parts of the
# generated ontology file.
import uuid
import random

rd = random.Random()
rd.seed(0)
uuid.uuid4 = lambda: uuid.UUID(int=rd.getrandbits(128))
