from Data import Config

def validate_input(data: list):
    pass

def get_hubs(data: list):
    pass

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
    Config_data.set_hubs(get_hubs(list_data[1:]))
    Config_data.set_connections(get_connections(list_data[1:]))
    return Config_data
