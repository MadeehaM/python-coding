class Library:
    def __init__(self,list_of_books,name):
        self.booklist = list_of_books
        self.name = name
        self.lend={}

    def bookDisplay(self):
        print("We have the following books in our library:",self.name)
        for book in self.booklist:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.booklist:
            print("Sorry we do not have that book")
        elif book in self.lend:
            print("The book is already being used by:", {self.lend[book]})
        else:
            self.lend[book]= user
            print("Lender-Book database has been updated. You can take the book now")

    def addBook(self, book):
        self.booklist.append(book)
        print((book), "has been added to the book list.")

    def returnBook(self,book):
        if book in self.lend:
            print("")