class CarbonFootprint:
    def __init__(self, item_name, carbon_footprint, category):
        """
        Initialize a CarbonFootprint object.
        :param item_name: Name of the item (string).
        :param carbon_footprint: Carbon footprint value (float).
        :param category: Category of the item (string).
        """
        self.item_name = item_name
        self.carbon_footprint = carbon_footprint
        self.category = category

    def __str__(self):
        """Return a string representation of the object."""
        return f"{self.item_name} ({self.category}): {self.carbon_footprint} kg CO2"

    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            "item_name": self.item_name,
            "carbon_footprint": self.carbon_footprint,
            "category": self.category
        }

if __name__ == "__main__":
    from carbonkeyrepo import Repository
    # Create a repository
    repo = Repository()

    # Add items to the repository
    beef = CarbonFootprint("Beef", 27.0, "Food")
    milk = CarbonFootprint("Milk", 1.9, "Food")
    train = CarbonFootprint("Train Travel", 0.02, "Transportation")

    repo.add(beef)
    repo.add(milk)
    repo.add(train)

    # Display all items
    print("All items in the repository:")
    for item in repo.get_all():
        print(item)

    # Remove an item
    print("\nRemoving 'Milk' from the repository...")
    repo.remove("Milk")

    # Display updated items
    print("\nUpdated items in the repository:")
    for item in repo.get_all():
        print(item)

    # Clear all items
    print("\nClearing the repository...")
    repo.clear()
    print("All items after clearing:", repo.get_all())
