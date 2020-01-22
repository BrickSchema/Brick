"""
ORM for Brick
"""
from collections import defaultdict
from . import namespaces as ns
from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#TODO: brick:feeds (many-to-many), brick:hasPart

class Equipment(Base):
    """
    SQLAlchemy ORM class for BRICK.Equipment; see SQLORM class for usage
    """
    __tablename__ = 'equipment'

    name = Column(String, primary_key=True)
    type = Column(String)

    points = relationship("Point", back_populates="equipment")

    location_id = Column(ForeignKey("location.name"))
    location = relationship("Location", back_populates="equipment")

class Point(Base):
    """
    SQLAlchemy ORM class for BRICK.Point; see SQLORM class for usage
    """
    __tablename__ = 'point'

    name = Column(String, primary_key=True)
    type = Column(String)
    equipment_id = Column(ForeignKey("equipment.name"))
    equipment = relationship("Equipment", back_populates="points")

    location_id = Column(ForeignKey("location.name"))
    location = relationship("Location", back_populates="points")

class Location(Base):
    """
    SQLAlchemy ORM class for BRICK.Location; see SQLORM class for usage
    """
    __tablename__ = 'location'

    name = Column(String, primary_key=True)
    type = Column(String)
    equipment = relationship("Equipment", back_populates="location")
    points = relationship("Point", back_populates="location")

class SQLORM:
    """
    A SQLAlchemy-based ORM for Brick models.

    Currently, the ORM models Locations, Points and Equipment and the
    basic relationships between them.

    Please see the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/13/)
    for detailed information on how to interact with the ORM. use the
    `orm.session` instance variable to interact with the ORM connection.

    Example usage:

        from brickschema.graph import Graph
        from brickschema.namespaces import BRICK
        from brickschema.orm import SQLORM, Location, Equipment, Point

        # loads in default Brick ontology
        g = Graph(load_brick=True)
        # load in our model
        g.load_file("test.ttl")
        # put the ORM in a SQLite database file called "brick_test.db"
        orm = SQLORM(g, connection_string="sqlite:///brick_test.db")

        # get the points for each equipment
        for equip in orm.session.query(Equipment)
            print(f"Equpiment {equip.name} is a {equip.type} with \
                    {len(equip.points)} points")
            for point in equip.points:
                print(f"    Point {point.name} has type {point.type}")

        # filter for a given name or type
        hvac_zones = orm.session.query(Location)\
                                .filter(Location.type==BRICK.HVAC_Zone)\
                                .all()
        print(f"Model has {len(hvac_zones)} HVAC Zones")

        # other SQLalchemy query stuff:
        # https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying
    """

    def __init__(self, graph, connection_string="sqlite://brick_orm.db"):
        """
        Creates a new ORM instance over the given Graph using SQLAlchemy.
        The ORM does not capture *all* information expressed in a Brick model,
        but can be easily extended over time to capture more information.

        Args:
            graph (brickschema.Graph): a Brick schema graph containing
                instances we want to interact with. **Note**: this graph
                should not have any inference applied to it (RDFS or otherwise)
            connection_string (str): a database URL telling SQLAlchemy how to
                connect to the database that is backing the ORM. See
                [SQLAlchemy's documentation on database URLs](https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls)
        """
        self._graph = graph
        self._engine = create_engine(connection_string)
        Base.metadata.create_all(self._engine)

        # the SQLAlchemy session; use for queries, etc
        self.session = sessionmaker(bind=self._engine)()

        # populate the database

        # get all equipment
        res = self._graph.query("""SELECT ?equip ?type WHERE {
            ?equip  rdf:type/rdfs:subClassOf* brick:Equipment .
            ?equip  rdf:type ?type
        }""")
        for (equip_name, equip_type) in res:
            equip = Equipment(name=equip_name, type=equip_type)
            self.session.merge(equip)

        # get all points of equipment
        res = self._graph.query("""SELECT ?point ?type ?equip WHERE {
            ?point  rdf:type/rdfs:subClassOf* brick:Point .
            ?point  rdf:type ?type .
            {
                ?point  brick:isPointOf ?equip .
            } UNION {
                ?equip  brick:hasPoint ?point .
            }
        }""")
        for (point_name, point_type, equip_name) in res:
            point = Point(name=point_name, type=point_type,
                          equipment_id=equip_name)
            self.session.merge(point)

        # get all locations
        res = self._graph.query("""SELECT ?location ?type WHERE {
            ?location  rdf:type/rdfs:subClassOf* brick:Location .
            ?location  rdf:type ?type .
        }""")
        for (loc_name, loc_type) in res:
            loc = Location(name=loc_name, type=loc_type)
            self.session.merge(loc)

        # get all locations of equipment
        res = self._graph.query("""SELECT ?location ?type ?equip WHERE {
            ?equip  rdf:type/rdfs:subClassOf* brick:Equipment .
            ?location  rdf:type/rdfs:subClassOf* brick:Location .
            ?location  rdf:type ?type .
            {
                ?location  brick:isLocationOf ?equip .
            } UNION {
                ?equip  brick:hasLocation ?location .
            }
        }""")
        for (loc_name, loc_type, equip_name) in res:
            # get existing equip object
            equip = self.session.query(Equipment)\
                                .filter(Equipment.name==equip_name)\
                                .one()
            # get existing Location
            loc = self.session.query(Location)\
                              .filter(Location.name==loc_name)\
                              .one()
            self.session.merge(loc)
            loc.equipment.append(equip)
            self.session.merge(loc)

        self.session.commit()


