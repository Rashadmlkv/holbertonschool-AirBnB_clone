#!/usr/bin/python3
"""
    HBNB console entry point
"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB console."""
    
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(command[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split(".")[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            all_objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objects:
                print("** no instance found **")
                return
            else:
                instance = all_objects[key]
                setattr(instance, args[2], args[3])
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
