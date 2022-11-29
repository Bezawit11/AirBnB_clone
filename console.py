#!/usr/bin/python3
"""something"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

class HBNBCommand(cmd.Cmd):
    """i willll"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'Review': Review, 'User': User,
                'Amenity': Amenity, 'City': City, 'State': State,
                 'Place': Place}

    def do_help(self, arg):
        """To get help
        """
        return super().do_help(arg)

    def do_EOF(self, line):
        """  """
        print("")
        return True

    def do_quit(self, arg):
        """  """
        return True

    def help_quit(self):
        """  """
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """ """
        pass

    def emptyline(self):
        """    """
        pass

    def do_create(self, arg):
        """  """
        if arg:
            for a in HBNBCommand.classes.keys():
                if arg == a:
                    o = HBNBCommand.classes[a]()
                    o.save()
                    print(o.id)
                    return
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """   """
        if arg:
            a = arg.split()
            for h in HBNBCommand.classes.keys():
                if h == a[0]:
                    if len(a) < 2:
                        print("** instance id missing **")
                        return
                    con = "{}.{}".format(a[0], a[1])
                    d = storage.all()
                    for k in d.keys():
                        if k == con:
                            print(d[k])
                            return
                    print("** no instance found **")
                    return
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """    """
        o = storage.all()
        lk = []
        if arg:
            a = arg.split()
            for h in HBNBCommand.classes.keys():
                if h == a[0]:
                    lk.append(o)
                    print(lk)
                    return
            print("** class doesn't exist **")
            return
        lk.append(o)
        print(lk)

    def do_destroy(self, arg):
        """ """
        if arg:
            a = arg.split()
            for h in HBNBCommand.classes.keys():
                if h == a[0]:
                    if len(a) < 2:
                        print("** instance id missing **")
                        return
                    con = "{}.{}".format(a[0], a[1])
                    d = storage.all()
                    for k in d.keys():
                        if k == con:
                            del d[k]
                            storage.save()
                            return
                    print("** no instance found **")
                    return
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id.
        """
        if arg:
            a = arg.split()
            for h in HBNBCommand.classes.keys():
                if h == a[0]:
                    if len(a) < 2:
                        print("** instance id missing **")
                        return
                    con = "{}.{}".format(a[0], a[1])
                    d = storage.all()
                    for k in d.keys():
                        if k == con:
                            if len(a) < 3:
                                print("** attribute name missing **")
                                return
                            if len(a) < 4:
                                print("** value missing **")
                                return
                            d[k].__dict__[a[2]] = a[3]
                            storage.save()
                            return
                    print("** no instance found **")
                    return
            print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
