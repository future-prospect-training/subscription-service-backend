from flask import Blueprint, jsonify, request

from ..managers.SubscriptionManager import SubscriptionManager
from ..schemas.SubscriptionSchema import SubscriptionSchema
from .utils.StatusCode import HttpStatus

bp = Blueprint("subscriptions", __name__)


# TODO: Fix this endpoint to return all subscriptions in the DB
@bp.route("/subscriptions", methods=["GET"])
def get_subscription():
    return {"name": "test"}, HttpStatus.OK


# TODO: Implement get_subscription


@bp.route("/subscriptions", methods=["POST"])
def create_subscription():
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

    subscription = SubscriptionManager.create_subscription(subscription_create_dto)
    return {"success": True, "data": subscription.to_dict()}, HttpStatus.CREATED.value


# TODO: Fix issue with items in update_subscription
@bp.route("/subscriptions/<subscription_id>", methods=["PUT"])
def update_subscription(subscription_id):
    subscription_schema = SubscriptionSchema()
    subscription_data = request.get_json()

    try:
        subscription_update_dto = subscription_schema.load(subscription_data)

        subscription = SubscriptionManager.get_subscription(subscription_id)
        if subscription is None:
            return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND.value

        updated_subscription = SubscriptionManager.update_subscription(
            subscription_id, subscription_update_dto
        )
        return {
            "success": True,
            "data": updated_subscription.to_dict(),
        }, HttpStatus.OK.value
    except Exception as e:
        return {"error": str(e)}, HttpStatus.BAD_REQUEST.value


@bp.route("/subscriptions", methods=["DELETE"])
def delete_subscription(subscription_id):
    subscription = SubscriptionManager.get_subscription(subscription_id)
    if subscription is None:
        return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND

    SubscriptionManager.delete_subscription(subscription)
    return {"success": True}, HttpStatus.NO_CONTENT
