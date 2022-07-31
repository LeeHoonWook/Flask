import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    """Flask Config"""
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    SESSION_COOKIE_NAME = 'gogglekaap'
    # 본인의 DB 설정에 맞추기!
    # SQLALCHEMY_DATABASE_URI='mysql+pymysql://계정:비밀번호@localhost/DB_Name?charset=utf8'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "DB-ERROR")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    """Flask Config for Dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # TODO: Front호출시 토큰 삽입
    WTF_CSRF_ENABLED = False


class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'


class ProductionConfig(Config):
    """Flask Config for Production"""
    pass
