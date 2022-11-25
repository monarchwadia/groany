from typing import TypedDict
from . import api;

used_joke_ids: list[str] = []

class GroanyParams(TypedDict):
  term: str | None
  page: int

def groany(params: GroanyParams) -> api.Joke | None:
  term = params["term"]
  page = params["page"]

  # Don't return a joke if the prompt is empty.
  if term is None or term == "":
    return None

  while True:
    LIMIT = 30

    results = api.search({
      "term": term,
      "page": page,
      "limit": LIMIT
    })

    # Don't return a joke if there are no results.
    if results["total_jokes"] == 0:
      return None

    # Loop over all results and return the first one that hasn't been used.
    for joke in results["results"]:

      # don't repeat jokes
      if joke["id"] in used_joke_ids:
        continue
      
      # found a unique joke. return.
      used_joke_ids.append(joke["id"])
      return joke
    
    # The loop completed without finding a unique joke. Try the next page, unless there are no more pages.
    if results["next_page"] == results["current_page"]:
      # There are no more pages. No results found.
      return None
    
    # Continue the loop with the next page.
    page = results["next_page"]
    continue


    
