class Game:
    def __init__(self):
        self.playing = False
        self.character = None
        self.travel_tokens = ["go"]
        self.attack_tokens = ["attack"]
        self.investigate_tokens = ["describe", "look"]
        self.quit_tokens = ["quit", "stop", "exit"]

    def process_command(self, command):
        tokens = self.tokenise(command)
        status_line = ""
        if tokens[0] in self.travel_tokens:
            if self.character.location.connections[tokens[1]]:
                status_line += self.move_player(self.character.location.connections[tokens[1]])
            else:
                status_line += "You can't go that way!"
        elif tokens[0] in self.attack_tokens:
            status_line += self.player_attack(tokens[1])
        elif tokens[0] in self.investigate_tokens:
            status_line += self.parse_describe(tokens)
        elif tokens[0] in self.quit_tokens:
            status_line += self.handle_quit()

        if len(status_line) == 0:
            status_line = "Not able to process that command.  Yet..."
        return status_line

    def move_player(self, location):
        self.character.location = location
        return "You have arrived in {}.".format(location)

    def do_damage(self, source, target):
        target.HP -= source.weapon.damage
        return source.weapon.damage

    def player_attack(self, target):
        status_line = ""
        if target in self.character.location.entity_list.keys():
            entity = self.character.location.entity_list[target]
            if entity.hostile:
                damage = self.do_damage(self.character, entity)
                status_line += "{} took {} damage from {}.".format(entity.name, damage, self.character.name)
            else:
                status_line += "You can't attack {}.".format(entity.name)
        else:
            status_line += "{} isn't here!".format(target)
        return status_line

    def parse_describe(self, tokens):
        status_line = ""
        if tokens[1] == "location":
            status_line += self.character.location.location_details()
        elif tokens[1] in self.character.location.entity_list.keys():
            status_line += self.character.location.interact_with_entity(tokens, source=self.character)
        return status_line

    def handle_quit(self):
        self.playing = False
        return "Thank you for playing!"

    def tokenise(self, command):
        tokens = command.lower().split(" ")
        tokens.append("EOL")
        return tokens

    def printintro(self):
        intro = """
Welcome, {}, this is your story, and it starts with humble beginnings!
Your village has been attacked by rampaging Orcs!  They have taken 
everything you own!  It is your job to warn the kingdom of the impending
invasion and retrieve your stuff!  But warn the kingdom first!  You wake
up in your farmstead, there isn't much left standing...""".format(self.character.name)
        print(intro)

    def equipplayer(self):
        pass

    def endofturn_step(self):
        deadlist = []
        status_line = ""
        for key, value in self.character.location.entity_list.items():
            entity = value
            for key, value in entity.endofturn_dict.items():
                status_line += value()
            if entity.dead:
                deadlist.append(entity)
        # for entity in deadlist:
        #    del self.character.location.entity_list[entity]
        return status_line
