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

Author: Mark Ryan Hilario | bluery0206    
Date: April 1, 2025

Just tryna practice by doing some old activities

Applying @property decorator is kinda fun
"""

class Book:
    def __init__(self, serial_number: int, title: str, author: str, year_published: str, quantity: int) -> None:
        self.__serial_number: int = serial_number
        self.__title: str = title
        self.__author: str = author
        self.__year_published: str = year_published
        self.__quantity: int = quantity

    @property
    def serial_number(self) -> int:
        return self.__serial_number
    
    @serial_number.setter
    def serial_number(self, new_serial_number) -> None:
        self.__serial_number = new_serial_number

    @property
    def title(self) -> int:
        return self.__title
    
    @title.setter
    def title(self, new_title) -> None:
        self.__title = new_title

    @property
    def author(self) -> int:
        return self.__author
    
    @author.setter
    def author(self, new_author) -> None:
        self.__author = new_author

    @property
    def year_published(self) -> int:
        return self.__year_published
    
    @year_published.setter
    def year_published(self, new_year_published) -> None:
        self.__year_published = new_year_published

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, new_quantity) -> None:
        self.__quantity = new_quantity

    @property
    def book_details(self) -> str:
        return f"{self.serial_number}, {self.title}, {self.author}, {self.year_published}, {self.quantity}"

book1 = Book(
    serial_number = 1111,
    title = "Arknights Operators",
    author = "bluery0206",
    year_published = "2025",
    quantity = 10
)

print(book1.book_details)