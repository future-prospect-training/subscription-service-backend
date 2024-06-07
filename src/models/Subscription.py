from ..extensions import db
import enum

class SubscriptionState(enum.Enum):
    pending = 'pending'
    active = 'active'
    cancelled = 'cancelled'
    expired = 'expired'

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    activated_at = db.Column(db.DateTime)
    cancelled_at = db.Column(db.DateTime, nullable = True)
    expires_at = db.Column(db.DateTime, nullable = True)
    current_period_started_at = db.Column(db.DateTime)
    current_period_ends_at = db.Column(db.DateTime)
    state = db.Column(db.Enum(SubscriptionState))
