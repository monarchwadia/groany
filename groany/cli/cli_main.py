from .parser import parse_arguments
from groany import groany

def cli_main(sys_args):
  args = parse_arguments(sys_args);
  result = groany(args.prompt)
  return result