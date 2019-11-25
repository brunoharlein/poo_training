from city import City

# if __name__ == '__main__':
city = City("Wasquehal", 59)
city1 = City("Croix", 59)
city2 = City("Paris", 75)
city3 = City("Tokyo", 00)

city.show_location()
city1.show_location()

city.change_location("Lille", 59)  # he method changes the name and the department for city object
city.show_location()
