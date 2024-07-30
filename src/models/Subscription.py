import enum
from datetime import datetime

from ..extensions import db


class SubscriptionState(enum.Enum):
    pending = "pending"
    active = "active"
    cancelled = "cancelled"
    expired = "expired"


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    def __init__(
        self,
        activated_at=None,
        cancelled_at=None,
        expires_at=None,
        current_period_started_at=None,
        current_period_ends_at=None,
        state=None,
    ):
        self.activated_at = activated_at
        self.cancelled_at = cancelled_at
        self.expires_at = expires_at
        self.current_period_started_at = current_period_started_at
        self.current_period_ends_at = current_period_ends_at
        self.state = state

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
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
            "state": self.state.value if self.state else None,
        }

    def activate(self):
        self.state = SubscriptionState.active
        self.activated_at = datetime.now()
        db.session.commit()

    def cancel(self):
        self.state = SubscriptionState.cancelled
        self.cancelled_at = datetime.now()
        db.session.commit()

    def expire(self):
        self.state = SubscriptionState.expired
        self.expires_at = datetime.now()
        db.session.commit()

    def update_status(self):
        if self.expires_at and self.expires_at < datetime.now():
            self.expire()
        elif self.cancelled_at and self.cancelled_at < datetime.now():
            self.cancel()
        elif self.activated_at and self.state == SubscriptionState.pending:
            self.activate()

    @classmethod
    def get_active_subscriptions(cls):
        return cls.query.filter_by(state=SubscriptionState.active).all()

    @classmethod
    def get_pending_subscriptions(cls):
        return cls.query.filter_by(state=SubscriptionState.pending).all()

    @classmethod
    def get_cancelled_subscriptions(cls):
        return cls.query.filter_by(state=SubscriptionState.cancelled).all()

    @classmethod
    def get_expired_subscriptions(cls):
        return cls.query.filter_by(state=SubscriptionState.expired).all()
