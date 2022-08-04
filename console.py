#!/usr/bin/python3
"""The console module of AIRBNB project"""
import cmd
import json

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """HBnB Console.
    See https://docs.python.org/3/library/cmd.html\
        for more details
    Attr:
        custom_prompt (str): command line prompt
    """

    prompt = '(hbnb) '
    file = None
    __classes = [
        'BaseModel'
    ]

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

    def do_create(self, arg):
        """Creates a new instance of given model, saves it (to the JSON file)
and prints the id\n
Usage: create MyModel
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print(" ** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            print(new_obj.id)
            new_obj.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
name and id.\n
Usage: show BaseModel 1234-1234-1234
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print(" ** class doesn't exist **")
        elif len(args) == 1:
            print(" ** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
(save the change into the JSON file)\n
Usage: destroy BaseModel 1234-1234-1234
        """

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print(" ** class doesn't exist **")
        elif len(args) == 1:
            print(" ** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
            else:
                del objects[key]
                new_objects = {
                    key: objects[key].to_dict() for key in objects.keys()
                }
                with open(FileStorage._FileStorage__file_path, "w") as f:
                    f.write(json.dumps(new_objects))
                storage.reload()

    def do_all(self, arg):
        """Prints all string representation of all instances based
or not on the class name\n
Usage: all BaseModel or all.
        """

        args = parse(arg)
        objs = storage.all()
        if len(args) == 1:
            if args[0] not in self.__classes:
                print(" ** class doesn't exist **")
            else:
                filter_objs = [
                    str(objs[key]) for key in objs.keys() if args[0] in key
                ]
                print(filter_objs)
        else:
            objs = [
                str(value) for value in objs.values()
            ]
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
updating attribute (save the change into the JSON file)\n
Usage: update update <class name> <id> <attribute name> "<attribute value>"
"""

        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print(" ** class doesn't exist **")
        elif len(args) == 1:
            print(" ** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objects.keys():
                print("** no instance found **")
            else:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(objects[key], args[2], args[3])
                    objects[key].save()


def parse(arg):
    """
    Method written to take and parse input before use
    """

    args = arg.split(' ')
    args = [arg for arg in args if len(arg) > 0]
    return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
