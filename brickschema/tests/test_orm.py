from brickschema.graph import Graph
from brickschema.namespaces import BRICK
from rdflib import Namespace
from brickschema.orm import SQLORM, Location, Equipment, Point
import pkgutil
import io


def test_orm():
    g = Graph(load_brick=True)
    data = pkgutil.get_data(__name__, "data/test.ttl").decode()
    g.load_file(source=io.StringIO(data))
    orm = SQLORM(g, connection_string="sqlite:///:memory:")

    equips = orm.session.query(Equipment).all()
    assert len(equips) == 5

    points = orm.session.query(Point).all()
    assert len(points) == 3

    locs = orm.session.query(Location).all()
    assert len(locs) == 4

    hvac_zones = orm.session.query(Location)\
                            .filter(Location.type == BRICK.HVAC_Zone)\
                            .all()
    assert len(hvac_zones) == 1

    # test relationships
    BLDG = Namespace("http://example.com/mybuilding#")
    vav2_4 = orm.session.query(Equipment)\
                        .filter(Equipment.name == BLDG["VAV2-4"]).one()
    assert vav2_4.type == str(BRICK.Variable_Air_Volume_Box)
    assert len(vav2_4.points) == 2


    vav2_4_dpr = orm.session.query(Equipment)\
                            .filter(Equipment.name == BLDG["VAV2-4.DPR"]).one()
    assert vav2_4_dpr.type == str(BRICK.Damper)
    assert len(vav2_4_dpr.points) == 1

    tstat = orm.session.query(Equipment)\
                       .filter(Equipment.name == BLDG["tstat1"]).one()
    room_410 = orm.session.query(Location)\
                          .filter(Location.name == BLDG["Room-410"]).one()
    assert tstat.location == room_410
    assert tstat in room_410.equipment
