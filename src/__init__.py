from flask import Flask
from .extensions import db, migrate, jwt
from .routes import subscription_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    app.register_blueprint(subscription_routes.bp)
    return app