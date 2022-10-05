def addClient(clientsList):
    id = len(clientsList) + 1

    full_name = input('Please enter your full name: ')
    age = input('Please enter your age: ')
    id_no = input('Please enter your ID number: ')
    phone_number = input('Please enter your phone number: ')

    client = {'id': id, 'full_name': full_name, 'age': age, 'id_no': id_no, 'phone_number': phone_number}
    clientsList.append(client)

    print('Client has been successfully added.')


def addLibrarian(librariansList):
    id = len(librariansList) + 1

    full_name = input('Please enter your full name: ')
    age = input('Please enter your age: ')
    id_no = input('Please enter your ID number: ')
    employment_type = input('Please enter your employment type (full/part): ')

    librarian = {'id': id, 'full_name': full_name, 'age': age, 'id_no': id_no, 'employment_type': employment_type}
    librariansList.append(librarian)

    print('Librarian has been successfully added.')


def addBook(booksList):
    id = len(booksList) + 1

    title = input("Please enter the book's title: ")
    description = input("Please enter the book's description: ")
    author = input("Please enter the book's author: ")
    status = input("Please enter the book's status (active/inactive): ")

    book = {'id': id, 'title': title, 'description': description, 'author': author, 'status': status}
    booksList.append(book)

    print('Book has been successfully added.')


def bookAvailability(booksList, book_id):
    exists = False
    available = False

    for book in booksList:
        for key, value in book.items():
            if key == 'id' and value == book_id:
                exists = True
                if book['status'] == 'active' or book['status'] == 'Active':
                    available = True
                    break
                break

    return (exists and available)


def addOrder(ordersList, clientsList, booksList, order_id, client_id, i):
    import datetime
    id = len(ordersList) + 1
    x = datetime.datetime.now()
    d = x.strftime("%x")

    exists = False
    ordered = False

    for client in clientsList:
        for key, value in client.items():
            if key == 'id_no' and value == client_id:
                exists = True
                break

    for order in ordersList:
        for key, value in order.items():
            if (key == 'id' and value == order_id):
                if (order['client_id'] == client_id) and (order['status'] == 'active' or order['status'] == 'Active'):
                    ordered = True
                break

    if i == 1:
        if not exists:
            print('Sorry! you are not a registered client, your request has been declined.')
            status = 'canceled'
        else:
            print('All done! you can take the book now.')
            status = 'active'

            for book in booksList:
                for key, value in book.items():
                    if key == 'id' and value == book_id:
                        book['status'] = 'inactive'
                        break

        order = {'id': id, 'date': d, 'client_id': client_id, 'book_id': book_id, 'status': status}
        ordersList.append(order)

    elif i == 2:
        if not exists:
            print('Sorry! you are not a registered client, your request has been declined.')
        elif not ordered:
            print('Sorry! this book is not currently borrowed under your name.')
        else:
            print('All done! your book has been returned.')

            for book in booksList:
                for key, value in book.items():
                    if key == 'id' and value == book_id:
                        book['status'] = 'active'
                        break

            for order in ordersList:
                for key, value in order.items():
                    if (key == 'id' and value == order_id):
                        order['status'] = 'expired'
                        break


def aviBooks(booksList, availableBooks):
    for i in range(len(availableBooks)):
        if availableBooks[i]['status'] == 'inactive':
            del availableBooks[i]
            break

    for book in booksList:
        for key, value in book.items():
            if key == 'status' and (value == 'active' or value == 'Active'):
                availableBooks.append(book)
                break


def viewRecords(librariansList, clientsList, booksList, ordersList, availableBooks):
    print()
    print("Librarians' list:")
    print(*librariansList, sep="\n")
    print()
    print("Clients' list:")
    print(*clientsList, sep="\n")
    print()
    print("Books' list:")
    print(*booksList, sep="\n")
    print()
    print("Orders' list:")
    print(*ordersList, sep="\n")
    print()
    print("Total number of borrowd books:")
    print((len(booksList) - len(availableBooks)))
    print()
    print("Total number of available books:")
    print(len(availableBooks))
    print()
    print("Total number of borrowed orders:")
    print(len(ordersList))
    print()


def user():
    print()
    print('To enter the library system, please identify yourself')
    print('1. logging in as a librarien')
    print('2. logging in as a client')
    print()
    print('Please enter your choice (1,2):')


def clientsMenu():
    print()
    print('Please choose one of the following options:')
    print()
    print('1. Register as a new client')
    print('2. Borrow a book')
    print('3. Return a book')
    print()
    print('Please enter your choice (1,2,3):')


def librariansMenu():
    print()
    print('Please choose one of the following options:')
    print()
    print('1. Register as a new librarian')
    print('2. Add a new book')
    print('3. View records')
    print()
    print('Please enter your choice (1,2,3):')


clientsList = []
librariansList = []
booksList = []
ordersList = []
availableBooks = []
book = {'id': 1, 'title': "the life of a stupid man", 'author': "Ryūnosuke Akutagawa", 'description': "fiction",
        'status': "active"}
booksList.append(book)
book = {'id': 2, 'title': "Goodnight punpun ", 'author': "Inio Asano", 'description': "drama", 'status': "inactive"}
booksList.append(book)
book = {'id': 3, 'title': "The Tokyo Zodiac Murders ", 'author': "Soji Shimada", 'description': "Murder mystery",
        'status': "active"}
booksList.append(book)

while True:
    user()
    userChoice = int(input())
    if userChoice == 1:
        librariansMenu()
        librariansChoice = int(input())
        if librariansChoice == 1:
            addLibrarian(librariansList)
            print()
            input('Press Enter button to go back to Main Menu ')
        elif librariansChoice == 2:
            addBook(booksList)
            print()
            input('Press Enter button to go back to Main Menu ')
        elif librariansChoice == 3:
            aviBooks(booksList, availableBooks)
            viewRecords(librariansList, clientsList, booksList, ordersList, availableBooks)
            print()
            input('Press Enter button to go back to Main Menu ')
        else:
            print('Please choose a valid number.')
            print()
            input('Press Enter button to go back to Main Menu ')

    elif userChoice == 2:
        clientsMenu()
        clientsChoice = int(input())
        if clientsChoice == 1:
            addClient(clientsList)
            print()
            input('Press Enter button to go back to Main Menu ')
        elif clientsChoice == 2:
            print("Books' list:")
            print(*booksList, sep="\n")
            print()
            book_id = int(input('Enter ID of the book you want to borrow: '))
            while not bookAvailability(booksList, book_id):
                print('Please choose an Active book: ')
                print("Books' list:")
                print(*booksList, sep="\n")
                print()
                book_id = int(input('Please enter ID of the book you want to borrow: '))
            client_id = input('Please enter your ID number: ')
            addOrder(ordersList, clientsList, booksList, book_id, client_id, 1)
            print()
            input('Press Enter button to go back to Main Menu ')
        elif clientsChoice == 3:
            client_id = input('Please enter your ID number: ')
            order_id = int(input('Please enter ID of the book you want to return: '))
            addOrder(ordersList, clientsList, booksList, order_id, client_id, 2)
            print()
            input('Press any button to go back to Main Menu ')
        else:
            print('Please choose a valid number.')
            print()
            input('Press Enter button to go back to Main Menu ')
    else:
        print('Please choose a valid number.')
        print()
        input('Press Enter to go back to Main Menu ')
