# tests/test_dns_group.py
import unittest
from dns_group import DNSGroup

class TestDNSGroup(unittest.TestCase):

    def test_dns_group_initialization(self):
        group = DNSGroup("TestGroup")
        self.assertEqual(group.group_name, "TestGroup")
        
    # Add more test methods here...

if __name__ == '__main__':
    unittest.main()