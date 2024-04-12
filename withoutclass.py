# Initialize empty list to store artwork data
artwork_data = []

# Function to add artwork
def add_artwork():
    title = input("Enter artwork title: ")
    artist = input("Enter artist name: ")
    price = float(input("Enter artwork price: "))
    artwork_data.append({'title': title, 'artist': artist, 'price': price})
    print("Artwork added successfully!")

# Function to view artwork
def view_artwork():
    if artwork_data:
        for artwork in artwork_data:
            print(f"Title: {artwork['title']}, Artist: {artwork['artist']}, Price: ${artwork['price']}")
    else:
        print("No artwork available.")

# Function to search artwork
def search_artwork():
    keyword = input("Enter title or artist to search: ")
    found = False
    for artwork in artwork_data:
        if keyword.lower() in artwork['title'].lower() or keyword.lower() in artwork['artist'].lower():
            print(f"Title: {artwork['title']}, Artist: {artwork['artist']}, Price: ${artwork['price']}")
            found = True
    if not found:
        print("Artwork not found.")

# Function to update artwork information
def update_artwork():
    title = input("Enter artwork title to update: ")
    for artwork in artwork_data:
        if title.lower() == artwork['title'].lower():
            artwork['artist'] = input("Enter new artist name: ")
            artwork['price'] = float(input("Enter new artwork price: "))
            print("Artwork information updated successfully!")
            return
    print("Artwork not found.")

# Function to delete artwork
def delete_artwork():
    title = input("Enter artwork title to delete: ")
    for artwork in artwork_data[:]:
        if title.lower() == artwork['title'].lower():
            artwork_data.remove(artwork)
            print("Artwork deleted successfully!")
            return
    print("Artwork not found.")

# Main function
def main():
    while True:
        print("\nArt Gallery Management System")
        print("1. Add Artwork")
        print("2. View Artwork")
        print("3. Search Artwork")
        print("4. Update Artwork")
        print("5. Delete Artwork")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_artwork()
        elif choice == '2':
            view_artwork()
        elif choice == '3':
            search_artwork()
        elif choice == '4':
            update_artwork()
        elif choice == '5':
            delete_artwork()
        elif choice == '6':
            print("Thank you for using the Art Gallery Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()