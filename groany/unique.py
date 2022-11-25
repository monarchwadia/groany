import os
from groany.types import GroanyJson, Joke
from pathlib import Path
import json

groany_home_path = Path.home().joinpath(".groany")
groany_home_path.mkdir(parents=True, exist_ok=True)
groany_json_filepath = Path(groany_home_path).joinpath("groany.json")

def default_json() -> GroanyJson:
  return {
    "used_joke_ids": []
  }

def exists_in_list(list: list[str], joke_id: str):
  for item in list:
    if item == joke_id:
      return True
  return False

def read_groany_json():
  io = groany_json_filepath.open('r')
  groany_json: GroanyJson = json.load(io)
  io.close()
  return groany_json

def exists_groany_json():
  return groany_json_filepath.exists()

def delete_groany_json():
  os.remove(groany_json_filepath)

def touch_groany_json():
  groany_json_filepath.touch(exist_ok=True)
  groany_json_filepath.write_text(json.dumps((default_json())))

if not exists_groany_json():
  touch_groany_json() 

def joke_is_used(joke: Joke) -> bool:
  groany_json = read_groany_json()
  return exists_in_list(groany_json["used_joke_ids"], joke["id"])

def joke_mark_as_used(joke: Joke) -> None:
  if (joke_is_used(joke)):
    return;

  groany_json = read_groany_json()
  groany_json["used_joke_ids"].append(joke["id"])
  delete_groany_json()
  touch_groany_json()
  io = groany_json_filepath.open('r+')
  io.write(json.dumps(groany_json))
  io.close()
