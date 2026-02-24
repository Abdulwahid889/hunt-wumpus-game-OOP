from _future_ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from player import Player


class Event(ABC):
    """Abstract base class for all events in the forest."""

    # This is the abstract encounter method
    @abstractmethod
    def encounter_the_event(self, player: Player) -> bool:
        """Handle encounter behavior when player steps on this event."""
        pass

    @abstractmethod
    def get_symbol(self) -> str:
        """Return the display symbol for this event."""
        pass