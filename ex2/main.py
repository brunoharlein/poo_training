from cities import cities
from city import City

if __name__ == '__main__':
    # Loop through the cities list and instanciate a new city object with each dictionnary
    # Parcourez la liste des villes et instanciez un nouvel objet de ville avec chaque dictionnaire
    for city in cities:
        city = City(city)
        city.show_information()
