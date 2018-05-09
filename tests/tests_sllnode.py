from context import datastructures
import unittest

class SllNodeTestSuite(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_node_with_int_and_none(self):
        self.node = datastructures.SllNode(5)
        self.assertEqual(self.node.value, 5)
        self.assertEqual(self.node.next, None)

if __name__ == '__main__':
    unittest.main()