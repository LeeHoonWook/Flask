# Flask 시작하기

## 1. 실행하기

> 해당 서버는 개발 서버로 배포 시 배포 서버를 확인해주세요.   
> 참고 : https://flask.palletsprojects.com/en/2.1.x/quickstart/

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

```sh
# FLASK install
(venv) User $ pip install flask

# 의존성 기록
(venv) User $ pip freeze > requirements.txt

# FLASK_APP 환경변수 설정
(venv) User $ export FLASK_APP=폴더명/app.py:app
(venv) User $ flask run

# 디버그 모드
(venv) User $ export FLASK_ENV=development
```

## 1-1. Application Factories

> 참고 : https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app

```
```sh
# 모듈화 환경변수 설정
(venv) User $ export FLASK_APP=폴더명
(venv) User $ flask run

# 디버그 모드
(venv) User $ export FLASK_ENV=development
```
