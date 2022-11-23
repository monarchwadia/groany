from requests import get;
from urllib import parse;

def api_search(prompt):
  quoted_prompt = parse.quote(prompt)
  return get("https://icanhazdadjoke.com/search?term=" + quoted_prompt, headers={"Accept": "application/json"})