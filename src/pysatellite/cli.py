import random


def ping() -> str:
    """살았니~ 죽었니?"""
    return 'pong'


def what_are_you_doing() -> str:
    """지금 뭐하고 있는지 묻는 질문에 답을함

    Returns:

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
    return {
        "info": {
            "satname": "CAS500-1",
            "satid": 47932,
            "transactionscount": 14
        },
        "positions": [
            {
                "satlatitude": 72.37270065,
                "satlongitude": -130.5659036,
                "sataltitude": 507.55,
                "azimuth": 20.41,
                "elevation": -25.18,
                "ra": 16.73985319,
                "dec": 24.41137318,
                "timestamp": 1627895784,
                "eclipsed": False
            }
        ]
    }
