# Task
# Given a Book class and a Solution class, write a MyBook class that does the following:

#     Inherits from Book
#     Has a parameterized constructor taking these 3 parameters:

#     string title
#     string author
#     int price
#     Implements the Book class' abstract display() method so it prints these 3 lines:

# Title:, a space, and then the current instance's title
# Author:, a space, and then the current instance's author
# Price:, a space, and then the current instance's price


from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
        
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
        
    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")
            
            
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()