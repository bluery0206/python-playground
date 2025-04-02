"""
Object Oriented Programming
Midterm Activity Part 1 

Act 1:
    Write a Python program to create a
        Book class with 
            serial_number,
            tittle, 
            author, 
            year_published and 
            quantity     
    as instance attributes.

    Sample output:
        111, Programming with Python, Juan Dela Cruz, 2022, 10

Act 2:
    Continue activity_1, make the instance attributes private and provide
    the setters and getters methods.

    Sample output using the getter method:
        111, Programming with Python, Juan Dela Cruz, 2022, 10

Act 3:
    Continue activity Act02 change the quantity and year published value
    by accessing the setter method

Act 4:
    Continue activity Act03, provide
        a method borrow_book
            will accept an integer value that will represent how many books will be borrowed, 
            then If there are enough book on-hand deduct the current stock with the borrowed book quantity and 
            set the new stock and return Successfully borrowed, else return Not Enough stock.

Author: Mark Ryan Hilario | bluery0206    
Date: April 1, 2025

Just tryna practice by doing some old activities

Applying @property decorator is kinda fun

I have added validation
"""

from datetime import datetime

MAX_SERIAL_NUMBER: int = 9999
MAX_TITLE_LENGTH: int = 100
MAX_AUTHOR_LENGTH: int = 100
MAX_QUANTITY: int = 100

class Book:
    def __init__(self, serial_number: int, title: str, author: str, year_published: int, quantity: int) -> None:
        self.__serial_number: int = serial_number
        self.__title: str = title
        self.__author: str = author
        self.__year_published: int = year_published
        self.__quantity: int = quantity

    # A @property is a getter. usually used ug naa kay validation when getting or setting (required if mag setter)
    @property
    def serial_number(self) -> int:
        """ The unique identifier of the book """
        return self.__serial_number
    
    # @var_name.setter is the setter which requires the @property (getter) above to function. again, usually used when we have validation
    @serial_number.setter
    def serial_number(self, new_serial_number: int) -> None:
        if type(new_serial_number) is not int:
            print("Serial number has to have a type int (0, 9999).")
        
        if new_serial_number > MAX_SERIAL_NUMBER:
            print(f"Serial number can't be set to {new_serial_number} (Max: {MAX_SERIAL_NUMBER})")

        self.__serial_number: int = new_serial_number

    @property
    def title(self) -> int:
        """ The title """
        return self.__title
    
    @title.setter
    def title(self, new_title: str) -> None:
        if type(new_title) is not str:
            print("Title has to have aa type str.")
        
        if len(new_title) > MAX_TITLE_LENGTH:
            print(f"Title is too long (Max: {MAX_TITLE_LENGTH})")
        
        self.__title: str = new_title

    @property
    def author(self) -> int:
        """ The author """
        return self.__author
    
    @author.setter
    def author(self, new_author: str) -> None:
        if type(new_author) is not str:
            print("Author name has to have a type str.")
        
        if len(new_author) > MAX_AUTHOR_LENGTH:
            print(f"Author name is too long (Max: {MAX_AUTHOR_LENGTH})")
        
        self.__author: str = new_author

    @property
    def year_published(self) -> int:
        """ The year published """
        return self.__year_published
    
    @year_published.setter
    def year_published(self, new_year_published: int) -> None:

        if type(new_year_published) is not int:
            print("Year published name has to have a type int.")
        
        if new_year_published > datetime.now().year:
            print("Year published cannot be ahead of current year")
        
        self.__year_published: str = new_year_published

    @property
    def quantity(self) -> int:
        """ The quantity or the number of books """
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity: int) -> None:
        if type(new_quantity) is not int:
            print("Quantity has to have a type str.")
        
        if new_quantity > MAX_QUANTITY:
            print(f"Quantity is too large (Max: {MAX_QUANTITY})")
        
        print(f"New quantity is set (old value={self.__quantity}, new value={new_quantity})")
        
        self.__quantity: int = new_quantity

    @property
    def book_details(self) -> str:
        """ The book details """
        return f"{self.__serial_number}, {self.__title}, {self.__author}, {self.__year_published}, {self.__quantity}"
    
    def borrow_book(self, quantity: int) -> str:
        print("Borrowing book...")

        if self.__quantity < quantity:
            print("Cannot borrow. Value cannot be above the book quantity.")
            return
        
        if self.__quantity == 0:
            print("Cannot borrow. Out of stock.")
            return
        
        self.quantity -= quantity

        print("Succesfully borrowed.")
        

book1 = Book(
    serial_number = 1111,
    title = "Arknights Operators",
    author = "bluery0206",
    year_published = 2025,
    quantity = 10
)

book1.borrow_book(5)
book1.borrow_book(2)
