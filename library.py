#Creating a empty list
books = []

#This function add books
def add_books():
    name = input("Enter Book Name: ")
    date = input("Enter release date: ")
    writter = input("Enter Writter Name: ")
    book = {"Name":name,"Date":date,"Writter":writter}
    books.append(book)
    print("Book added to library successfully")

#This function helps to view books
def view_books():
    if not books:
     print("There is no book found")
    print("Book list")
    for id,book in enumerate(books,start=1):
     print(f"{id}. Book name: {book["Name"]}, Release Date: {book["Date"]},Writter of book {book["Writter"]} \n")

#This function search books
def search_book():
   search_name = input("Enter book name to search: ")
   found = False
   for book in books:
      if book["Name"].lower() == search_name.lower():
         print(f"Book Found! Name:{book["Name"]}, Release Date: {book["Date"]}, Writter: {book["Writter"]}")
         found = True
         break
   if not found:
      print("Book no found")

#This function delete books
def delete_book():
   delete_name = input("Enter book name to delete: ")
   for book in books:
      if book["Name"].lower() == delete_name.lower():
         books.remove(book)
         print(f"Book Deleted! Name:{book["Name"]}")
         return
   print("Book no found")


while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
       add_books()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("👋 Exiting system. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice! Please try again.\n")