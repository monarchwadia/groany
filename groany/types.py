from typing import TypedDict

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

class GroanyJson(TypedDict):
  used_joke_ids: list[str]
