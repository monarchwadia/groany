import json
from pathlib import Path

def get_json_file_path():
  return Path(Path.home(), ".groany")

def read_file():
  file_path = get_json_file_path()

  if not file_path.exists():
    return None;

  return json.loads(file_path.read_text())