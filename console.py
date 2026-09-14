#!/usr/bin/python3
"""This module defines the HBnB console command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "
    __classes = [
        "BaseModel", "User", "State", "City",
        "Amenity", "Place", "Review"
    ]

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Create a new instance with given parameters and print its id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        obj = eval(args[0])()
        for param in args[1:]:
            if "=" not in param:
                continue
            key, value = param.split("=", 1)
            if value.startswith('"'):
                value = value[1:]
                if value.endswith('"'):
                    value = value[:-1]
                value = value.replace('\\"', '"').replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue
            setattr(obj, key, value)
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Print the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        print(objs[key])

    def do_destroy(self, line):
        """Delete an instance based on class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        del objs[key]
        storage.save()

    def do_all(self, line):
        """Print all string representations of all instances."""
        args = line.split()
        objs = storage.all()
        if not args:
            print([str(v) for v in objs.values()])
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in objs.items()
               if k.startswith(args[0] + ".")])

    def do_update(self, line):
        """Update an instance based on class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objs[key]
        attr_name = args[2]
        attr_val = args[3].strip('"')
        try:
            attr_val = int(attr_val)
        except ValueError:
            try:
                attr_val = float(attr_val)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
