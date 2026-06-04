"""Faithful port of the Java UserService. It coordinates several factories to build a
User graph from a request. Because the factories are deliberately left as stubs (they
return None), this is the "complex object construction" smell the course uses to
motivate the Factory / Builder patterns."""

from .user.factories import (
    ConfigurationFactory,
    RoleFactory,
    UserCategoryFactory,
    UserFactory,
)


class UserService:
    def create_user(self, new_user_request, username, user_entity_id):
        user_factory = UserFactory()
        user_role_list = []
        user_categories = []
        configurations = []
        user = user_factory.create_user_from_request(
            new_user_request, username, user_entity_id,
            new_user_request.remote_addr, new_user_request.get_header("User-Agent"))

        role_factory = RoleFactory()
        if new_user_request.role_r_entity_ids:
            for role_entity_id in new_user_request.role_r_entity_ids:
                user_role = role_factory.create_user_role_from_request(
                    role_entity_id, username, user_entity_id,
                    new_user_request.remote_addr, new_user_request.get_header("User-Agent"))
                user_role.user = user
                user_role_list.append(user_role)
            user.roles = user_role_list

        user_category_factory = UserCategoryFactory()
        if new_user_request.category_entity_ids:
            for discipline_resource_id in new_user_request.category_entity_ids:
                user_category = user_category_factory.create_catagory_from_request(
                    discipline_resource_id, username, user_entity_id,
                    new_user_request.remote_addr, new_user_request.get_header("User-Agent"))
                user_category.user = user
                user_categories.append(user_category)
            user.categories = user_categories

        configuration_factory = ConfigurationFactory()
        if new_user_request.configuration_entity_ids:
            for configuration_entity_id in new_user_request.configuration_entity_ids:
                configuration = configuration_factory.create_configuration_from_request(
                    configuration_entity_id, username, user_entity_id,
                    new_user_request.remote_addr, new_user_request.get_header("User-Agent"))
                configuration.user = user
                configurations.append(configuration)
            user.configurations = configurations

        return user
