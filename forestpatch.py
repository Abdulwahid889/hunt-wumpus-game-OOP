
from _future_ import annotations
import typing
from event import Event
from player import Player


class ForestPatch:
    """Represents a single patch in the forest grid."""

    # Private attribute storing the event in this patch (or None if empty)
    __event: typing.Optional[Event]

    def _init_(self, event: typing.Optional[Event] = None) -> None:
        """Initialize a forest patch with an optional event."""
        self.__event = event

    def get_event(self) -> typing.Optional[Event]:
        """Get the event in this patch."""
        return self.__event

    def set_event(self, event: typing.Optional[Event]) -> None:
        """Set the event in this patch."""
        self.__event = event

    def is_empty(self) -> bool:
        """Check if this patch has no event."""
        return self.__event is None

    def get_symbol(self) -> str:
        """Get the display symbol for this patch's event."""
        if self.__event is None:
            return " "
        return self.__event.get_symbol()

    def trigger_encounter(self, player: Player) -> None:
        """Trigger the encounter for this patch's event if present."""
        if self.__event is not None:
            should_remove = self.__event.encounter_the_event(player)
            if should_remove:
                self.__event = None