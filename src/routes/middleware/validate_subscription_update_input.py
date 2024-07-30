from functools import wraps

from flask import jsonify, request
from marshmallow import ValidationError

from ...schemas.SubscriptionSchema import SubscriptionUpdateSchema
from ..utils.StatusCode import HttpStatus


def validate_subscription_update_input(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        schema = SubscriptionUpdateSchema()
        try:
            request.fields = schema.load(request.json)
        except ValidationError as err:
            return (
                jsonify({"success": False, "errors": err.messages}),
                HttpStatus.BAD_REQUEST.value,
            )
        return f(*args, **kwargs)

    return decorated_function
