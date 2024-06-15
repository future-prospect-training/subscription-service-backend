from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..extensions import db
from ..extensions import ma
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
        exclude = ("id",)


class SubscriptionUpdateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subscription
        load_instance = True
        exclude = ("id", "created_at", "updated_at")
