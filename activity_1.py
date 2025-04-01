"""
Object Oriented Programming
Midterm Activity Part 1 

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

Author: Mark Ryan Hilario | bluery0206    
Date: April 1, 2025

Just tryna practice by doing some old activities
"""

class Book:
    def __init__(self, serial_number: int, title: str, author: str, year_published: str, quantity: int) -> None:
        self.serial_number: int = serial_number
        self.title: str = title
        self.author: str = author
        self.year_published: str = year_published
        self.quantity: int = quantity

    def __repr__(self) -> str:
        return f"{self.serial_number}, {self.title}, {self.author}, {self.year_published}, {self.quantity}"

book1 = Book(
    serial_number = 1111,
    title = "Arknights Operators",
    author = "bluery0206",
    year_published = "2025",
    quantity = 10
)

print(book1)