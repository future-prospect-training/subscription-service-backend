from flask import Flask

from .extensions import db, jwt, ma, migrate
from .managers.SubscriptionManager import SubscriptionManager
from .routes.SubscriptionRoutes import SubscriptionRoutes
from .stores.SubscriptionStore import SubscriptionStore


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Stores
    subscription_store = SubscriptionStore(db)
    # Managers
    subscription_manager = SubscriptionManager(subscription_store)
    # Routes
    subscription_routes = SubscriptionRoutes(subscription_manager)
    # Attach routes
    app.register_blueprint(subscription_routes.bp)

    # Create tables TODO: Move to a separate file containing DB seeds
    with app.app_context():
        from .models import Subscription

        db.create_all()

    return app
