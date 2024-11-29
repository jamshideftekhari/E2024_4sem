class Repository:
    def __init__(self):
        # Internal storage for the items
        self.data = []

    def add(self, item):
        """Add an item to the repository."""
        self.data.append(item)

    def get_all(self):
        """Get all items in the repository."""
        return self.data

    def remove(self, item):
        """Remove an item from the repository."""
        if item in self.data:
            self.data.remove(item)
        else:
            print("Item not found in the repository.")

    def clear(self):
        """Clear all items from the repository."""
        self.data = []

if __name__ == "__main__":
    # Create a repository instance
    repo = Repository()

    # Add items to the repository
    repo.add({"item": "Beef", "carbon_footprint": 27.0})
    repo.add({"item": "Milk", "carbon_footprint": 1.9})
    repo.add({"item": "Train Travel", "carbon_footprint": 0.02})

    # Get all items
    print("All items in the repository:")
    for item in repo.get_all():
        print(item)

    # Remove an item
    print("\nRemoving 'Milk' from the repository...")
    repo.remove({"item": "Milk", "carbon_footprint": 1.9})

    # Get updated items
    print("\nUpdated items in the repository:")
    for item in repo.get_all():
        print(item)

    # Clear all items
    print("\nClearing the repository...")
    repo.clear()
    print("All items after clearing:", repo.get_all())
