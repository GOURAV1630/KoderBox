# Design a class Library with methods for adding books, lending books to users, and keeping track of available 
# and borrowed books. Users can return borrowed books to the library.

class library:
    books = {}  # Dictionary to store available books (book_name: count)
    borrowed_books = {}  # Dictionary to track borrowed books (user: [book_name])
    
    #this method is to add book name to the dictionary and storing it with the count of books
    def add_book(self):  
        book_name=input('Name of the book: ').upper()
        self.book_name = book_name
        
        if book_name in self.books: 
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1
            
        print(self.books)
       
    # method to borrow book if available in the library i.e. count>0 .Borrowed_books ditionary will store the name of 
    # Student and name of book.
    def borrow(self):
        Std_name = input('Student name= ').upper()
        book_name = input('Book name= ').upper()

        if book_name in self.books and self.books[book_name] > 0:
            if Std_name not in self.borrowed_books:
                self.borrowed_books[Std_name] = [book_name]
            else:
                self.borrowed_books[Std_name] += [book_name]
            self.books[book_name] -= 1
            print(f'{Std_name} has borrowed book {book_name}.')
        else:
            print('This book is not available')
            
    ## this method add the book to the books dictionary and increase the count after return. Book which was return back 
    #  will be removed from theb borrowed_books dictionary. Only the student name will be stored to show that this stud. has
    # borrowed book in the past.
    def return_book(self):
        Std_name= input('Student name= ').upper()
        book_name = input('Book name= ').upper()
        if Std_name in self.borrowed_books and book_name in self.borrowed_books[Std_name]:
            self.books[book_name] += 1
            self.borrowed_books[Std_name].remove(book_name)
            print(f'{Std_name} has return the book:- {book_name}')
        else:
            print(f'{Std_name} has not borrowed the book - {book_name}.')
    
    
    # finally, this method is to check the borrowed books record and books which are available. 
    def check_books(self):
        print(f'\nBorrowed books with Student names who have borrowed book in the past are:-\n{self.borrowed_books}')
        print(f'Books available are:-\n{self.books}')

        
## Assigning Library class to variable a , then the object a can be used to interact with methods of the class
a=library()  
print('Hello Admin, welcome to our library system.')

## Adding try and except just in case if there's an input error.
try:
    while True:
        print('\n1. Add book to library')
        print('2. Borrow book')
        print('3. Return book')
        print('4. Check available books and borrowed books')
        print('5. Exit\n')

        choice= int(input('Enter valid option(1,2,3,4,5):- '))
        if choice==1:
            a.add_book()
        elif choice==2:
            a.borrow()
        elif choice==3:
            a.return_book()
        elif choice==4:
            a.check_books()
        elif choice==5:
            print('Thank you.')
            break
        else:
            print('Enter valid option.')
            break
except Exception as e:print('Enter valid options from 1 to 5.Try again.')