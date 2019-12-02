class Book():
    """Book class with 3 attributs:
    - title : the main title of the book as a string
    - pages : a list of strings representing each page of the books
    - current_page : the page the reader is on, -1 by default because the book is closed

        Classe de livre avec 3 attributs:
     - titre: le titre principal du livre sous forme de chaîne
     - pages: une liste de chaînes représentant chaque page des livres
     - current_page: la page sur laquelle se trouve le lecteur, -1 par défaut car le livre est fermé"""
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.current_page = -1