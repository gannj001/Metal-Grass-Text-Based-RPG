class Item:
    def __init__(self, name, value, description):
        self.value = value
        self.name = name
        self.description = description

    def __str__(self):
        print(self.name)
