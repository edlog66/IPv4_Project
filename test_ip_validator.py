import unittest
from ip_validator import classify_ip, get_network_info

class TestIPValidator(unittest.TestCase):

    def test_valid_ipv4(self):
        self.assertEqual(classify_ip("192.168.0.1"), "IPv4")

    def test_valid_ipv6(self):
        self.assertEqual(classify_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"), "IPv6")

    def test_invalid_ip(self):
        self.assertEqual(classify_ip("300.300.300.300"), "Invalid")

    def test_valid_network(self):
        result = get_network_info("192.168.1.0/24")
        self.assertEqual(result["Network"], "192.168.1.0")

    def test_invalid_network(self):
        self.assertEqual(get_network_info("999.999.999.999/24"), "Invalid Network")


if __name__ == "__main__":
    unittest.main()
