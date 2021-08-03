import json
import random
import sys
import requests


def ping() -> str:
    """살았니~ 죽었니?"""
    return 'pong'


def what_are_you_doing() -> str:
    """지금 뭐하고 있는지 묻는 질문에 답을함

    Returns:
        블라블라~

    Todo:
        - 외계어 지원
        - 암호문 전송
        - 암호화 처리 후 회신
    """
    대답_뭉치 = ["It's circling around the Earth. Oh! I'm dizzy.",
             "잇스 서컬링 어라운드 디 이에얄티에이치 오우 아임 디지.",
             "지구 주위를 돌고 있어. 오! 어지럽다.",
             "wlrn wndnlfmf ehfrh dlTdj. dh! djwlfjqek."]

    return random.choice(대답_뭉치)


def cli_where_are_you_now():
    """인공위성의 위치 및 정보를 알고싶다면 사용해 보세요.

    API_KEY 는 https://www.n2yo.com/api/ 에서 발급

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> pySatellite-where-are-you-now 1 InvalidAPIKey
        {"error": "Invalid API Key!"}

        >>> pySatellite-where-are-you-now 1 **-****-***-****
        {"info": {"satname": "SL-1 R/B", "satid": 1, "transactionscount": 11}, "positions": [{"satlatitude": 0, "satlongitude": 0, "sataltitude": 0, "azimuth": 0, "elevation": 0, "ra": 0, "dec": 0, "timestamp": 0, "eclipsed": false}]}

    Returns:

    """
    satellite_id = sys.argv[1]
    api_key = sys.argv[2]
    d = where_are_you_now(satellite_id, api_key)

    return json.dumps(d)


def where_are_you_now(satellite_id: int, api_key: str, observer_lat=37.44, observer_lng=126.96, observer_alt=592.0, seconds=1) -> dict:
    """인공위성의 위도,경도,고도 등의 정보 수신

    Args:
        satellite_id: 인공위성 식별 id
        api_key: api key
        observer_lat: Observer's latitide (decimal degrees format)
        observer_lng: Observer's longitude (decimal degrees format)
        observer_alt: Observer's altitude above sea level in meters
        seconds: Number of future positions to return. Each second is a position. Limit 300 seconds

    Returns:
        https://www.n2yo.com/api/#positions
    """

    URL = "https://api.n2yo.com/rest/v1/satellite/positions"
    api = f"{URL}/{satellite_id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}/&apiKey={api_key}"

    res = requests.get(api)
    json_dict = res.json()
    return json_dict
