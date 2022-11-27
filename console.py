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
from models.place import

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
                         print("** instance id missing ** ")
                         return
                    con = "{}.{}".format(a[0], a[1])
                    d = storage.all()
                    for k in d.keys():
                        if k == con:
                            print(d[k])
                            return
                print("** class doesn't exist ** ")
        else:
            print("** class name missing ** ")
    
        def do_all(self, arg):
            """    """
            o = storage.all()
            l = []
            if arg:
                a = arg.split()
                for h in HBNBCommand.classes.keys():
                    if h == a[0]:
                        l.append(o)
                        print(l)
                        return
                print("** class doesn't exist **")
                return
            l.append(o)
            print(l)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
