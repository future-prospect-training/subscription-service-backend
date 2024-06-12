from flask import Blueprint, request, jsonify
from .utils.StatusCode import HttpStatus
from ..managers.SubscriptionManager import SubscriptionManager

bp = Blueprint('subscriptions', __name__)

@bp.route('/subscriptions', methods = ['GET'])
def get_subscription():
    return {
        'name':'test'
    }, HttpStatus.OK

@bp.route('/subscriptions', methods = ['POST'])
def create_subscription():
    fields = [
        'created_at', 'updated_at', 'activated_at', 'cancelled_at',
        'expires_at', 'current_period_started_at', 'current_period_ends_at', 'state'
    ]
    subscription_create_dto = {field: request.json.get(field) for field in fields}

    subscription = SubscriptionManager.create_subscription(subscription_create_dto)
    return {
        'success': True,
        'data': subscription.to_dict()
    }, HttpStatus.CREATED.value