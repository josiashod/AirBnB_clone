#!/usr/bin/python3
"""
test module for console.py
"""

import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models


class TestHBNBCommand(unittest.TestCase):
    """testing the Console class."""

    def setUp(self):
        """unittest setup method"""
        self.test_c = HBNBCommand()

    def test_emptyline(self):
        """Checks empty line + ENTER"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_c.emptyline()
            self.assertEqual(f.getvalue(), "")
            self.assertEqual(self.test_c.prompt, "(hbnb) ")

    def test_do_EOF(self):
        """Checks EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_c.do_EOF("")
            self.assertEqual(f.getvalue(), "\n")
            self.assertEqual(self.test_c.prompt, "(hbnb) ")

    def test_do_quit(self):
        """Checks quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            # with self.assertRaises(SystemExit):
            self.test_c.do_quit("")

    def test_console_all(self):
        """Checks model all"""

        for classe in self.test_c._HBNBCommand__classes:
            objs = models.storage.all()
            objs = [
                str(objs[key]) for key in objs.keys() if classe in key
            ]
            with patch('sys.stdout', new=StringIO()) as f:
                self.test_c.default(f"{classe}.all()")
                self.assertEqual(eval(f.getvalue()), objs)

    def test_console_count(self):
        """Checks model count"""

        for classe in self.test_c._HBNBCommand__classes:
            objs = models.storage.all()
            objs = len([
                str(objs[key]) for key in objs.keys() if classe in key
            ])
            with patch('sys.stdout', new=StringIO()) as f:
                self.test_c.default(f"{classe}.count()")
                self.assertEqual(eval(f.getvalue()), objs)


if __name__ == "__main__":
    unittest.main()
