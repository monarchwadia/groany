from api import api_search;
from parser import parse_arguments;

def get_unique_joke(api_search_results):
  return api_search_results["results"][0]

args = parse_arguments();
response = api_search(args.prompt)
joke = get_unique_joke(response)

print (joke)
