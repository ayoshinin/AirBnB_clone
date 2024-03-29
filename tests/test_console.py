#!/usr/bin/python3
"""Module for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
    """Test the HBNBCommand Console"""
    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        _s ="""

        self.assertEqual(_s, f.getvalue())

    # Test cases for quit

    def test_do_quit(self):
        """Tests the quit commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        # modelling what happens when someone types `quit`
        _msg = f.getvalue()
        self.assertTrue(len(_msg) == 0)
        self.assertEqual("", _msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        # modelling when user types `quit anything`
        _msg = f.getvalue()
        self.assertTrue(len(_msg) == 0)
        self.assertEqual("", _msg)

    # Test cases for EOF
    def test_do_EOF(self):
        """Tests the EOF commmand"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        # modelling what happens when user types `quit`
        _msg = f.getvalue().strip().split('\n')
        # self.assertTrue(len(msg) == 1)
        info = f"Expected length 1, got{len(msg)}.\nOutput:{msg}"
        self.assertEqual(len(_msg), 1, info)

    # Test cases for emptyline
    def test_do_emptyline(self):
        """Tests the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        # modelling what happens when user doesn't type anything
        _msg = f.getvalue()
        self.assertTrue(len(_msg) == 0)
        self.assertEqual("", _msg)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                     \n")
        # modelling when user types lots of whitespaces & enter
        _msg = f.getvalue()
        self.assertTrue(len(_msg) == 0)
        self.assertEqual("", _msg)

    # Test cases for do_all
    def test_do_all(self):
        """Tests the do_all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")

    # Test cases for do_count
    # Test cases for do_show
    # Test cases for do_create
    # Test cases for do_update
    # Test cases for do_destroy


if __name__ == "__main__": 
    unittest.main()

