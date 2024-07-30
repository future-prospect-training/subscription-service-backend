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
            subscription = self.db.session.query(Subscription).get(subscription_id)
            #subscription = Subscription.query.get(subscription_id)
            if not subscription:
                return None

            subscription_update_dict = subscription_update_dto.to_dict()
            for key, value in subscription_update_dict.items():
                setattr(subscription, key, value)

            self.db.session.commit()
            return subscription
        except Exception as e:
            self.db.session.rollback()
            raise e

    def delete_subscription(self, subscription_id):
        try:
            subscription = Subscription.query.get(subscription_id)
            if not subscription:
                return None

            self.db.session.delete(subscription)
            self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()
            raise e

    def get_active_subscriptions(self):
        return Subscription.query.filter_by(status="active").all()

    def get_pending_subscriptions(self):
        return Subscription.query.filter_by(status="pending").all()

    def get_expired_subscriptions(self):
        return Subscription.query.filter_by(status="expired").all()

    def get_cancelled_subscriptions(self):
        return Subscription.query.filter_by(status="cancelled").all()

    def get_subscription_by_user_id(self, user_id):
        return Subscription.query.filter_by(user_id=user_id).first()

    def get_subscription_by_product_id(self, product_id):
        return Subscription.query.filter_by(product_id=product_id).first()