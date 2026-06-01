from curses.ascii import isdigit

from .Data import Config


def validate_input(data: list):
    valid_inits = ["hub:", "connection:", "start_hub:", "end_hub:", "#"]
    for line in data:
        if not any(line.startswith(init) for init in valid_inits):
            raise ValueError(f"Invalid input format: line '{line}' does not start with a valid keyword.")

# Refatorar a parte de leitura e validação dos hubs, para validar se a linha tem o formato correto e não existe nenhum dado "lixo" na linha e retirar os comentários da linha, para evitar erros de formatação. O mesmo para as conexões, validar se a linha tem o formato correto e retirar os comentários da linha.

def clean_hub_data(hub_data: str, line: str) -> str:
    new_str: str = ""
    hub_data = hub_data.split("#")[0].strip()
    split = hub_data.split(" ")
    meta_start = hub_data.find("[")
    meta_end = hub_data.find("]")

    if not split[0].isalnum():
        raise ValueError(f"Invalid input format: First parameter '{split[0]}' of hub must be a string in line '{line}'.")
    new_str += split[0]
    for param in range(1, 3):
        if not split[param].isdigit():
            raise ValueError(f"Invalid input format: expected a number at position {param} in hub data. From line: '{line}'")
        new_str += f" {split[param]}"
    if len(split) > 3:
        if meta_start == -1 or meta_end == -1 or meta_end < meta_start:
            raise ValueError(f"Invalid input format: Metadata brackets are not properly formatted in line '{line}'. Expected format: [meta1, meta2, ...]")
        if meta_end != len(hub_data) - 1:
            raise ValueError(f"Invalid input format: More than one parameter found after metadata in line '{line}'. Expected format: [meta1, meta2, ...]")
        metadata = hub_data[meta_start + 1:meta_end].split(",")
        new_str += f" [{', '.join(meta.strip() for meta in metadata)}]"
    return new_str

def get_hubs(data: list) -> list:
    valid_hubs = {"hub", "start_hub", "end_hub"}
    hubs: list = []
    for line in data:
        split = line.split(":")
        if split[0] in valid_hubs:
            hubs.append("".join(split[0]+ " : " + clean_hub_data(split[1], line)))
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
    print("Hubs:")
    for hub in Config_data._hubs:
        print(hub)
    Config_data.set_connections(get_connections(list_data[1:]))
    return Config_data
