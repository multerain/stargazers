"""Test utilities.py"""
# pylint: disable=C,R,W
import unittest

import utilities


class TestInputToList(unittest.TestCase):

    def test_input_to_list_commas(self):
        """Test comma separated input to list."""
        comma_input = ','.join(['owner/repo'] * 100)
        response = utilities.input_to_list(comma_input)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 100)

    def test_input_to_list_spaces(self):
        """Test space separated input to list."""
        space_input = ' '.join(['owner/repo'] * 100)
        response = utilities.input_to_list(space_input)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 100)

    def test_input_to_list_single(self):
        """Test single entry to list."""
        single_input = 'owner/repo'
        response = utilities.input_to_list(single_input)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)

    def test_input_to_list_empty(self):
        """Test empty input."""
        empty_input = ''
        response = utilities.input_to_list(empty_input)
        self.assertEqual(response, None)


if __name__ == '__main__':
    unittest.main()
