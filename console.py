#!/usr/bin/python3
"""something"""


import cmd
class HBNBCommand(cmd.Cmd):
    """i willll"""
    def __init__(self):
        """"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_quit(self, arg):
        """ """
        return True
    
    def emptyline(self):
        """if enter is clicked it will pass
        """
        pass
    
    def help_quit(self):
        """  """
        print("Quit command to exit the program")
        
    def do_EOF(self, arg):
        """"""
        return True
        
    def help_EOF(self):
        """" """
        print("terminate")
        
    def do_help(self, arg):
        """To get help"""
        return super().do_help(arg)
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
        
    
