from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class User:
    """A data object with many fields, consumed by UserProcessor.
    The Java version exposed getters only; here they are plain dataclass attributes."""
    age: int = 0
    experience: int = 0
    certifications: list[str] = field(default_factory=list)
    last_login_days: int = 0
    failed_logins: int = 0
    background_check: bool = False
    compliance_training: bool = False
    financial_clearance: bool = False
    audit_score: int = 0
    general_training: bool = False
    account_age: int = 0
    trial_days_remaining: int = 0
    suspension_reason: str | None = None
    parental_consent: bool = False
