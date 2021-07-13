from pysatellite.satellite import Satellite


def test_coordinates():
    xyz = Satellite.coordinates()
    assert xyz == "I don't know yet."
