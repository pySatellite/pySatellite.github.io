import json
import sys
from pysatellite.cli import ping, what_are_you_doing, where_are_you_now, cli_where_are_you_now
import os


def test_ping():
    print(ping())


def test_what_are_you_doing():
    print(what_are_you_doing())


def test_where_are_you_now():
    # https://www.n2yo.com/login/edit/ -> License K
    # export N2YO_KEY="****"
    r = where_are_you_now(satellite_id=47932, api_key=os.environ['N2YO_KEY'])
    assert r['info']['satname'] == 'CAS500-1'


def test_cli_where_are_you_now():
    satellite_id = 47932
    api_key = os.environ['N2YO_KEY']
    sys.argv = ['foo', satellite_id, api_key]
    j = cli_where_are_you_now()

    isinstance(j, str)
    json_dict = json.loads(j)
    assert json_dict['info']['satname'] == 'CAS500-1'
