import os

def list_env_vars():
    for key, value in os.environ.items():
        print(f"{key}: {value}")

list_env_vars()
