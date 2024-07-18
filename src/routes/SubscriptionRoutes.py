from flask import Blueprint, jsonify, request

from ..schemas.SubscriptionSchema import SubscriptionSchema
from .utils.StatusCode import HttpStatus


class SubscriptionRoutes:
    bp = Blueprint("subscription", __name__)

    def __init__(self, subsciption_manager):
        self.subscription_manager = subsciption_manager
    
        # Register the routes
        self.bp.add_url_rule("/subscriptions", "get_all_subscriptions", self.get_all_subscriptions, methods=["GET"])
        self.bp.add_url_rule("/subscriptions/<int:subscription_id>", "get_subscription", self.get_subscription, methods=["GET"])
        self.bp.add_url_rule("/subscriptions", "create_subscription", self.create_subscription, methods=["POST"])
        self.bp.add_url_rule("/subscriptions/<int:subscription_id>", "update_subscription", self.update_subscription, methods=["PUT"])
        self.bp.add_url_rule("/subscriptions/<int:subscription_id>", "delete_subscription", self.delete_subscription, methods=["DELETE"])
    
    def get_all_subscriptions(self):
        subscriptions = self.subscription_manager.get_all_subscriptions()
        return {
            "success": True,
            "data": [subscription.to_dist() for subscription in subscriptions],
        }, HttpStatus.OK.value

    def get_subscription(self, subscription_id):
        subscription = self.subscription_manager.get_subscription(subscription_id)
        if subscription is None:
            return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND.value
        return {"success": True, "data": subscription.to_dict()}, HttpStatus.OK.value

    def create_subscription(self):
        fields = [
            "created_at",
            "updated_at",
            "activated_at",
            "cancelled_at",
            "expires_at",
            "current_period_started_at",
            "current_period_ends_at",
            "state",
        ]
        subscription_create_dto = {field: request.json.get(field) for field in fields}

        subscription = self.subscription_manager.create_subscription(
            subscription_create_dto
        )
        return {
            "success": True,
            "data": subscription.to_dict(),
        }, HttpStatus.CREATED.value

    def update_subscription(self, subscription_id):
        subscription_schema = SubscriptionSchema()
        subscription_data = request.get_json()

        try:
            subscription_update_dto = subscription_schema.load(subscription_data)

            subscription = self.subscription_manager.get_subscription(subscription_id)
            if subscription is None:
                return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND.value

            updated_subscription = self.subscription_manager.update_subscription(
                subscription_id, subscription_update_dto  # Pass the update DTO directly
            )
            return {
                "success": True,
                "data": updated_subscription.to_dict(),
            }, HttpStatus.OK.value
        except Exception as e:
            return {"error": str(e)}, HttpStatus.BAD_REQUEST.value

    def delete_subscription(self, subscription_id):
        subscription = self.subscription_manager.get_subscription(subscription_id)
        if subscription is None:
            return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND.value

        self.subscription_manager.delete_subscription(subscription)
        return {"success": True}, HttpStatus.NO_CONTENT.value
