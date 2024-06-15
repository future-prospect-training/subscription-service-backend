import enum

from ..extensions import db


class SubscriptionState(enum.Enum):
    pending = "pending"
    active = "active"
    cancelled = "cancelled"
    expired = "expired"


class Subscription(db.Model):
    def __init__(
        self,
        created_at,
        updated_at,
        activated_at,
        cancelled_at,
        expires_at,
        current_period_started_at,
        current_period_ends_at,
        state,
    ):
        self.created_at = created_at
        self.updated_at = updated_at
        self.activated_at = activated_at
        self.cancelled_at = cancelled_at
        self.expires_at = expires_at
        self.current_period_started_at = current_period_started_at
        self.current_period_ends_at = current_period_ends_at
        self.state = state

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    activated_at = db.Column(db.DateTime)
    cancelled_at = db.Column(db.DateTime, nullable=True)
    expires_at = db.Column(db.DateTime, nullable=True)
    current_period_started_at = db.Column(db.DateTime)
    current_period_ends_at = db.Column(db.DateTime)
    state = db.Column(db.Enum(SubscriptionState))

    def to_dict(self):
        return {
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "activated_at": self.activated_at,
            "cancelled_at": self.cancelled_at,
            "expires_at": self.expires_at,
            "current_period_started_at": self.current_period_started_at,
            "current_period_ends_at": self.current_period_ends_at,
            "state": self.state.value,
        }
