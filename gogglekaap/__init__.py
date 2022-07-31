from flask import Flask, render_template, g
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

load_dotenv('.env')  # 배포 시 포함하여야 함


def create_app(config=None):
    app = Flask(__name__)

    """ === Flask Configuration === """
    from .configs import DevelopmentConfig, ProductionConfig
    if not config:
        if app.config['DEBUG']:
            config = DevelopmentConfig()
        else:
            config = ProductionConfig()

    print('run with: ', config)
    app.config.from_object(config)

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

    """ === Restx Init === """
    from .apis import blueprint as api
    app.register_blueprint(api)

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
