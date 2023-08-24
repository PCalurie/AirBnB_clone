#!/usr/bin/env python3
"""Module for the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(command_input):
    """
    Parse the command input using shlex.split().

    Args:
        command_input (str): The input command to be parsed.

    Returns:
        list: A list of parsed arguments extracted from the command input,
              or an empty list if parsing fails.
    """
    try:
        args = shlex.split(command_input)
        return args
    except ValueError:
        return []


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        """
        arg_list = parse(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all instances"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_l = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_l.append(obj.__str__())
                elif len(args) == 0:
                    obj_l.append(obj.__str__())
            print(obj_l)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        arg_list = parse(arg)
        num = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                num += 1
        print(num)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        arg_list = parse(arg)
        obj_dict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            attribute_name = arg_list[2]
            if attribute_name in obj.__class__.__dict__.keys():
                attribute_type = type(obj.__class__.__dict__[attribute_name])
                obj.__dict__[attribute_name] = attribute_type(arg_list[3])
            else:
                obj.__dict__[attribute_name] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            attributes = eval(arg_list[2])
            for key, value in attributes.items():
                if (key in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[key]) in {str, int, float}):
                    attribute_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = attribute_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
