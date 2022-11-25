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

class JokeSearchParams(TypedDict):
  term: str
  page: int | None
  limit: int | None

# Methods

def search(params: JokeSearchParams) -> JokeSearchResults:
  term = params["term"]
  page = params["page"]
  limit = params["limit"]

  url = "https://icanhazdadjoke.com/search?term=" + parse.quote(term)

  if page != None and page > 1:
    url += "&page=" + str(page)

  if limit != None:
    url += "&limit=" + str(limit)

  headers = {"Accept": "application/json"}
  response = get(url, headers=headers)
  return response.json()

