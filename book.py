import json, os

path = "bookdata.json" # ფაილი სადაც შეინახება ინფორმაცია

class Book:
    def __init__(self, book_name, book_author, book_year):
        # ვალიდაცია
        if not self.is_valid_name(book_name):
            raise ValueError('book name is not valid')
        if not self.is_valid_name(book_author):
            raise ValueError('book author is not valid')
        if not self.is_valid_year(book_year):
            raise ValueError('book year is not valid')
            
        self.book_name = book_name
        self.book_author = book_author
        self.book_year = book_year
    @staticmethod
    def is_valid_name(book_name):
        return  book_name != ""
    @staticmethod
    def is_valid_year(year):
        return (0 < year <= 2025) and type(year) is int
class BookManager:
    def __init__(self):
        # ვამოწმებთ ფაილი თუ არსებობს 
        
        if os.path.exists(path):
         try:
             with open(path, 'r', encoding='utf-8') as f:
                self.data = json.loads(f.read())
         except json.JSONDecodeError:
            self.data = [] 
            
        else: # თუ არ არსებობს ქმნის
            self.data = []
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        
    def append_book(self, book):
        if isinstance(book, Book): # ვამოწმებთ არის თუ არა Book კლასის
            new_book = {
             "book_name" : book.book_name,
             "book_author" : book.book_author,
             "book_release_date" : book.book_year
                }

            for data in self.data: # ვამოწმებთ ხომ არ გვაქვს შენახული უკვე წიგნი
                if data['book_name'].lower() == book.book_name.lower() and data['book_author'].lower() == book.book_author.lower() and data['book_release_date'] == book.book_year:
                    print("this book already exists")
                    return
            
        # თუ არ არის ფაილში წიგნი ამატებს
        self.data.append(new_book)
        with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)


        
    def find_book(self, title): # ეძებს წიგნს
        for book in self.data:
            if book['book_name'] == title:
                return book


    def all_book(self): # აბრუნებს ყველა წიგნს
        return self.data
        
# მენიუს დაბეჭდვა
def print_options():
    print("1. find book")
    print("2. add a book")
    print("3. show all books")
    print("4. Exit")
 
manager = BookManager()

while True:
    print("Hello, choose option")
    print_options()
    try:
        op = int(input("your choice: "))
    except Exception as e:
        print("invalid input. enter a number 1-4")
    if op == 1:
        title = input("enter book name you want to find: ")
        book = manager.find_book(title)
        if book is not None:
            print(f"Book name : {book['book_name']}, Book author : {book['book_author']}, release year : {book['book_release_date']}")
        else:
            print("can't find a book")
    elif op == 2:
        name = input("enter books name: ")
        author = input("enter books author: ")
        year = int(input("eneter books year: "))
        book =Book(name, author, year)
        manager.append_book(book)
    elif op == 3:
        for book in manager.all_book():
            print(f"Book name : {book['book_name']}, Book author : {book['book_author']}, release year : {book['book_release_date']}")
    elif op == 4:
        print("Goodbye👋🏻!")
        break
    else:
        print("please enter valid choice")
        continue



    