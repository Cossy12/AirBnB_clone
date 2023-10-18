#!/usr/bin/env python3
"""console"""

import cmd
import models
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }
dot_cmds = ['all', 'count', 'show', 'destroy', 'update']


class HBNBCommand(cmd.Cmd):
    """ the  hbnb """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ exit the program.\n"""

        return True

    def do_EOF(self, line):
        """EOF signal  exit  program."""

        print()
        return True

    def emptyline(self):
        """ do nothing"""
        pass

    def do_help(self, line):
        cmd.Cmd.do_help(self, line)

    def do_create(self, args):
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):

        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        all_instances = models.storage.all()
        found = False
        for key, instance in all_instances.items():
            if class_name in key and class_id in key:
                found = True
                print(instance)
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        "Delete a class  id."
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id is missing **")
            return

        found = False
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        instance = all_instances.pop(key)
        if instance:
            del (instance)
            models.storage.save()
            found = True
        if not found:
            print("** no instance found **")

    def do_all(self, args):
        "Usage: all or all <class> .all()\n        "

        args = args.split(" ")
        class_name = args[0]
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            all_instances = models.storage.all()
            for key, instances in all_instances.items():
                print([str(instances)])
        if class_name in classes:
            all_instances = models.storage.all()
            for key, instance in all_instances.items():
                if class_name in key:
                    print([str(instance)])

    def do_update(self, args):
        args = args.split()
        class_name = args[0]

        if len(args) < 1:
            print("** class name missing **")
            return
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        found = False
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        if len(args) < 3:
            print("** atribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

        for key, instance in all_instances.items():
            if instance_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance,
                            attribute_name,
                            attribute_value.strip('"'))
                    models.storage.save()

        if not found:
            print("** no instance found **")
            return

    def do_precmd(self, args):
        """Reformat  syntax.
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        if not ('.' in args and '(' in args and ')' in args):
            return args

        try:  
            fnpline = args[:]  # parsed line

            _cls = fnpline[:fnpline.find('.')]

            _cmd = fnpline[fnpline.find('.') + 1:fnpline.find('(')]
            if _cmd not in dot_cmds:
                raise Exception

            fnpline = fnpline[fnpline.find('(') + 1:fnpline.find(')')]
            if fnpline:
                fnpline = fnpline.partition(', ')  

                _id = fnpline[0].replace('\"', '')


                fnpline = fnpline[2].strip()  
                if fnpline:
                    if fnpline[0] == '{' and fnpline[-1] == '}' \
                            and type(eval(fnpline)) is dict:
                        _args = fnpline
                    else:
                        _args = fnpline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def do_count(self, args):
        count = 0
        all_instances = models.storage.all()
        for key, value in all_instances.items():
            if args[0] in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()


