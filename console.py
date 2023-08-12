#!/usr/bin/python3 
"""Module for the entry point of the command line interpreter."""

import cmd 
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command line interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, line):
        """Creates an instance of a new object
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, args):
        """Prints the string representation of the instance created
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            commands = args.split(' ')
            if commands[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(comands[0], commands[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes the created instance based on the class name and id.
        """
        if args == "" or args is None:
            print("** class name missing **")
        else:
            commands = args.split(' ')
            if commands[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(commands) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(commands[0], commands[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
    def do_all(self, args):
        """Prints the string representation of all instances created
        """
        if args != "":
            commands =args.split(' ')
            if commands[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                ln = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == commands[0]]
                print(ln)
        else:
            new_string = [str(obj) for key, obj in storage.all().items()]
            print(new_string)

    def do_count(self, args):
        """Counts the instances created in the class.
        """
        commands = args.split(' ')
        if not commands[0]:
            print("** class name missing **")
        elif commands[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    commands[0] + '.')]
            print(len(matches))

    def do_update(self, command_input):
        """Updates an instance by adding or updating attributes.
        """

        if not command_input or command_input == "":
            print("** class name missing **")
            return

        #passing input using regular expression
        regex_pattern = (
                r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
                )
        match = re.search(regex_pattern, command_input)
        class_name = match.group(1)
        instance_id = match.group(2)
        attribute_name = match.group(3)
        value = match.group(4)

        # Handling different cases
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif instance_id is None:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(class_name, instance_id)
            if instance_key not in storage.all():
                print("** no instance found **")
            elif not attribute_name:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                    attributes = storage.attributes()[class_name]
                    if attribute_name in attributes:
                        value = attributes[attribute_name](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass # It's fine, keep value as a string
                    setattr(storage.all()[instance_key], attribute_name, value)
                    storage.all()[instance_key].save()

    def update_dict(self, class_name, instance_id, s_dict):
        """Helper method for update() with a dictionaryin it"""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not class_name:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif instance_id is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[class_name]
                for attribute_name, value in d.items():
                    if attribute_name in attributes:
                        value = attributes[attribute_name](value)
                    setattr(storage.all()[key], attribute_name, value)
                storage.all()[key].save()

    def _precmd(self, line):
        """Intercepts and processes special commands"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line

        classname, method, args = match.groups()
        uid = ""
        attr_or_dict = ""

        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid, attr_or_dict = match_uid_and_args.groups()

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            if attr_or_dict.startswith('{') and attr_or_dict.endswith('}'):
                self.update_dict(classname, uid, attr_or_dict)
                return ""
            match_attr_and_value = re.search(
                    '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_part1 = match_attr_and_value.group(1) or ""
                attr_part2 = match_attr_and_value.group(2) or ""
                attr_and_value = attr_part1 + " " + attr_part2

            command = f"{method} {classname} {uid} {attr_and_value}"
            self.onecmd(command)
            return command

    def default(self, line):
        """use commands if no matches found"""
        self._precmd(line)

    def do_quit(self, args):
        """quit the console"""
        return True

    def do_EOF(self, args):
        """handles End Of File"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
