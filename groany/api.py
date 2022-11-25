from requests import get;
from urllib import parse;
from typing import TypedDict

# Static types

class Joke(TypedDict):
  id: str
  joke: str
  status: int

class JokeSearchResults(TypedDict):
  current_page: int
  limit: int
  next_page: int
  previous_page: int
  results: list[Joke]
  search_term: str
  status: int
  total_jokes: int
  total_pages: int

# Methods

def api_search(prompt: str) -> JokeSearchResults:
  url = "https://icanhazdadjoke.com/search?term=" + parse.quote(prompt)
  headers = {"Accept": "application/json"}
  response = get(url, headers=headers)
  return response.json()