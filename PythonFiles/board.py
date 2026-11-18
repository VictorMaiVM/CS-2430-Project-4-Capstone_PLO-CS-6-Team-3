#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 4

# Represents a single square on the 40-space Monopoly board.
class Square:
    def __init__(self, index, name, square_type):
        self.index = index
        self.name = name
        self.square_type = square_type  # GO, Property, Railroad, Utility, Chance, CommunityChest, Jail, GoToJail, Tax, FreeParking
        self.landing_count = 0

    def reset_count(self):
        self.landing_count = 0


# Initializes and returns the 40 classic Monopoly squares in order.
def initialize_board():
    return [
        Square(0, "GO", "GO"),
        Square(1, "Mediterranean Avenue", "Property"),
        Square(2, "Community Chest 1", "CommunityChest"),
        Square(3, "Baltic Avenue", "Property"),
        Square(4, "Income Tax", "Tax"),
        Square(5, "Reading Railroad", "Railroad"),
        Square(6, "Oriental Avenue", "Property"),
        Square(7, "Chance 1", "Chance"),
        Square(8, "Vermont Avenue", "Property"),
        Square(9, "Connecticut Avenue", "Property"),
        Square(10, "Jail / Just Visiting", "Jail"),
        Square(11, "St. Charles Place", "Property"),
        Square(12, "Electric Company", "Utility"),
        Square(13, "States Avenue", "Property"),
        Square(14, "Virginia Avenue", "Property"),
        Square(15, "Pennsylvania Railroad", "Railroad"),
        Square(16, "St. James Place", "Property"),
        Square(17, "Community Chest 2", "CommunityChest"),
        Square(18, "Tennessee Avenue", "Property"),
        Square(19, "New York Avenue", "Property"),
        Square(20, "Free Parking", "FreeParking"),
        Square(21, "Kentucky Avenue", "Property"),
        Square(22, "Chance 2", "Chance"),
        Square(23, "Indiana Avenue", "Property"),
        Square(24, "Illinois Avenue", "Property"),
        Square(25, "B. & O. Railroad", "Railroad"),
        Square(26, "Atlantic Avenue", "Property"),
        Square(27, "Ventnor Avenue", "Property"),
        Square(28, "Water Works", "Utility"),
        Square(29, "Marvin Gardens", "Property"),
        Square(30, "Go To Jail", "GoToJail"),
        Square(31, "Pacific Avenue", "Property"),
        Square(32, "North Carolina Avenue", "Property"),
        Square(33, "Community Chest 3", "CommunityChest"),
        Square(34, "Pennsylvania Avenue", "Property"),
        Square(35, "Short Line", "Railroad"),
        Square(36, "Chance 3", "Chance"),
        Square(37, "Park Place", "Property"),
        Square(38, "Luxury Tax", "Tax"),
        Square(39, "Boardwalk", "Property")
    ]