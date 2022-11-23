import json
from pathlib import Path

def default_state():
  return {
    "used_joke_ids": []
  }

def get_json_state():
  file_path = Path(Path.home(), ".groany")

  if not file_path.exists():
    file_path.touch()
    file_path.write_text(json.dumps(default_state))

  return json.loads(file_path.read_text())
  

def save_used(joke):
  file_path = Path(Path.home(), ".groany")

  state_json;

  if not file_path.exists():

    file_path.touch()
    file_path.write_text(json.dumps(default_state))
  
  path.touch()

