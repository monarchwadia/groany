from requests import get;
from urllib import parse;
from groany.api_types import Joke, JokeSearchParams, JokeSearchResults

def random() -> Joke:
  url = "https://icanhazdadjoke.com/"
  headers = {"Accept": "application/json"}
  response = get(url, headers=headers)
  return response.json()

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

