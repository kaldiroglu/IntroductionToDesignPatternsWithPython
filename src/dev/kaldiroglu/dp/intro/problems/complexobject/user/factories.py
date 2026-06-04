"""Faithful ports of the Java factory stubs: each is intentionally unimplemented and
returns None - the "before" picture the course refactors."""


class UserFactory:
    def create_user_from_request(self, user_request, username, user_resource_id,
                                 remote_addr, user_agent):
        user = None
        # ...
        return user


class RoleFactory:
    def create_user_role_from_request(self, role_entity_id, username, user_entity_id,
                                      remote_addr, user_agent):
        user_role = None
        # ...
        return user_role


class UserCategoryFactory:
    # Method name keeps the Java original's spelling ("catagory") so the port mirrors
    # the source repo exactly; UserService calls it under that name.
    def create_catagory_from_request(self, discipline_resource_id, username,
                                     user_entity_id, remote_addr, header):
        user_category = None
        # ...
        return user_category


class ConfigurationFactory:
    def create_configuration_from_request(self, configuration_entity_id, username,
                                          user_entity_id, remote_addr, header):
        configuration = None
        #
        return configuration
