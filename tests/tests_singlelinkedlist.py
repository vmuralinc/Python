from context import datastructures
import unittest

class SingleLinkedListTestSuite(unittest.TestCase):
    """tests the SllNode class"""

    def setUp(self):
        pass

    def test_create_node_with_int_value(self):
        """Tests a node with an integer value"""
        self.node = datastructures.SllNode(5)
        self.assertEqual(self.node.value, 5)
        self.assertEqual(self.node.next, None)

if __name__ == '__main__':
    unittest.main()