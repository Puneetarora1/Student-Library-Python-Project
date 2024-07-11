class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.NoOfBooks = len(self.books)
    
    def addBook(self, bookName):
        print('Thanks for adding/returning this book')
        self.books.append(bookName)
        self.NoOfBooks = len(self.books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'Dear student, book {bookName} has been issued to you')
            self.books.remove(bookName)
            return True
        else:
            print(f'Dear student, book {bookName} is not available')
            return False

    def displayBooks(self):
        print("Books present in this library are: ")
        for index, book in enumerate(self.books):
            print(index + 1, book)


class Student:
    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll
        self.issuedBooks = []
    
    def requestBook(self):
        self.book = input("Enter name of book you want to borrow :- ").capitalize()
        return self.book
    
    def addBook(self):
        self.book = input("Enter name of book you want to add/return :- ").capitalize()
        return self.book
    
    def studentBooks(self, reqBook):
        self.issuedBooks.append(reqBook)

BooksIndianLibrary = ['Python', 'Java', 'C language', 'Physics', 'Chemistry', 'Maths', 'English', 'Cs']
indianLibrary = Library(BooksIndianLibrary)
punit = Student("punit", '1')

while True:
    infoMsg = '''====Welcome to Library===
    Tell what do you want to do
    1- Display Books
    2- Request Book
    3- Add/Return Book
    4- Issued Books to Student
    5- No of Books in Library
    6- Exit()'''
    print(infoMsg)
    try:
        userInput = int(input('Enter your choice :- '))
        if userInput == 1:
            indianLibrary.displayBooks()
        elif userInput == 2:
            reqBook = punit.requestBook()
            if indianLibrary.borrowBook(reqBook):
                punit.studentBooks(reqBook)
        elif userInput == 3:
            indianLibrary.addBook(punit.addBook())
        elif userInput == 4:
            print(punit.issuedBooks)
        elif userInput == 5:
            print(indianLibrary.NoOfBooks)
        elif userInput == 6:
            exit()
        else:
            print('invalid input')
    except Exception as e:
        print(e)
