#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test"""
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        """Tear down the test"""
        del self.console
        storage._FileStorage__objects = {}
        self.mock_stdout.close()

    def capture_stdout(self):
        """Capture the stdout for testing"""
        sys.stdout = self.mock_stdout

    def release_stdout(self):
        """Release the stdout after testing"""
        sys.stdout = sys.__stdout__

    @patch('sys.stdin', StringIO('create BaseModel\n'))
    def test_create(self):
        """Test create command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'creates an instance of BaseModel and prints its ID')

    @patch('sys.stdin', StringIO('update BaseModel\n'))
    def test_update(self):
        """Test update command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)')

    @patch('sys.stdin', StringIO('show BaseModel\n'))
    def test_show(self):
        """Test show command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'prints the string representation of an instance based on the class name and id')

    @patch('sys.stdin', StringIO('destroy BaseModel\n'))
    def test_destroy(self):
        """Test destroy command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'deletes an instance based on the class name and id (save the change into the JSON file)')

    @patch('sys.stdin', StringIO('all BaseModel\n'))
    def test_all(self):
        """Test all command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'prints all string representation of all instances based or not on the class name')

    @patch('sys.stdin', StringIO('count BaseModel\n'))
    def test_count(self):
        """Test count command"""
        self.capture_stdout()
        self.console.cmdloop()
        self.release_stdout()
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, 'retrieve the number of instances of a class')

    @patch('sys.stdin', StringIO('EOF\n'))
    def test_EOF(self):
        """Test EOF command"""
        with self.assertRaises(SystemExit):
            self.console.cmdloop()


if __name__ == '__main__':
    unittest.main()

