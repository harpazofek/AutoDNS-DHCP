# tests/test_name_to_ip_mapper.py
import unittest
from unittest.mock import MagicMock
from name_to_ip_mapper import NameToIPMapper

class TestNameToIPMapper(unittest.TestCase):

    def test_add_mapping(self):
        mapper = NameToIPMapper()
        mapper.add_mapping("example", "192.168.1.1")
        # Add assertions to check if the mapping was added correctly
        
    def test_get_ip_by_name(self):
        mapper = NameToIPMapper()
        mapper.add_mapping("example", "192.168.1.1")
        ip = mapper.get_ip_by_name("DefaultGroup", "example")
        self.assertEqual(ip, "192.168.1.1")
        
    # Add more test methods here...

if __name__ == '__main__':
    unittest.main()
