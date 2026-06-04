"""The entity graph the factories assemble. Java JavaBeans -> Python dataclasses.
(Grouped into one module, which is the idiomatic Python equivalent of Java's
one-class-per-file package.)"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class User:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    username: str | None = None
    password: str | None = None
    email: str | None = None
    status: bool = False
    approved: bool = False
    list_name: str | None = None
    name: str | None = None
    last_name: str | None = None
    organization: str | None = None
    roles: list[UserRole] | None = None
    categories: list[UserCategory] | None = None
    configurations: list[Configuration] | None = None
    internal: bool = False


@dataclass
class Role:
    resource_id: str | None = None
    deleted: bool = False
    name: str | None = None
    user_roles: list[UserRole] | None = None
    privileges: list[RolePrivilege] | None = None


@dataclass
class Category:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    name: str | None = None
    user_categories: list[UserCategory] | None = None


@dataclass
class Privilege:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    name: str | None = None
    role_privileges: list[RolePrivilege] | None = None


@dataclass
class Configuration:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    user: User | None = None


@dataclass
class UserRole:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    role: Role | None = None
    user: User | None = None


@dataclass
class UserCategory:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    category: Category | None = None
    user: User | None = None


@dataclass
class RolePrivilege:
    id: int | None = None
    entity_id: str | None = None
    deleted: bool = False
    privilege: Privilege | None = None
    role: Role | None = None
