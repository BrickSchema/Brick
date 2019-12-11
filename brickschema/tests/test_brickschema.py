from brickschema import __version__
from brickschema.inference import TagInferenceSession


def test_version():
    assert __version__ == '0.1.0'


def test_lookup_tagset():
    session = TagInferenceSession()
    assert session is not None

    tagset1 = ['AHU', 'Equipment']
    inferred, leftover = session.most_likely_tagsets(tagset1)
    assert inferred == ['AHU']
    assert len(leftover) == 0

    tagset2 = ['Air', 'Flow', 'Sensor']
    inferred, leftover = session.most_likely_tagsets(tagset2)
    assert inferred == ['Air_Flow_Sensor']
    assert len(leftover) == 0

    tagset3 = ['Air', 'Flow', 'Sensor', 'Equipment']
    inferred, leftover = session.most_likely_tagsets(tagset3)
    assert inferred == ['Air_Flow_Sensor']
    assert len(leftover) == 1
