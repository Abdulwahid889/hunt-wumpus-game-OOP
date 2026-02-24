from _future_ import annotations
from event import Event
from player import Player


class Pond(Event):
    """Represents the pond where the player can drink water."""

    # Implementation of the abstract encounter method override
    def encounter_the_event(self, player: Player) -> bool:
        """Player drinks from the pond if they haven't already."""
        if player.is_thirsty():
            player.drink()
            print("You drink from the pond.")
        else:
            print("You're not thirsty.")
        return False

    def get_symbol(self) -> str:
        """Return 'P' for pond."""
        return "P"