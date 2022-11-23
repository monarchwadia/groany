from requests import get;
from urllib import parse;

def api_search(prompt):
  url = "https://icanhazdadjoke.com/search?term=" + parse.quote(prompt)
  headers = {"Accept": "application/json"}
  response = get(url, headers=headers)
  return response.json()