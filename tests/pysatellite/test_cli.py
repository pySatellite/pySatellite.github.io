from pysatellite.cli import ping, what_are_you_doing


def test_ping():
    print(ping())


def test_what_are_you_doing():
    print(what_are_you_doing())
