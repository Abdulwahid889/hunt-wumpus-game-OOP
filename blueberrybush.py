class BlueberryBush(event):
    """Represents a blueberry bush the player can eat."""

    # Implementation of the abstract encounter method override
    def encounter_the_event(self, player: player) -> bool:
        """Player eats the blueberry bush."""
        player.eat()
        print("You chow down on some tasty blueberries.")
        return True

    def get_symbol(self) -> str:
        """Return 'B' for blueberry bush."""
        return "B"