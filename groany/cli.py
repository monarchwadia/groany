from groany import groany
from argparse import ArgumentParser;

def parse_arguments(args):
  parser = ArgumentParser(
    prog="groany-jokes-cli",
    description="Dad jokes to make you groan, right in your terminal."
  )

  parser.add_argument('prompt')

  return parser.parse_args();

def exec_cli(sys_args):
  args = parse_arguments(sys_args);
  result = groany(args.prompt)
  return result