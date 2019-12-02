from book import Book
from reader import Reader
from library import Library
from book_list import books_list

if __name__ == '__main__':
    #We open the library, for now it does not have any book
    # Nous ouvrons la bibliothèque, pour l'instant elle n'a pas de livre
    library = Library()

    # For each book data in the list, we instanciate a book object and add it to the library
    # Pour chaque donnée livre de la liste, nous instancions un objet livre et nous l'ajoutons à la bibliothèque.
    for book in books_list:
        book = Book(title=book[0], pages=book[1])
        library.add_book(book)

    # A new reader come in the library
    reader = Reader()
    # He wants to borrow a book but this one does not exists so an exception shows up
    # Il veut emprunter un livre mais celui-ci n’existant pas, une exception se présente
    reader.borrow_book(library, 'test')
    # Instead he borrows Harry Potter (OK it is not a title but let's keep things simple)
    # Au lieu de cela, il emprunte Harry Potter (OK, ce n'est pas un titre, mais gardons les choses simples)
    reader.borrow_book(library, 'Harry Poter')
    # Then he read the whole book
    # Puis il a lu le livre en entier
    reader.read_book()
