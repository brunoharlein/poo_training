class City:
    """class representing a city defined by name and department"""
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_location(self):
        """print object attribut"""
        print('The city of {} is in the French department of number {}'.format(self.name, self.department))

    def change_location(self, name, department):
        """function for update attributs city object"""
        self.name = name
        self.department = department