import json
import os

def load_tools_config():
    config_path = os.path.join(os.path.dirname(__file__), 'tools.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("tools.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("tools.json is not properly formatted.")
        return {}
