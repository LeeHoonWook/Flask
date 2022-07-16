# Flask_request_hook

## 1. application context & request_hook

> 자주 사용되는 앱 컨텍스트는 g와 current_app이 있다.<br/><br/>
> @ 참고 사이트    
https://flask-docs-kr.readthedocs.io/ko/latest/appcontext.html   
https://flask.palletsprojects.com/en/2.1.x/api/

```python
from flask import g, current_app

    # 최초 실행 시 실행할 함수를 등록합니다.
    @app.before_first_request
    def before_first_request():
        app.logger.info("BEFORE_FIRST_REQUEST")

    # 각 요청 전에 실행할 함수를 등록합니다.
    @app.before_request
    def before_request():
        g.test = True
        app.logger.info("BEFORE_REQUEST")

    # 각 요청 후에 실행할 함수를 등록합니다.
    @app.after_request
    def after_request(response):
        app.logger.info(f"g.test: {g.test}")
        app.logger.info(f"current_app.config: {current_app.config}")
        app.logger.info("AFTER_REQUEST")
        return response

    # 예외 발생 여부에 관계없이 각 요청이 끝날 때 실행할 함수를 등록합니다.
    # 이러한 함수는 실제 요청이 수행되지 않았더라도 요청 컨텍스트가 팝될 때 실행됩니다.
    @app.teardown_request
    def teardown_request(exception):
        app.logger.info("TEARDOWN_REQUEST")

    # 애플리케이션 컨텍스트가 종료될 때 호출될 함수를 등록합니다.
    # 이러한 함수는 일반적으로 요청 컨텍스트가 표시될 때도 호출됩니다.
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        app.logger.info("TEARDOWN_CONTEXT")
```

## 2. Method

```python
@app.route(
    "/test/method/", defaults={"id": 1}, methods=["GET", "POST", "DELETE", "PUT"]
)
@app.route("/test/method/<int:id>", methods=["GET", "POST", "DELETE", "PUT"])
def method_test(id):
    return jsonify(
        {
            "id": id,
            # GET으로 받은 값
            "request.args": request.args,
            # POST로 받은 값
            "request.form": request.form,
            # JSON으로 받은 값
            "request.json": request.json,
        }
    )
```