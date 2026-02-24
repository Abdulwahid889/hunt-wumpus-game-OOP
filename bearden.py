from _future_ import annotations
from event import Event
from player import Player


class BearDen(Event):
    """Represents a hidden bear den - dangerous if visited twice."""

    def _init_(self) -> None:
        """Initialize the bear den with zero encounters."""
        self._times_encountered: int = 0

    # Implementation of the abstract encounter method override
    def encounter_the_event(self, player: Player) -> bool:
        """First encounter warns and moves back, second encounter kills."""
        self._times_encountered += 1
        if self._times_encountered == 1:
            print("Whew, that was close! You almost woke a nearby bear.")
            player.move_back()
        else:
            print("You woke a nearby bear. It's hungry. Game over.")
            player.lose()
        return False

    def get_symbol(self) -> str:
        """Return ' ' since bear dens are hidden."""
        return " "
