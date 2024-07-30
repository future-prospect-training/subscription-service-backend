from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models.Subscription import SubscriptionState

from ..extensions import db, ma
from ..models.Subscription import Subscription


class SubscriptionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        sqla_session = db.session


class SubscriptionCreateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        sqla_session = db.session
        exclude = ("id",)


class SubscriptionUpdateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        exclude = ("id", "created_at", "updated_at")
        load_instance = True
        sqla_session = db.session

    state = EnumField(SubscriptionState, by_value=True)  # Handle state as Enum
