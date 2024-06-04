from flask import Blueprint, request, jsonify


bp = Blueprint('subscriptions', __name__)

@bp.route('/subscriptions', methods = ['GET'])
def get_subscription():
    return {
        'name':'test'
    }, 200