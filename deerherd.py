class DeerHerd(Event):
    """Represents the deer herd - starting and ending point."""

    # Implementation of the abstract encounter method override
    def encounter_the_event(self, player: player) -> bool:
        """Check if player has completed all objectives."""
        if not player.is_hungry() and not player.is_thirsty():
            print("You've finished browsing for the day and arrived "
                  "safely back at the herd.")
            player.win()
        return False

    def get_symbol(self) -> str:
        """Return 'H' for herd."""
        return "H"