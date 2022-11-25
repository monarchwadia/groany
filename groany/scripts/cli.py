import cmd
from groany import groany

class GroanyCLI(cmd.Cmd):
  """Simple command processor example."""
  
  def default(self, line: str):
    result = groany(line)
    if result is None:
      print("No jokes found.")
    else:
      joke_str = result["joke"]
      print (joke_str)
    
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