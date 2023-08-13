# This module will contain the GroupNameResolver class
class GroupNameResolver:
    def __init__(self):
        self.prefix_to_group = {
            "GR": "Something",
            "LR": "AnotherGroup",
            "TP": "YetAnotherGroup"
        }
    
    def determine_group_name(self, name):
        for prefix, group_name in self.prefix_to_group.items():
            if name.startswith(prefix):
                return group_name
        return "DefaultGroup"
        