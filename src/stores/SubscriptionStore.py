from ..extensions import db
from ..models.Subscription import Subscription


class SubscriptionStore:
    @staticmethod
    def get_all_subscriptions():
        return Subscription.objects.all()  # SELECT * FROM subscriptions

    @staticmethod
    def get_subscription(subscription_id):
        return Subscription.query.get({"id": subscription_id})

    @staticmethod
    def save_subscription(subscription):
        try:
            db.session.add(subscription)
            db.session.commit()
            return subscription
        except:
            db.session.rollback()
            raise

    @staticmethod
    def update_subscription(subscription_id, subscription_update_dto):
        try:
            subscription = Subscription.query.get(subscription_id)
            if not subscription:
                return None

            # TODO: Fix this to not throw an error, because items is not a valid method
            for key, value in subscription_update_dto.items():
                setattr(subscription, key, value)

            db.session.commit()
            return subscription
        except:
            db.session.rollback()
            raise
