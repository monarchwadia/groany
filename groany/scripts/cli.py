import cmd

class GroanyCLI(cmd.Cmd):
  """Simple command processor example."""
  
  def default(self, line: str):
    print ("<Filtered joke goes here>")
    
  def emptyline(self):
    print ("<Random joke goes here>")
    return False

  def do_funny(self, line: str):
    return True

  def do_EOF(self, line: str):
    return True
    
  def postloop(self) -> None:
    print ("Goodbye!")

if __name__ == "__main__":
  GroanyCLI().cmdloop()