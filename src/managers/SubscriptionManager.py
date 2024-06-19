import logging

from psycopg2 import OperationalError, ProgrammingError

from ..models.Subscription import Subscription
from ..stores.SubscriptionStore import SubscriptionStore

# Configure logging
logging.basicConfig(level=logging.ERROR)


class SubscriptionManager:
    def get_all_subscriptions(self):
        return SubscriptionStore.get_all_subscriptions()

    @staticmethod
    def get_subscription(subscription_id):
        return SubscriptionStore.get_subscription(subscription_id)

    @staticmethod
    def create_subscription(subscription_create_dto):
        # Input validation
        required_fields = [
            "created_at",
            "updated_at",
            "activated_at",
            "cancelled_at",
            "expires_at",
            "current_period_started_at",
            "current_period_ends_at",
            "state",
        ]
        missing_fields = [
            field for field in required_fields if field not in subscription_create_dto
        ]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        try:
            subscription = Subscription(
                created_at=subscription_create_dto.get("created_at"),
                updated_at=subscription_create_dto.get("updated_at"),
                activated_at=subscription_create_dto.get("activated_at"),
                cancelled_at=subscription_create_dto.get("cancelled_at"),
                expires_at=subscription_create_dto.get("expires_at"),
                current_period_started_at=subscription_create_dto.get(
                    "current_period_started_at"
                ),
                current_period_ends_at=subscription_create_dto.get(
                    "current_period_ends_at"
                ),
                state=subscription_create_dto.get("state"),
            )

            return SubscriptionStore.save_subscription(subscription)
        except OperationalError as e:
            logging.error(f"Database error creating subscription: {e}")
            raise
        except ProgrammingError as e:
            logging.error(f"Invalid SQL query: {e}")
            raise
        except Exception as e:
            logging.error(f"Error creating subscription: {e}")
            raise

    @staticmethod
    def update_subscription(subscription_id, subscription_update_dto):
        # Input validation
        if not subscription_update_dto:
            raise ValueError("subscription_update_dto cannot be empty")

        try:
            return SubscriptionStore.update_subscription(
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
