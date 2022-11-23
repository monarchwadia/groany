from argparse import ArgumentParser;

def parse_arguments():
  parser = ArgumentParser(
    prog="groany-jokes-cli",
    description="Dad jokes to make you groan, right in your terminal."
  )

  parser.add_argument('prompt')

  return parser.parse_args();
  
