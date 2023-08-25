import json

#from loguru import logger



def write_to_json(file_path, data, mute_on_error = False):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except FileNotFoundError as e:
        print(f"{str(e)} while try to open \"{file_path}\"") if not mute_on_error else None
    except Exception as e:
        print(f"{str(e)} while write to txt file: \"{file_path}\"") if not mute_on_error else None
