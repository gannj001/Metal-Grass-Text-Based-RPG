class Location:
    def __init__(self):
        self.name = None
        self.connections = {
            "north": None,
            "south": None,
            "east": None,
            "west": None,
        }
        self.description = "This location has no description... Yet..."
        self.hostility = 0
        self.entity_list = {}
    
#Entity functions
    def add_entity(self, entity):
        self.entity_list[entity.name.lower()] = entity

    def remove_entity(self, entity):
        del self.entity_list[entity.name]

    def interact_with_entity(self, tokens, **kwargs):
        status_line = ""
        if tokens[1] in self.entity_list.keys():
            entity = self.entity_list[tokens[1]]
            if tokens[0] in entity.commands.keys():
                status_line += entity.commands[tokens[0]](**kwargs)
            else:
                status_line += "You can't do {} with {}.".format(tokens[0], entity.name)
        else:
            status_line += "There isn't anything with the name {}.".format(tokens[1])
        return status_line

    # Connection Functions
    def connect_north(self, loc):
        self.connections["north"] = loc

    def connect_south(self, loc):
        self.connections["south"] = loc

    def connect_east(self, loc):
        self.connections["east"] = loc

    def connect_west(self, loc):
        self.connections["west"] = loc

    def describe_connections(self):
        connection_description = ""
        for k, v in self.connections.items():
            if v is not None:
                connection_description += "To the {} is the {}.".format(k, v.name)
        return connection_description

    # Presentation Functions
    def hostility_rating(self):
        ratings = {
            0: "not",
            1: "barely",
            2: "slightly",
            3: "moderately",
            4: "very",
            5: "dangerously",
        }
        return "The {} is {} hostile.".format(self.name, ratings[self.hostility])

    def __str__(self):
        return self.name

    def location_details(self):
        location_connections = self.describe_connections()
        location_description = self.description
        location_name = self.name
        location_hostility = self.hostility_rating()
        status_line = """
You are in:  {}
Description: {}
Hostility:   {}
Connections: \n{}""".format(location_name, location_description, location_hostility, location_connections)
        return status_line
