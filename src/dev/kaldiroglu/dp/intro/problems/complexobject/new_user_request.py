from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NewUserRequest:
    """The incoming request the UserService turns into a User graph."""
    username: str | None = None
    status: bool = False
    email: str | None = None
    approved: bool = False
    list_name: str | None = None
    name: str | None = None
    last_name: str | None = None
    organization: str | None = None
    role_r_entity_ids: list[str] | None = None
    category_entity_ids: list[str] | None = None
    configuration_entity_ids: list[str] | None = None
    internal: bool = False
    remote_addr: str | None = None

    # The Java original's getHeader(x) ignored its field and returned the argument;
    # setHeader was a stub. Preserved for fidelity.
    def get_header(self, header):
        return header

    def set_header(self, header, value):
        # ...
        pass
