class Artwork:
    def _init_(self, title, artist, price):
        self.title = title
        self.artist = artist
        self.price = price

class ArtGallery:
    def _init_(self):
        self.artwork_data = []

    def add(self):
        title = input("Enter artwork title: ")
        artist = input("Enter artist name: ")
        price = float(input("Enter artwork price: "))
        artwork = Artwork(title, artist, price)
        self.artwork_data.append(artwork)
        print("Artwork added successfully!")

    def view(self):
        if self.artwork_data:
            for artwork in self.artwork_data:
                print(f"Title: {artwork.title}, Artist: {artwork.artist}, Price: ${artwork.price}")
        else:
            print("No artwork available.")

    def search(self):
        keyword = input("Enter title or artist to search: ")
        found = False
        for artwork in self.artwork_data:
            if keyword.lower() in artwork.title.lower() or keyword.lower() in artwork.artist.lower():
                print(f"Title: {artwork.title}, Artist: {artwork.artist}, Price: ${artwork.price}")
                found = True
        if not found:
            print("Artwork not found.")

    def update(self):
        title = input("Enter artwork title to update: ")
        for artwork in self.artwork_data:
            if title.lower() == artwork.title.lower():
                artwork.artist = input("Enter new artist name: ")
                artwork.price = float(input("Enter new artwork price: "))
                print("Artwork information updated successfully!")
                return
        print("Artwork not found.")

    def delete(self):
        title = input("Enter artwork title to delete: ")
        for artwork in self.artwork_data:
            if title.lower() == artwork.title.lower():
                self.artwork_data.remove(artwork)
                print("Artwork deleted successfully!")
                return
        print("Artwork not found.")

    def menu(self):
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
                self.add()
            elif choice == '2':
                self.view()
            elif choice == '3':
                self.search()
            elif choice == '4':
                self.update()
            elif choice == '5':
                self.delete()
            elif choice == '6':
                print("Thank you for using the Art Gallery Management System!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
if __name__ == "__main__":
    art_gallery = ArtGallery()
    art_gallery.menu()