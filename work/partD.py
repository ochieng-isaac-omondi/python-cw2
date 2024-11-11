
         #PART D
def search_books(books):   #function for seacrhing a book basing on it's title
    #it starts an infinite loop
  while True:
        title_input = input("Enter a book title to search : ") #prompts user to put a book title

        '''If we want to search and know if a value was found. we use a variable that starts at False and
        sets it to True as soon as we find what we are looking for. '''
        
        found = False

        for book in books:
            if book["title"] == title_input: #checks if the current book title entered matches the title_input
                print(f"Found{book['title']} by {book['author']} was published in {book['year_published']}")
                found = True #indicates that a matching book was found
                break   #breaks out a loop
        
        if not found:     #indicates that no matching book was found
               print("Book not found. Please try again.")   #displays a message to user prompting them to try again
            
        if title_input == 'exit':   #checks user entered exit instead of book title
                print("Exiting the search.")    #informs the user that the search is ending
                break

#defining the book list
books = [
     {"title":"Kings Landing", "author": "Nary", "year_published": 1988},
     {"title":"Winterfell", "author": "John Snow", "year_published": 1941},
     {"title":"Lost Kingdom", "author": "chai Feng", "year_published": 1843},
     {"title":"Galaxy Wave", "author": "Christopher", "year_published": 1776}
] 
# Calls the function to start searching
search_books(books)
       
       