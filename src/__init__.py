from flask import Flask, jsonify

from .extensions import db, jwt, ma, migrate
from .managers.SubscriptionManager import SubscriptionManager
from .routes.SubscriptionRoutes import SubscriptionRoutes
from .stores.SubscriptionStore import SubscriptionStore
from .routes.utils.StatusCode import HttpStatus

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

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = jsonify(
            {"success": False, "error": {"type": type(e).__name__, "message": str(e)}}
        )
        response.status_code = HttpStatus.INTERNAL_SERVER_ERROR.value
        return response

    # Create tables TODO: Move to a separate file containing DB seeds
    with app.app_context():
        from .models import Subscription

        db.create_all()

    return app
