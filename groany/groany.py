from . import api;

def get_unique_joke(api_search_results):
  results = api_search_results["results"]
  if len(results) == 0:
    return None
  else:
    return results[0]


def groany(prompt):
  response = api.api_search(prompt)
  joke = get_unique_joke(response)
  return joke

