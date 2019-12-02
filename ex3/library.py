class Library():
    """Library class with one attribut:
    - books : a list of book objects"""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Function to append a book object to the books list
            Fonction pour ajouter un objet livre à la liste des livres"""
        self.books.append(book)

    def get_book(self, title):
        """Function to return a book object from the books list by its title
            Fonction permettant de retourner un objet livre de la liste des livres par son titre"""
        for book in self.books:
            if title == book.title:
                return book
        raise Exception("The book you are looking for is not in the library; Le livre que vous recherchez n'est pas dans la bibliothèque")