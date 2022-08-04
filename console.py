#!/usr/bin/python3
"""The console module of AIRBNB project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details
    Attr:
        custom_prompt (str): command line prompt
    """

    prompt = '(hbnb) '
    file = None

    # ----- basic hbnb commands -----
    def do_EOF(self, arg):
        """EOF signal to exit the program
        """

        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True


def parse(arg):
    """
    Method written to take and parse input before use
    """
    return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
