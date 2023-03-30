from database import Database
from writeAJson import writeAJson
from bookModel import BookModel
from cli import BookCLI

db = Database(database="BibliotecaInatel", collection="Livros")
bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel)
bookCLI.run()