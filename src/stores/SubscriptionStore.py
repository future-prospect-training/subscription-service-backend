from ..models.Subscription import Subscription
from ..extensions import db

class SubscriptionStore:
    @staticmethod
    def get_all_subscriptions():
        return Subscription.objects.all() # SELECT * FROM subscriptions

    @staticmethod
    def save_subscription(subscription):
        try:
            db.session.add(subscription)
            db.session.commit()
            return subscription
        except:
            db.session.rollback()
            raise