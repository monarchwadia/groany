from api import api_search;
from parser import parse_arguments;

args = parse_arguments();
response = api_search(args.prompt)
print (response.text)
