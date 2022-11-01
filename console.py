#!/usr/bin/python3
""" Defines the hbnh console """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    intro = " Welcome to my AirBnB "
    prompt = " (hbnh) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