class _DynamicORM:
    """
    TODO: under construction
    Object-oriented interface to Brick models. We turn triples into objects
    as follows:

    1. Equipment with points: all instances of equipment
    """

    def __init__(self, graph):
        """
        Creates a new ORM instance over the given Graph

        Args:
            graph (brickschema.Graph): a Brick schema graph containing
                instances we want to interact with. **Note**: this graph
                should not have any inference applied to it (RDFS or otherwise)
        """
        self.graph = graph

        # construct initial Equipment class
        self.equipment_classes = {
            "Equipment": type('Equipment', (), {
                "URI": ns.BRICK['Equipment'],
                "classname": 'Equipment',
                "name": None,
                "__repr__": _brick_repr,
                "points": [],
            }),
        }
        # construct subclasses recursively
        self._build_subclasses(self.equipment_classes['Equipment'],
                               self.equipment_classes, set())

        self.point_classes = {
            "Point": type('Point', (), {
                "URI": ns.BRICK['Point'],
                "classname": 'Point',
                "name": None,
            }),
        }
        self._build_subclasses(self.point_classes['Point'],
                               self.point_classes, set())

        # get equipment instances
        self.instances = {}
        for name, klass in self.equipment_classes.items():
            res = self.graph.query(f"""SELECT ?inst ?point ?pointtype WHERE {{
                ?inst a <{klass.URI}> .
                ?inst brick:hasPoint ?point .
                ?point a ?pointtype
            }}""")
            for (inst, point, pointtype) in res:
                inst_name = inst.split('#')[-1]
                class_inst = self.instances.get(inst_name, klass())
                pointtype = pointtype.split('#')[-1]
                if pointtype not in self.point_classes:
                    print(f"No instances of {pointtype} for {klass}")
                    continue
                point_class = self.point_classes[pointtype]
                point_inst = point_class()
                point_inst.name = point
                class_inst.name = inst_name
                class_inst.points.append(point_inst)
                self.instances[inst_name] = class_inst

    def _build_subclasses(self, rootclass, dest, visited=None):
        if rootclass.URI in visited:
            return
        visited.add(rootclass.URI)
        res = self.graph.query(f"""SELECT ?class WHERE {{
            ?class rdfs:subClassOf <{rootclass.URI}>
        }}""")
        for row in res:
            class_uri = row[0]
            name = class_uri.split('#')[-1]
            klass = type(name, (rootclass,), {
                "URI": class_uri,
                "classname": name,
                "__repr__": _brick_repr,
                "name": None,
                "points": [],
            })
            dest[name] = klass
            self._build_subclasses(klass, dest, visited=visited)

def _brick_repr(self):
    return(f"<BRICK {self.classname}: {self.name}>")
