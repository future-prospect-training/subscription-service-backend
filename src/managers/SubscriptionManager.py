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
