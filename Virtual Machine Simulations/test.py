import unittest
from libs import *

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.cred = Credentials('username', 'password', 'domain')

    def test_1(self):
        self.assertEqual(self.cred.username, 'username')
        self.assertEqual(self.cred.password, 'password')
        self.assertEqual(self.cred.domain, 'domain')


class TestMountPoint(unittest.TestCase):
    def setUp(self):
        self.cred = MountPoint('c:\\', 50)

    def test_1(self):
        self.assertEqual(self.cred.mountname, 'c:\\')
        self.assertEqual(self.cred.totalsize, 50)


if __name__ == '__main__':
    unittest.main()
