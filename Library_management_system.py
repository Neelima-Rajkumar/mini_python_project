import random
books = []
last_slno=random.randint(172346,534889)
def generate_slno():
    global last_slno
    last_slno+=1
    return last_slno
def add_books():
    title = input("enter the book title: ")
    author = input("enter the author: ")
    copies = int(input("enter the number of copies: "))
    slno = generate_slno()
    book = {
        "title": title,
        "author": author,
        "copies": copies,
        "slno": slno
    }
    books.append(book)
    print('the book', book['title'], 'is added to the library')

def remove_books():
    display_books()
    slno = input("enter the serial no: of the book to be removed: ")
    for book in books:
        if book['slno'] == slno:
            print(book['title'].upper())
            break
    if not books:
        print('no books available in library')
    for book in books:
        if book['slno'] == slno:
            books.remove(book)
            print('the book is removed')
            return
    print('no book is found')


def display_books():
    if not books:
        print('no books available in library')
    for book in books:
        print('Slno:', book['slno'], ', Title: ', book['title'].upper(), ', Author:', book['author'].upper(),
              ', Copies available:', book['copies'])


def rent_book():
    display_books()
    slno = input('enter the serial no: of the book: ')
    for book in books:
        if book['slno'] == slno:
            print(book['title'].upper())
            break
    status = 'available'
    if not books:
        print("book not found")
    for book in books:
        if book['slno'] == slno:
            if book['copies'] > 0:
                print(status)
                book['copies'] -= 1
                print('The book rented:', book['title'])
                return
    print('book currently not available')


def return_book():
    display_books()
    slno = input("Enter the slno of the book you want to return: ")
    for book in books:
        if book['slno'] == slno:
            print(book['title'].upper())
            break
    days = int(input("Enter the number of days you had the book: "))
    fine = 0

    if days > 5:
        for i in range(5, days):
            fine += 1
    for book in books:
        if book['slno'] == slno:
            book['copies'] += 1
            print("book returned. And rupees", fine, " is the total fine")
            return
    print('book does not belong to this library')


def library():
    while True:
        print("1. Add a book \n"
              "2. Remove a book \n"
              "3. Display all books \n"
              "4. Rent a book \n"
              "5. Return a book \n"
              "6. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            add_books()
        elif choice == "2":
            remove_books()
        elif choice == "3":
            display_books()
        elif choice == "4":
            rent_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thankyou for choosing our library. Enjoy reading. Good Bye")
            break
        else:
            print("invalid choice")
        print('-' * 100)


library()
