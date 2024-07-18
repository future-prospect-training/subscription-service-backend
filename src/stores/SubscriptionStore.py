from ..models.Subscription import Subscription


class SubscriptionStore:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def get_all_subscriptions():
        return Subscription.query.all()  # SELECT * FROM subscriptions

    @staticmethod
    def get_subscription(subscription_id):
        return Subscription.query.get(subscription_id)

    def save_subscription(self, subscription):
        try:
            self.db.session.add(subscription)
            self.db.session.commit()
            return subscription
        except Exception as e:
            self.db.session.rollback()
            raise e

    def update_subscription(self, subscription_id, subscription_update_dto):
        try:
            subscription = Subscription.query.get(subscription_id)
            if not subscription:
                return None

            subscription_update_dict = dict(
                subscription_update_dto
            )  # Convert to a dictionary
            for key, value in subscription_update_dict.items():
                setattr(subscription, key, value)

            self.db.session.commit()
            return subscription
        except Exception as e:
            self.db.session.rollback()
            raise e
