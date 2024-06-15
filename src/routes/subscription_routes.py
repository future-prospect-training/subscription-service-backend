from flask import Blueprint, jsonify, request

from ..managers.SubscriptionManager import SubscriptionManager
from .utils.StatusCode import HttpStatus

bp = Blueprint("subscriptions", __name__)


@bp.route("/subscriptions", methods=["GET"])
def get_subscription():
    return {"name": "test"}, HttpStatus.OK


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


@bp.route("/subscriptions", methods=["PUT"])
def update_subscription(subscription_id):
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
    subscription_update_dto = {field: request.json.get(field) for field in fields}

    subscription = SubscriptionManager.get_subscription(subscription_id)
    if subscription is None:
        return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND

    updated_subscription = SubscriptionManager.update_subscription(
        subscription, subscription_update_dto
    )
    return {"uccess": True, "data": updated_subscription.to_dict()}, HttpStatus.OK


@bp.route("/subscriptions", methods=["DELETE"])
def delete_subscription(subscription_id):
    subscription = SubscriptionManager.get_subscription(subscription_id)
    if subscription is None:
        return {"error": "Subscription not found"}, HttpStatus.NOT_FOUND

    SubscriptionManager.delete_subscription(subscription)
    return {"success": True}, HttpStatus.NO_CONTENT
