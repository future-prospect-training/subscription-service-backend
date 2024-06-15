from ..models.Subscription import Subscription
from ..stores.SubscriptionStore import SubscriptionStore


class SubscriptionManager:
    def get_all_subscriptions(self):
        return SubscriptionStore.get_all_subscriptions()

    @staticmethod
    def get_subscription(subscription_id):
        return SubscriptionStore.get_subscription(subscription_id)

    @staticmethod
    def create_subscription(
        subscription_create_dto,
    ):  # dto stands for data transfer object
        created_at = subscription_create_dto.get("created_at")
        updated_at = subscription_create_dto.get("updated_at")
        activated_at = subscription_create_dto.get("activated_at")
        cancelled_at = subscription_create_dto.get("cancelled_at")
        expires_at = subscription_create_dto.get("expires_at")
        current_period_started_at = subscription_create_dto.get(
            "current_period_started_at"
        )
        current_period_ends_at = subscription_create_dto.get("current_period_ends_at")
        state = subscription_create_dto.get("state")

        subscription = Subscription(
            created_at=created_at,
            updated_at=updated_at,
            activated_at=activated_at,
            cancelled_at=cancelled_at,
            expires_at=expires_at,
            current_period_started_at=current_period_started_at,
            current_period_ends_at=current_period_ends_at,
            state=state,
        )

        return SubscriptionStore.save_subscription(subscription)


    @staticmethod
    def update_subscription(subsciption_id, subscription_update_dto):
        return SubscriptionStore.update_subscription(subsciption_id, subscription_update_dto)