import os
from groany.types import GroanyJson, Joke
from pathlib import Path
import json

# Mock this function in tests
def get_groany_home_path(): 
  return Path.home().joinpath(".groany")

# Mock this function in tests
def get_groany_json_filepath():
  return Path(get_groany_home_path()).joinpath("groany.json")

def _default_json() -> GroanyJson:
  return {
    "used_joke_ids": []
  }

def _exists_in_list(list: list[str], joke_id: str):
  for item in list:
    if item == joke_id:
      return True
  return False

def _read_groany_json():
  io = get_groany_json_filepath().open('r')
  groany_json: GroanyJson = json.load(io)
  io.close()
  return groany_json

def _exists_groany_json():
  return get_groany_json_filepath().exists()

def _delete_groany_json():
  os.remove(get_groany_json_filepath())

def _touch_groany_json():
  get_groany_home_path().mkdir(parents=True, exist_ok=True)
  get_groany_json_filepath().touch(exist_ok=True)
  get_groany_json_filepath().write_text(json.dumps((_default_json())))

# Public API

def joke_is_used(joke: Joke) -> bool:
  if not _exists_groany_json():
    _touch_groany_json()

  groany_json = _read_groany_json()
  return _exists_in_list(groany_json["used_joke_ids"], joke["id"])


def joke_mark_as_used(joke: Joke) -> None:
  if not _exists_groany_json():
    _touch_groany_json()

  if (joke_is_used(joke)):
    return;

  groany_json = _read_groany_json()
  groany_json["used_joke_ids"].append(joke["id"])
  _delete_groany_json()
  _touch_groany_json()
  io = get_groany_json_filepath().open('r+')
  io.write(json.dumps(groany_json))
  io.close()
