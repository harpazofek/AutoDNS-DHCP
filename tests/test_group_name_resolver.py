# tests/test_group_name_resolver.py
import unittest
from group_name_resolver import GroupNameResolver

class TestGroupNameResolver(unittest.TestCase):

    def test_determine_group_name(self):
        resolver = GroupNameResolver()
        group = resolver.determine_group_name("GR_example")
        self.assertEqual(group, "Something")
        
    # Add more test methods here...

if __name__ == '__main__':
    unittest.main()