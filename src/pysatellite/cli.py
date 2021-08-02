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
