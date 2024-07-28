import logging

from psycopg2 import OperationalError, ProgrammingError

from ..models.Subscription import Subscription

# Configure logging
logging.basicConfig(level=logging.ERROR)


class SubscriptionManager:
    def __init__(self, subscription_store):
        self.subscription_store = subscription_store

    def get_all_subscriptions(self):
        return self.subscription_store.get_all_subscriptions()

    def get_subscription(self, subscription_id):
        return self.subscription_store.get_subscription(subscription_id)

    def create_subscription(self, subscription_create_dto):
        try:
            return self.subscription_store.save_subscription(subscription_create_dto)
        except OperationalError as e:
            logging.error(f"Database error creating subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error creating subscription: {e}")
            raise

    def update_subscription(self, subscription_id, subscription_update_dto):
        # Input validation
        if not subscription_update_dto:
            raise ValueError("subscription_update_dto cannot be empty")

        try:
            return self.subscription_store.update_subscription(
                subscription_id, subscription_update_dto
            )
        except OperationalError as e:
            logging.error(f"Database error updating subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error updating subscription: {e}")
            raise

    def delete_subscription(self, subscription_id):
        try:
            return self.subscription_store.delete_subscription(subscription_id)
        except OperationalError as e:
            logging.error(f"Database error deleting subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error deleting subscription: {e}")
            raise

    def activate_subscription(self, subscription_id):
        try:
            subscription = self.get_subscription(subscription_id)
            if subscription:
                subscription.activate()
                return self.subscription_store.update_subscription(subscription_id, subscription)
            else:
                raise ValueError("Subscription not found")
        except OperationalError as e:
            logging.error(f"Database error activating subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error activating subscription: {e}")
            raise

    def cancel_subscription(self, subscription_id):
        try:
            subscription = self.get_subscription(subscription_id)
            if subscription:
                subscription.cancel()
                return self.subscription_store.update_subscription(subscription_id, subscription)
            else:
                raise ValueError("Subscription not found")
        except OperationalError as e:
            logging.error(f"Database error cancelling subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error cancelling subscription: {e}")
            raise

    def expire_subscription(self, subscription_id):
        try:
            subscription = self.get_subscription(subscription_id)
            if subscription:
                subscription.expire()
                return self.subscription_store.update_subscription(subscription_id, subscription)
            else:
                raise ValueError("Subscription not found")
        except OperationalError as e:
            logging.error(f"Database error expiring subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error expiring subscription: {e}")
            raise

    def update_subscription_status(self, subscription_id):
        try:
            subscription = self.get_subscription(subscription_id)
            if subscription:
                subscription.update_status()
                return self.subscription_store.update_subscription(subscription_id, subscription)
            else:
                raise ValueError("Subscription not found")
        except OperationalError as e:
            logging.error(f"Database error updating subscription status: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error updating subscription status: {e}")
            raise

    def get_active_subscriptions(self):
        try:
            return self.subscription_store.get_active_subscriptions()
        except OperationalError as e:
            logging.error(f"Database error getting active subscriptions: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting active subscriptions: {e}")
            raise

    def get_pending_subscriptions(self):
        try:
            return self.subscription_store.get_pending_subscriptions()
        except OperationalError as e:
            logging.error(f"Database error getting pending subscriptions: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting pending subscriptions: {e}")
            raise

    def get_expired_subscriptions(self):
        try:
            return self.subscription_store.get_expired_subscriptions()
        except OperationalError as e:
            logging.error(f"Database error getting expired subscriptions: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting expired subscriptions: {e}")
            raise

    def get_cancelled_subscriptions(self):
        try:
            return self.subscription_store.get_cancelled_subscriptions()
        except OperationalError as e:
            logging.error(f"Database error getting cancelled subscriptions: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting cancelled subscriptions: {e}")
            raise

    def get_subscription_by_user_id(self, user_id):
        try:
            return self.subscription_store.get_subscription_by_user_id(user_id)
        except OperationalError as e:
            logging.error(f"Database error getting subscription by user ID: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting subscription by user ID: {e}")
            raise

    def get_subscription_by_product_id(self, product_id):
        try:
            return self.subscription_store.get_subscription_by_product_id(product_id)
        except OperationalError as e:
            logging.error(f"Database error getting subscription by product ID: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting subscription by product ID: {e}")
            raise

    def get_subscription_by_status(self, status):
        try:
            return self.subscription_store.get_subscription_by_status(status)
        except OperationalError as e:
            logging.error(f"Database error getting subscription by status: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error getting subscription by status: {e}")
            raise