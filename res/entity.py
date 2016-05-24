class Entity:
    def __init__(self):
        self.name = None
        self.commands = {
            "look": self.look,
        }
        self.description = "No description exists... yet..."
        self.HP = 1
        self.hostile = False
        self.endofturn_dict = {
            "check death": self.check_death,
        }
        self.dead = False

    def add_command(self, string, command):
        self.commands[string] = command

    def add_endofturn(self, string, command):
        self.endofturn_dict[string] = command

    def look(self, **kwargs):
        return self.description

    def check_death(self):
        status_line = ""
        if self.HP <= 0:
            status_line += "{} has died...\n".format(self.name)
            self.dead = True
        return status_line
