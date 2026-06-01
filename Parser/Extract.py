from curses.ascii import isdigit

from .Data import Config

def validate_input(data: list):
    valid_inits = ["hub:", "connection:", "start_hub:", "end_hub:", "#"]
    for line in data:
        if not any(line.startswith(init) for init in valid_inits):
            raise ValueError(f"Invalid input format: line '{line}' does not start with a valid keyword.")

def clean_hub_data(hub_data: str, line: str) -> list:
    new_list: list = []
    hub_data = hub_data.split("#")[0].strip()
    split = hub_data.split(" ")

    print(f"Debug: Processing hub data '{hub_data}' from line '{line}'. Split into: {split}")
    print(len(split))
    #if len(split) > 4 or len(split) < 3:
    #    raise ValueError(f"Invalid input format: hub data must have 3 or 4 parameters in line '{line}'.")
    #if not split[0].isalpha():
    #    raise ValueError(f"Invalid input format: First parameter of hub must be a string in line '{line}'.")
    #new_list.append(split[0])
    #for param in range(1, 3):
    #    if not split[param].isdigit():
    #        raise ValueError(f"Invalid input format: expected a number at position {param} in hub data. From line: '{line}'")
    #    new_list.append(int(split[param]))
    #if len(split) == 5:
    #    if split[4].startswith("[") and split[4].endswith("]"):
    #        new_list.append(split[4][1:-1].split(","))
    #    else:
    #        raise ValueError(f"Invalid input format: Metadata brackets are not properly formatted in line '{line}'. Expected format: [meta1,meta2,...]") 
    return new_list

def get_hubs(data: list) -> dict:
    valid_hubs = {"hub", "start_hub", "end_hub"}
    hubs: dict = {}
    for line in data:
        split = line.split(":")
        if split[0] in valid_hubs:
            hubs[split[0]] = clean_hub_data(split[1], line)
    return hubs

def get_connections(data: list):
    pass

def Parser():
    Config_data = Config({})
    list_data = []
    with open("input.txt", "r") as file:
        data = file.readlines()
    for line in data:
        if line.startswith("#") or line.strip() == "":
            continue  # Skip comment lines and empty lines
        else:
            list_data.append(line.strip())
    if list_data[0].startswith("nb_drones:"):
        nb_drone = int(list_data[0].split(":")[1].strip())
        Config_data.set_nb_drones(nb_drone)
    else:
        raise ValueError("Invalid input format: expected 'nb_drones:' at the beginning of the file.")
    validate_input(list_data[1:])
    Config_data.set_hubs(get_hubs(list_data[1:]))
    print(Config_data._hubs)
    Config_data.set_connections(get_connections(list_data[1:]))
    return Config_data
