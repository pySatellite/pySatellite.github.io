# How to contribute

First, try to make it move in your environment. And if there's anything interesting to add, start with the issue.

Right here - [good first issue](https://github.com/pySatellite/pySatellite.github.io/issues/new)

Then you'll be with us.

## Make a rolling wheel
### Bursting - Code & Environment
```bash
git clone https://github.com/pySatellite/pySatellite.github.io.git
```

```bash
$ cd pySatellite.github.io

# Use it optionally. If you're already on top of another Python environment, you can get out.
$ deactivate

$ pip install pipenv

$ pipenv shell

(pySatellite.github.io) $ pipenv install
# 자 이제 깨끗한 파이썬 가상 개발환경 위에 pySatellie 개발에 필요한 모듈이 설치 되었습니다.
# Now, on top of a clean Python virtual development environment, the modules needed for pySatellie development are installed. 
```

### Build & Install
```
python3 -m build
pip install .
```

### Test
```bash
(pySatellite.github.io) $ pipenv install --dev
(pySatellite.github.io) $ sh test.sh
sh test.sh
========== test session starts ==========
platform darwin -- Python 3.6.12, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/diginori/myhub/pySatellite.github.io/tests, configfile: ../pytest.ini
plugins: cov-2.12.1
collected 2 items

tests/pysatellite/test_rocket.py .                   [ 50%]
tests/pysatellite/test_satellite.py .                [100%]

-------------------------- generated xml file: /Users/diginori/myhub/pySatellite.github.io/report/test/tests.xml --------------------------

---------- coverage: platform darwin, python 3.6.12-final-0 ----------
Name    Stmts   Miss  Cover
---------------------------
---------------------------
TOTAL       7      0   100%

2 files skipped due to complete coverage.
Coverage XML written to file report/coverage/coverage.xml

========== 2 passed in 10.14s ==========
```

### 문서화
- Create a documentation website by automatically reading the Google-style docstring written in the code. Make sure that the module you added or modified has an appropriate explanation.
- 코드에 작성된 구글 스타일 docstring 을 자동으로 읽어 문서화 웹사이트를 만들어 냅니다. 당신이 추가하거나 수정한 모듈에 적절한 설명이 있는지 확인하세요.
```base
mkdocs serve
# Serving on http://127.0.0.1:8000/
```

