from context import datastructures
import unittest

class SllNodeTestSuite(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_node_with_int_value(self):
        self.node = datastructures.SllNode(5)
        self.assertEqual(self.node.value, 5)
        self.assertEqual(self.node.next, None)
    
    def test_create_node_with_string_value(self):
        self.node = datastructures.SllNode("abc")
        self.assertEqual(self.node.value, "abc")
        self.assertEqual(self.node.next, None)
    
    def test_create_node_with_none_value(self):
        self.assertRaises(ValueError, datastructures.SllNode, None)
        
    def test_repr_node_with_int_value(self):
        self.node = datastructures.SllNode(5)
        self.assertEqual(repr(self.node.value), "5")
    
    def test_repr_node_with_string_value(self):
        self.node = datastructures.SllNode("abc")
        self.assertEqual(repr(self.node.value), repr("abc"))

if __name__ == '__main__':
    unittest.main()