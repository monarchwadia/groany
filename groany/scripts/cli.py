import cmd
from groany import groany

prompt = "What kind of dad joke are you in the mood for?"

class GroanyCLI(cmd.Cmd):
  """Simple command processor example."""

  intro = 'Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\n' + prompt
  prompt = '(groany)> '
  file = None
  
  def default(self, line: str):
    'Get a funny joke based on your input.'
    result = groany(line)
    if result is None:
      print("No jokes found.")
    else:
      joke_str = result["joke"]
      print (joke_str)
    
  def emptyline(self):
    'Get a random funny joke.'
    result = groany(None)
    if result is None:
      print("No jokes found.")
    else:
      joke_str = result["joke"]
      print (joke_str)
    return False

  def do_funny(self, line: str):
    return True
    
  def postloop(self) -> None:
    print ("Goodbye!")

  def postcmd(self, stop: bool, line: str) -> bool:
    print(prompt)
    return stop

def exec():
  GroanyCLI().cmdloop()

if __name__ == "__main__":
  exec()