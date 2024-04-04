library = []
wishlist = []

book_name = input("Enter the name of a book you own: ")
library.append(book_name)

book_name = input("Enter the name of another book you own (or press enter to skip): ")
if book_name:
  library.append(book_name)

print("\nYour Library: ", library)

book_name = input("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(book_name)

book_name  = input("Enter the name of a book you wish to have (or press enter to skip): ")
if book_name:
  wishlist.append(book_name)

print("\nYour Wishlist: ", wishlist)

acquired_book = input("\nEnter the name of a book from your sihlist that you've acquired (or press enter to skip): ")
if acquired_book in wishlist:
  library.append(acquired_book)
  wishlist.remove(acquired_book)


print("\nUpdated Library: ", library)
print("\nUpdated Wishlist: ", wishlist)

donated_book = input("\nEnter the name of a book from your library you wish to donate (or press enter to skip): ")
if donated_book in library:
  library.remove(donated_book)


print("\nFinal Library after donation: ", library)