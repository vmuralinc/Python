from context import datastructures
import unittest

class SllNodeTestSuite(unittest.TestCase):
    """tests the SllNode class"""

    def setUp(self):
        pass

    def test_create_node_with_int_value(self):
        """Tests a node with an integer value"""
        self.node = datastructures.SllNode(5)
        self.assertEqual(self.node.value, 5)
        self.assertEqual(self.node.next, None)
    
    def test_create_node_with_string_value(self):
        """Tests a node with a string value"""
        self.node = datastructures.SllNode("abc")
        self.assertEqual(self.node.value, "abc")
        self.assertEqual(self.node.next, None)
    
    def test_create_node_with_none_value(self):
        """Tests a node with an integer value"""
        self.assertRaises(ValueError, datastructures.SllNode, None)
        
    def test_repr_node_with_int_value(self):
        """Tests __repr__ of a node with an integer value"""
        self.node = datastructures.SllNode(5)
        self.assertEqual(repr(self.node.value), "5")
    
    def test_repr_node_with_string_value(self):
        """Tests __repr__  of a node with a string value"""
        self.node = datastructures.SllNode("abc")
        self.assertEqual(repr(self.node.value), repr("abc"))

if __name__ == '__main__':
    unittest.main()