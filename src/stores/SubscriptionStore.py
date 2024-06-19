from ..extensions import db
from ..models.Subscription import Subscription


class SubscriptionStore:
    @staticmethod
    def get_all_subscriptions():
        return Subscription.query.all()  # SELECT * FROM subscriptions

    @staticmethod
    def get_subscription(subscription_id):
        return Subscription.query.get(subscription_id)

    @staticmethod
    def save_subscription(subscription):
        try:
            db.session.add(subscription)
            db.session.commit()
            return subscription
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_subscription(subscription_id, subscription_update_dto):
        try:
            subscription = Subscription.query.get(subscription_id)
            if not subscription:
                return None

            subscription_update_dict = dict(
                subscription_update_dto
            )  # Convert to a dictionary
            for key, value in subscription_update_dict.items():
                setattr(subscription, key, value)

            db.session.commit()
            return subscription
        except Exception as e:
            db.session.rollback()
            raise e
