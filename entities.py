from res.entity import Entity

scarecrow = Entity()
scarecrow.name = "Scarecrow"
scarecrow.description = """
An old, raggedy scarecrow still left standing by the Orcs.  It looks like 
it's smirking at you.  Why don't you wipe the smirk of it's face?"""
scarecrow.hostile = True
def scarecrow_bounce_back(self=scarecrow):
    status_line = ""
    if self.HP <= 0:
        self.HP = 1
        status_line = "The {} bounces back up...\n".format(self.name)
        self.dead = False
    return status_line
scarecrow.add_endofturn("scarecrow_bounce_back", scarecrow_bounce_back)