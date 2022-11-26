#!/usr/bin/python3
"""something"""


import cmd
class HBNBCommand(cmd.Cmd):
    """i willll"""
    prompt = "(hbnb) "
        
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

    def emptyline(self):
        """    """
        pass
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
        
    
