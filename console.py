#!/usr/bin/python3
'''
Use cmd to create the console and prompt
'''
import cmd
import re
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

all_cls = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    '''
    class to set the consile prompt and functions
    '''
    prompt = "(hbnb)"

    def do_quit(self, arg):
        '''
        Quit command exits the program with a new line
        '''
        return True

    def do_EOF(self, arg):
        '''
        End of File command exits the program with a new line
        '''
        print()
        return True

    def emptyline(self):
        '''
        Handle empty line + Enter to do nothing
        '''
        pass

    def do_create(self, args):
        '''
        Update the def do_create(self, arg): function of command interpreter
        (console.py) to allow for object creation with given parameters
        '''

        commands = args.split()
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        obj = eval(commands[0])
        for command in commands[1:]:
            param = command.split("=")
            param_type = literal_eval(param[1])
            if type(param_type) is str:
                param[1] = param[1].strip('"').replace("_", " ")
                value = param[1]
            elif type(param_type) is int or type(param_type) is float:
                value = eval(param[1])
            setattr(obj, param[0], value)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        '''
        commands = arg.split()
        if not check_class(commands) or not check_inst(commands):
            return
        inst_dict = storage.all()
        if "{}.{}".format(commands[0], commands[1]) not in inst_dict:
            print("** no instance found **")
            return
        print(inst_dict["{}.{}".format(commands[0], commands[1])])

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        '''
        commands = arg.split()
        if not check_class(commands) or not check_inst(commands):
            return
        inst_dict = storage.all()
        if "{}.{}".format(commands[0], commands[1]) not in inst_dict:
            print("** no instance found **")
            return
        del inst_dict["{}.{}".format(commands[0], commands[1])]
        storage.save()

    def do_all(self, arg):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        '''
        commands = arg.split()
        all_dict = storage.all()
        all_list = []
        if commands and commands[0] not in all_cls.keys():
            print("** class doesn't exist **")
            return
        elif not commands:
            for value in all_dict.values():
                all_list.append(str(value))
            print(all_list)
        elif commands and commands[0] in all_cls.keys():
            for value in all_dict.values():
                if commands[0] == type(value).__name__:
                    all_list.append(str(value))
            print(all_list)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        '''
        commands = arg.split()
        if not check_class(commands) or not check_inst(commands):
            return
        inst_dict = storage.all()
        if "{}.{}".format(commands[0], commands[1]) not in inst_dict:
            print("** no instance found **")
            return
        if len(commands) < 3:
            print("** attribute name missing **")
            return
        if len(commands) < 4:
            print("** value missing **")
            return
        if len(commands) == 4:
            inst = inst_dict["{}.{}".format(commands[0], commands[1])]
            if commands[2] in inst.__class__.__dict__.keys():
                get_type = type(inst.__class__.__dict__[commands[2]])
                inst.__dict__[commands[2]] = get_type(commands[3])
            else:
                inst.__dict__[commands[2]] = commands[3]
        storage.save()


def check_class(commands):
    '''
    checks if class name is missing or doesn't exist
    '''
    if not commands:
        print("** class name missing **")
        return False
    if commands[0] not in all_cls.keys():
        print("** class doesn't exist **")
        return False
    return True


def check_inst(commands):
    '''
    checks if instance id is missing
    '''
    if len(commands) < 2:
        print("** instance id missing **")
        return False
    return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
