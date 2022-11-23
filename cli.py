from argparse import ArgumentParser;

parser = ArgumentParser(
  prog="groany-jokes-cli",
  description="Dad jokes to make you groan, right in your terminal."
)

parser.add_argument('prompt')

args = parser.parse_args();

print(args.prompt)