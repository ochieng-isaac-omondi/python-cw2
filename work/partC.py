               #PART C
#Class definition
class Book:
    def __init__(self,title,author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    #method of the book description
    def description_of_the_book(self) ->str:
        return f"{self.title} by {self.author} was published in {self.year_published}."

#creating instances    
book1 = Book("Kings Landing", "Nary", 1988)
book2 = Book("Winterfell","John Snow", 1941)
book3 = Book("Lost Kingdom","chai Feng", 1843)
book4 = Book("Galaxy Wave","Christopher", 1776)

#printing out the description
print(book1.description_of_the_book())
print(book2.description_of_the_book()) 
print(book3.description_of_the_book()) 
print(book4.description_of_the_book()) 

#method of sorting book list
def sort_books_by_year(books) ->list:
        # Check if the input is a list
        if not isinstance(book_list, list):
            raise ValueError("Input must be a list of Book objects.")
        
        # Handle empty list case
        if len(books) == 0:
            return []

        # Sort the list of books by year_published attribute
        sorted_books = sorted(books, key=lambda book: book.year_published)
        return sorted_books

# List of books
book_list = [book1, book2, book3, book4 ]

# Sorting books and printing results
sorted_books = sort_books_by_year(book_list)
print("\nBooks sorted by year published:")
for book in sorted_books:
    print(book.description_of_the_book())



        #Displaying the details of each book using loops
#for loop
print("\nBook details using For loop:")
for book in sorted_books:
    print(book.description_of_the_book())

#while loop
print("\nBook details using While loop:")
num = 0
while num < len(sorted_books): #checks if the current value of num is less than the total number in sorted_books
    book = sorted_books[num]
    print(book.description_of_the_book())
    num +=1
