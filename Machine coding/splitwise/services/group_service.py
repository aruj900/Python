from splitwise.services.group_service_interface import GroupServiceInterface
from splitwise.models.group import Group

class GroupService(GroupServiceInterface):
    group_details = {}
    def add_group(self, id, name,members):
        group = Group(id,name,members)
        GroupService.group_details[id] = group
        return group