import groany.unique as unique
from . import api;

def groany_random() -> api.Joke | None:
  retries = 5
  while retries > 0:
    joke = api.random()

    # Don't return a joke if it is already used
    if unique.joke_is_used(joke):
      retries -= 1
      continue
  
    # Found a unique joke. Return it.
    unique.joke_mark_as_used(joke)
    return joke
  
  # No unique jokes found after 5 retries.
  return None;


def groany_with_term(term: str) -> api.Joke | None:
  # Don't return a joke if the prompt is empty.
  if term is None or term == "":
    return None

  page = 1
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
      if unique.joke_is_used(joke):
        continue
      
      # found a unique joke. return.
      unique.joke_mark_as_used(joke)
      return joke
    
    # The loop completed without finding a unique joke. Try the next page, unless there are no more pages.
    if results["next_page"] == results["current_page"]:
      # There are no more pages. No results found.
      return None
    
    # Continue the loop with the next page.
    page = results["next_page"]
    continue


def groany(term: str | None) -> api.Joke | None:
  if term is None or term == "":
    return groany_random()
  else:
    return groany_with_term(term)
