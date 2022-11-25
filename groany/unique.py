from groany.api_types import Joke

used_joke_ids: list[str] = []

def joke_is_used(joke: Joke) -> bool:
  return joke["id"] in used_joke_ids

def joke_mark_as_used(joke: Joke) -> None:
  used_joke_ids.append(joke["id"])
