
class Config():
    def __init__(self, data: dict):
        self._nb_drones: int
        self._hubs: dict
        self._connections: list

    def set_nb_drones(self, nb_drones: int):
        self._nb_drones = nb_drones

    def set_hubs(self, hubs: dict):
        self._hubs = hubs
    
    def set_connections(self, connections: list):
        self._connections = connections
