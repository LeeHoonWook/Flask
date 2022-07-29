from flask import Flask, render_template, g
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os


csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get(
        "SECRET_KEY")
    app.config['SESSION_COOKIE_NAME'] = 'gogglekaap'
    # 본인의 DB 설정에 맞추기!
    # SQLALCHEMY_DATABASE_URI='mysql+pymysql://계정:비밀번호@localhost/DB_Name?charset=utf8'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if app.config['DEBUG'] == True:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    """ === DB Init === """
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    """ === CSRF Init === """
    csrf.init_app(app)

    """ === Routes Init === """
    from gogglekaap.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    """ === Error Route === """
    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404

    @app.before_request
    def before_request():
        g.db = db.session

    """ === Request hook === """
    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
            g.db.close()

    return app
