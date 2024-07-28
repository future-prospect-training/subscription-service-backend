from ..extensions import db
from ..models import Subscription


class SubscriptionService:
    def create_subscription(self, **kwargs):
        subscription = Subscription(**kwargs)
        db.session.add(subscription)
        db.session.commit()
        return subscription

    def get_subscription(self, subscription_id):
        return Subscription.query.get(subscription_id)

    def update_subscription(self, subscription_id, **kwargs):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            for key, value in kwargs.items():
                setattr(subscription, key, value)
            db.session.commit()
        return subscription

    def delete_subscription(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            db.session.delete(subscription)
            db.session.commit()
        return subscription

    def activate_subscription(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            subscription.activate()
        return subscription

    def cancel_subscription(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            subscription.cancel()
        return subscription

    def expire_subscription(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            subscription.expire()
        return subscription

    def update_subscription_status(self, subscription_id):
        subscription = self.get_subscription(subscription_id)
        if subscription:
            subscription.update_status()
        return subscription

    def get_active_subscriptions(self):
        return Subscription.get_active_subscriptions()

    def get_pending_subscriptions(self):
        return Subscription.get_pending_subscriptions()

    def get_cancelled_subscriptions(self):
        return Subscription.get_cancelled_subscriptions()

    def get_expired_subscriptions(self):
        return Subscription.get_expired_subscriptions()
