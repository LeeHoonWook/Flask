# Flask_DB

# 1. DB 설정 후

```sh
# DB Migrate 실행
(venv) User $ flask db init
(venv) User $ flask db current
(venv) User $ flask db migrate -m 'Init database'

# DB 변경 시
(venv) User $ flask db migrate -m 'add ~~'
(venv) User $ flask db upgrade

```