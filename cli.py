from argparse import ArgumentParser;
from requests import get;
from urllib import parse;

def api_search(prompt):
  # HTTP post request
  quoted_prompt = parse.quote(prompt)
  return get("https://icanhazdadjoke.com/search?term=" + quoted_prompt, headers={"Accept": "application/json"})

parser = ArgumentParser(
  prog="groany-jokes-cli",
  description="Dad jokes to make you groan, right in your terminal."
)

parser.add_argument('prompt')

args = parser.parse_args();

response = api_search(args.prompt)

print (response.text)
