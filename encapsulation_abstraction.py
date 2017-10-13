#!/usr/bin/python 

class Library:
    
    def __init__(self,listofbooks):

    	self.availableBooks=listofbooks

    def showAvailableBooks(self):
	print("List of Books in Library")
		
	for book in self.availableBooks:
	    print(book)

    def lendABook(self,book):
        if book in self.availableBooks:
           self.availableBooks.remove(book)
           print("you have successfully borrowed the book")
        else:
           print("book is not available")       
   
    def backToLibrary(self,book):
        self.availableBooks.append(book)
        print("book has been sucessfully added to library")

class Customer:

      def borrowBook(self):
          self.bbook = input()
          return self.bbook

      def returnBook(self):
          self.rbook = input()
          return self.rbook

library = Library(["aws","jenkins","docker"])
customer = Customer()
while True:
 print("press 1 for display list of books in library")
 print("press 2 to lend a book")
 print("press 3 to return a book")
 print("press 4 for quit")
 userInput = int(input())
 
 if userInput is 1:
    library.showAvailableBooks()
 elif userInput is  2:
      print("Enter the book u want to lend")
      requestedBook= customer.borrowBook()
      library.lendABook(requestedBook)
 elif userInput is 3:
      print("Enter the book u want to return")
      returnBook = customer.returnBook()
      library.backToLibrary(returnBook)
 elif userInput is 4:
    quit()
