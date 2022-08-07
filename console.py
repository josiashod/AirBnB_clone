#!/usr/bin/python3
"""The console module of AIRBNB project"""
import cmd
import json
import re
import shlex

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


def parse(arg):
    """
    Method written to take and parse input before use
    """
    brackets_arg = re.search(r'\{.*\}', arg)
    if brackets_arg:
        args = shlex.split(arg)
        args = [args[0], args[1].strip(','), brackets_arg.group(0)]
    else:
        args = shlex.split(arg)
        args = [arg.strip(',') for arg in args]
    return args


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details
    Attr:
        custom_prompt (str): command line prompt
    """

    prompt = '(hbnb) '
    __classes = [
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
    ]

    def default(self, line: str):
        """HBnB default command to handle model method"""

        a = line.split('.')
        if a[0] in HBNBCommand.__classes and len(a) == 2:
            _a = re.match(r"(?P<func>\w+)\((?P<params>(\".*\"?,?)?)\)", a[1])
            try:
                func = _a.group('func')
                params = _a.group('params')
                eval('HBNBCommand.do_' + func)(f"{a[0]} {params}")
            except Exception:
                return super().default(line)
        else:
            return super().default(line)

    def emptyline(self):
        """Ignore empty lines + ENTER."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """

        print("")
        return True

    def do_quit(self, arg):
        """Quitjosiashodcommand to exit the program
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of given model, saves it (to the JSON file)
        and prints the id

        Usage: create <class name>
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        else:
            new_obj = eval(args[0])()
            print(new_obj.id)
            new_obj.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.

        Usage: show <class name> <id>
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        elif len(args) == 1:
            print(" ** instance id missing **")
            return False
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
                return False
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)

        Usage: destroy <class name> <id>
        """

        objects = storage.all()
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        elif len(args) == 1:
            print(" ** instance id missing **")
            return False
        elif f"{args[0]}.{args[1]}" not in objects:
            print("** no instance found **")
            return False
        else:
            del objects[f"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name

        Usage: all <class name> or all.
        """

        args = parse(arg)
        objs = storage.all()
        if len(args) == 1 and args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        else:
            if len(args) == 1 and args[0] not in HBNBCommand.__classes:
                objs = [
                    str(objs[key]) for key in objs.keys() if args[0] in key
                ]
            else:
                objs = [
                    str(value) for value in objs.values()
                ]
            print(objs)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        elif len(args) == 1:
            print(" ** instance id missing **")
            return False
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
                return False
            else:
                if len(args) == 2:
                    print("** attribute name missing **")
                    return False
                elif len(args) == 3:
                    attr_dict = eval(args[2])
                    if type(attr_dict) != dict:
                        print("** value missing **")
                        return False
                    else:
                        for key_at in attr_dict.keys():
                            setattr(objects[key], key_at, attr_dict[key_at])
                        objects[key].save()
                else:
                    setattr(objects[key], args[2], args[3])
                    objects[key].save()

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class

        Usage: count <class name>
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print(" ** class doesn't exist **")
            return False
        else:
            objs = storage.all()
            filter_objs = [
                str(objs[key]) for key in objs.keys() if args[0] in key
            ]
            print(len(filter_objs))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
