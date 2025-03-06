def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if not books:
            print("\n📖 No books found in the store.\n")
            return

        print("\n📚 Book List:")
        print("=" * 70)
        print(f"{'ID':<6} {'Title':<20} {'Author':<20} {'Genre':<10} {'Price':<6} {'Qty':<4}")
        print("=" * 70)

        for book in books:
            # Strip leading/trailing spaces and split by ' | '
            book_details = book.strip().split(" | ")

            # Check if the line has exactly 6 parts (ID, Title, Author, Genre, Price, Qty)
            if len(book_details) == 6:
                print(f"{book_details[0]:<6} {book_details[1]:<20} {book_details[2]:<20} {book_details[3]:<10} {book_details[4]:<6} {book_details[5]:<4}")
            else:
                print("Warning: Skipping invalid line:", book.strip())

        print("=" * 70)

    except FileNotFoundError:
        print("\n❌ Error: The file 'books.txt' does not exist. Add some books first.\n")

# Call function to test
# view_books()  # Uncomment this if you want to test separately
