print("Script started")

import os

print("Script directory:", os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.json')
print("Config path:", config_path)
print("Config path exists?", os.path.exists(config_path))
