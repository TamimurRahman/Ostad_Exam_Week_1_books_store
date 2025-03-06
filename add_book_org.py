
def duplicate(isbn):
    """Check if the given ISBN already exists in books.txt."""
    try:
        with open("books.txt", "r") as file:
            for line in file:
                details = line.strip().split(" | ")
                if len(details) < 3:  # Ensure the line has enough parts
                    continue
                
                existing_isbn = details[2]  # Extract ISBN
                if existing_isbn == isbn:
                    return True
        return False
    except FileNotFoundError:
        return False  # If file doesn't exist, no duplicates


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    
    if duplicate(isbn):
        print("\nError: A book with this ISBN already exists!\n")
        return  # Stop adding duplicate books
    
    genre = input("Enter book genre: ")
    price = input("Enter book price: ")
    quantity = input("Enter quantity in stock: ")

    with open("books.txt", "a") as file:
        file.write(f"{title} | {author} | {isbn} | {genre} | {price} | {quantity}\n")
    
    print(f"\nBook added successfully! Book ID: {isbn}\n")

# Call the function to test

