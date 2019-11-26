class City:
    """class representing city with 6 attributs """
    def __init__(self, data_dic):
        self.name = None
        self.department = None
        self.country = None
        self.population = None
        self.mayor = None
        self.capital = None
        self.hydrate(data_dic)

    def hydrate(self, data):
        """function to set a value to each attribut based on a dictionnary"""
        for key, value in data.items():
            # Prevent he creation of unwanted attributs
            if hasattr(self, key):
                setattr(self, key, value)

    def show_location(self):
        print('the city of {} is in the French department of number {}'.format(self.name, self.department))

    def change_location(self, name, department):
        self.name = name
        self.department = department

    def show_information(self):
        text = "-------------\n \
        name: {}\n \
        department: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n"

        print(text.format(self.name, self.department, self.country, self.population, self.mayor, self.capital))
