import sys;
from groany.cli import exec_cli

result = exec_cli(sys.argv[1:])
print(result)